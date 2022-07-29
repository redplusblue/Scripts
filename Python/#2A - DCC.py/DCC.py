from datetime import date
from importlib.resources import path
from pathlib import Path
from os import system, chdir

today = date.today().strftime("%b-%d-%Y")
currentDate = date.today().strftime("%d")
currentMonth = date.today().strftime("%b")
currentYear = date.today().strftime("%Y")
#################################################
# Set directory here:
directory = "C:/Users/user/Documents/GitHub/DCC"
# Set path to your *root* github folder [Where you set up git bash]
path = r""
#################################################
folderName = "/" + today
fileName = folderName + "/problem.txt"

def directoryCreator():    
    try:
        global directory
        if currentDate == "01":
            if currentMonth == "Jan":
                #Create folder for new calender year
                Path(directory + "/" + str(currentYear)).mkdir()

            directory += "/" + currentYear + "/" + currentMonth
            #Create folder for new month
            Path(directory).mkdir()
            currentDir = directory 
        
        else:
            currentDir = directory + "/" + currentYear + "/" + currentMonth
        
        Path(currentDir+folderName).mkdir()
        
    except FileExistsError: 
        print("Directory Already Exists!")
        
    except FileNotFoundError:
        Path(directory+"/"+currentYear).mkdir()
        Path(directory+"/"+currentYear+"/"+currentMonth).mkdir()

def fileCreator():
    try:
        localDir = directory
        #localDir += f"/{currentYear}/{currentMonth}"
        with open(localDir+fileName, 'w') as f:
            f.write(f"Problem for {today} :")
             
    except FileNotFoundError:
        print("Directory does not exist!")
        
def sendToGit():
    try: 
        chdir(path)
        system('git add DCC && git commit -m"Auto Commit" && git push origin main')
    except Exception as e:
        print(e)

def main():
    #Create Directory
    directoryCreator()
    
    #Create file in Directory
    fileCreator()
    
    #Empty Push to GitHub
    sendToGit()
    
if __name__ == "__main__":
    main()
