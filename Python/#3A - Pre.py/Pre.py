import subprocess as sp
import screen_brightness_control as sbc
import time, art, os, psutil, sys

# Lines ending with ## are paths to the script/programs that need to be adjusted accordingly

def main():
    try:
        if os.path.exists(r" directory : files\procID.txt"): ##
            closeAndRun()
            time.sleep(3)
            sys.exit()
        ########################
        delay = 0.5
        ########################
        countdown()
        global throttleStopRun, afterBurnerRun, vibranceGUIRun
        throttleStop = r"path to ThrottleStop.exe" ##
        msiAfterburner = r"path to MSIAfterburner.exe" ## 
        vibranceGUI = r"path to vibranceGUI.exe" ## 
        throttleStopRun = sp.Popen(throttleStop)
        afterBurnerRun = sp.Popen(msiAfterburner)
        vibranceGUIRun = sp.Popen(vibranceGUI)
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
        def kill(proc_pid):
            process = psutil.Process(proc_pid)
            for proc in process.children(recursive=True):
                proc.kill()
            process.kill()
        def restoreBrightness():
            sbc.set_brightness(80, method="wmi")
        path = r"script directory path" ## 
        os.chdir(path)
        with open("files/procID.txt", "r+") as f:
            proc_ids = f.read().splitlines()
        kill(int(proc_ids[0]))
        kill(int(proc_ids[1]))
        kill(int(proc_ids[2]))
        time.sleep(0.5)
        print("-Restoring brightness")
        restoreBrightness()
        os.remove("files/procID.txt")
        art.tprint("Hope you had fun!")
        time.sleep(3)
        
    except Exception as e: 
        print("A problem in killing 😏")
        print(e)        
    
if __name__ == "__main__":
    main()