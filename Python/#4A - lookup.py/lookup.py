import os, fnmatch, time, csv
from pwd import getpwuid

print("Example extension: .txt")
extension = input("Enter extension: ")
print("Example directory: /c")
directory = input("Enter directory: ")
#directory = '/c'

directoryMap = {} 

def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                directoryMap[filename] = basename
                yield filename

# for filename in find_files(directory, '*' + extension):
#     print ('Found:', directoryMap[filename], 'path:', filename , 'last modified:', time.ctime(os.path.getmtime(filename)), 'created:', time.ctime(os.path.getctime(filename)), 'created by:', getpwuid(os.stat(filename).st_uid).pw_name)

# store the output in csv file
with open('output.csv', newline='', mode='w+') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for filename in find_files(directory, '*' + extension):
        spamwriter.writerow([directoryMap[filename],'path:' + str(filename), 'last modified:' + str(time.ctime(os.path.getmtime(filename))), 'created:' + str(time.ctime(os.path.getctime(filename))), 'created by:' + str(getpwuid(os.stat(filename).st_uid).pw_name)])
