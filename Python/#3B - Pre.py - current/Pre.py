import subprocess as sp
import screen_brightness_control as sbc
import time, art, os, psutil, sys

# Lines ending with ## need to be adjusted according to the paths for the script/programs accordingly

def main():
    try:
        if os.path.exists(r" directory of Scripts\files\procID.txt"):
            closeAndRun()
            time.sleep(3)
            sys.exit()
        ########################
        delay = 0.5
        ########################
        print("-Boring console, changing color")
        time.sleep(delay)
        os.system('color 0a')
        time.sleep(delay)
        print("-This is more fun")
        time.sleep(delay)
        print("-Running countdown")
        countdown()
        print("-Globalizing unspecified Popen objects")
        time.sleep(delay)
        global throttleStopRun, afterBurnerRun, vibranceGUIRun
        print("-Adding file-variable indexes")
        time.sleep(delay)
        throttleStop = r"Path to ThrottleStop.exe" ##
        msiAfterburner = r"Path to MSIAfterburner.exe" ## 
        vibranceGUI = r"Path to vibranceGUI.exe" ##
        print("-Opening Throttlestop")
        time.sleep(delay)
        throttleStopRun = sp.Popen(throttleStop)
        print("-Opening MSI Afterburner")
        time.sleep(delay)
        afterBurnerRun = sp.Popen(msiAfterburner)
        print("-Opening Vibrance GUI")
        time.sleep(delay)
        vibranceGUIRun = sp.Popen(vibranceGUI)
        print("-Recording Processs IDs")
        time.sleep(delay)
        saveProcID()
        art.tprint("Adjust 'em!")
        time.sleep(5)
        print("-Changing brightness")
        changeBrightness()
    except Exception as e:
        print("Oops, main function error!")
        print(e)
    
def countdown():
    
    countdown = 3
    art.tprint("\tHi Samir!")
    print(art.decor("random"), art.decor("random"), art.decor("random"), art.decor("random"), art.decor("random"), art.decor("random"))
    print(art.decor("random"), art.decor("random"), art.decor("random"), art.decor("random"), art.decor("random"), art.decor("random"))
    print(art.decor("random"), art.decor("random"), art.decor("random"), art.decor("random"), art.decor("random"), art.decor("random"))
    print("")
    os.system("pause")
    print("")
    while countdown > 0:
        art.tprint(str(countdown), font="rand")
        countdown -= 1
        time.sleep(0.8)
    print("Ready to launch!")
    time.sleep(0.2)

def saveProcID():
    try:
        path = r"C:\Scripts"
        os.chdir(path)
        with open("files/procID.txt", "w+") as f:
            f.write(f"{throttleStopRun.pid}\n{afterBurnerRun.pid}\n{vibranceGUIRun.pid}")
    except Exception as e:
        print("Oops, file-write problem!")
        print(e)

def changeBrightness():
    print("Brightness down in: ")
    countdown = 5
    while countdown > 0: 
        art.tprint(str(countdown))
        countdown -= 1
        time.sleep(0.8)
    sbc.set_brightness(1, method="wmi")
    art.tprint("Have a blast!", font="rand")
    time.sleep(1)
    
def closeAndRun():
    try:
        ####################
        delay = 0.5
        ####################
        time.sleep(delay)
        print("-Preparing to close")
        time.sleep(delay)
        os.system('color 1f')
        time.sleep(delay)
        print("-Initializing process killer")
        def kill(proc_pid):
            process = psutil.Process(proc_pid)
            for proc in process.children(recursive=True):
                proc.kill()
            process.kill()
        def restoreBrightness():
            sbc.set_brightness(80, method="wmi")
        time.sleep(delay)
        print("-Changing Script path")
        path = r"scripts directory" ## 
        os.chdir(path)
        time.sleep(delay)
        print("-Reading Process IDs")
        with open("files/procID.txt", "r+") as f:
            proc_ids = f.read().splitlines()
        time.sleep(delay)
        print(proc_ids)
        time.sleep(delay)    
        print("-Initiating instant kill")
        kill(int(proc_ids[0]))
        time.sleep(delay)
        print("-Throttlestop dead")
        kill(int(proc_ids[1]))
        time.sleep(delay)
        print("-MSI Afterburner dead")
        kill(int(proc_ids[2]))
        time.sleep(delay)
        print("-Vibrance GUI dead")
        time.sleep(0.5)
        print("-Restoring brightness")
        restoreBrightness()
        time.sleep(delay)
        print("-Removing proc IDs")
        os.remove("files/procID.txt")
        time.sleep(delay)
        print("-All done!")
        art.tprint("Hope you had fun!")
        time.sleep(3)
        
    except Exception as e: 
        print("A problem in killing 😏")
        print(e)        
    
if __name__ == "__main__":
    main()