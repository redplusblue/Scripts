# This program finds all files with a given extension in a given directory and its subdirectories and stores the output in a csv file.

import os, fnmatch, time, csv
from pwd import getpwuid

def find_files(directory, pattern):
    """
    Recursively finds all files matching the pattern.
    """
    global directoryMap
    directoryMap = {}
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                directoryMap[filename] = basename
                yield filename

def main():
    print("Example extension: .txt")
    extension = input("Enter extension: ")
    print("Example directory: /home")
    directory = input("Enter directory: ")
    # check if directory exists
    if not os.path.isdir(directory):
        print("Directory does not exist")
        return
     
    # store the output in csv file
    print("Output file: output.csv")
    print("Please wait...")
    with open('output.csv', newline='', mode='w+') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for filename in find_files(directory, '*' + extension):
            spamwriter.writerow([directoryMap[filename],
                                 'path:' + str(filename), 
                                 'last modified:' + str(time.ctime(os.path.getmtime(filename))), 
                                 'created:' + str(time.ctime(os.path.getctime(filename))), 
                                 'created by:' + str(getpwuid(os.stat(filename).st_uid).pw_name)])
    print("Done!")
    
if __name__ == '__main__':
    main()