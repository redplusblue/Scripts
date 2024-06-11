# This program searches for files with a specific extension in a specific directory and outputs the results to a csv file.

import os, fnmatch, time, csv, win32security

def find_files(directory, pattern):
    """
    Recursively finds all files matching the pattern.
    """
    global directoryMap, ownerMap
    directoryMap, ownerMap = {}, {}
    for root, dirs, files in os.walk(directory):
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                ownerMap[filename] = get_owner(filename)
                directoryMap[filename] = basename
                yield filename
                
def get_owner(filename):
    owner_sid = win32security.GetFileSecurity(filename, win32security.OWNER_SECURITY_INFORMATION).GetSecurityDescriptorOwner()
    # returns a tuple of (domain, type, name) 
    return win32security.LookupAccountSid(None, owner_sid)[0]

def main():
    print("Example extension: .txt")
    extension = input("Enter extension: ")
    print("Example directory: C:/")
    directory = input("Enter directory: ")
    try:
        print("Output file: output.csv")
        print("loading...")
        with open(r'output.csv', 'w', newline='') as csvfile:
            fieldnames = ['Filename', 'Owner','Path', 'Last Modified', 'Date Created']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for filename in find_files(directory, '*' + extension):
                writer.writerow({'Filename': directoryMap[filename],
                                 'Owner': ownerMap[filename],
                                'Path': filename,
                                 'Last Modified': time.ctime(os.path.getmtime(filename)),
                                 'Date Created': time.ctime(os.path.getctime(filename))})

        print("Done!")
        time.sleep(3)
    except Exception as e:
        print('Error:', e)

if __name__ == '__main__':
    main()

#'created by:' + str(getpwuid(os.stat(filename).st_uid).pw_name)