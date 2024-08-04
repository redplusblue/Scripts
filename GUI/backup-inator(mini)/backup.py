import tkinter as tk
from tkinter import ttk
import os, shutil, datetime, threading, subprocess, time

# EXE: pyinstaller --onefile --noconsole .\backup.py

class BackupApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Backup Application")
        self.geometry("600x500")  # Increased height to accommodate new settings
        self.create_main_screen()
        self.create_advanced_screen()

        self.show_main_screen()

    def create_main_screen(self):
        self.main_frame = ttk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        screen_frame = ttk.Frame(self.main_frame, height=250)
        screen_frame.pack(fill=tk.X, padx=10, pady=10)
        screen_frame.pack_propagate(False)

        self.screen = tk.Text(screen_frame, wrap=tk.WORD, bg="black", fg="white", font=("Arial", 12))
        self.screen.pack(fill=tk.BOTH, expand=True)

        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        button_frame.columnconfigure(0, weight=1)

        button_style = ttk.Style()
        button_style.configure('Large.TButton', font=('Arial', 14))

        self.cloud_backup_var = tk.BooleanVar(value=True)
        self.cloud_backup_checkbox = ttk.Checkbutton(button_frame, text="Enable Cloud Backup", variable=self.cloud_backup_var)
        self.cloud_backup_checkbox.grid(row=0, column=0, pady=(0, 10))

        self.backup_button = ttk.Button(button_frame, text="Backup", command=self.start_backup, style='Large.TButton', width=20)
        self.backup_button.grid(row=1, column=0, pady=(0, 10))

        self.advanced_button = ttk.Button(button_frame, text="Advanced", command=self.show_advanced_screen, style='Large.TButton', width=20)
        self.advanced_button.grid(row=2, column=0)
        
        ttk.Label(button_frame, text="backup-inator(mini) © Samir Kabra", font=("Arial", 8)).grid(row=3, column=0, pady=(10, 0))

    def create_advanced_screen(self):
        self.advanced_frame = ttk.Frame(self)

        ttk.Label(self.advanced_frame, text="Drive Name:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.drive_name_var = tk.StringVar(value="DRIVE")
        ttk.Entry(self.advanced_frame, textvariable=self.drive_name_var).grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(self.advanced_frame, text="Backup Folder:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.backup_folder_var = tk.StringVar(value="E:\\backup")
        ttk.Entry(self.advanced_frame, textvariable=self.backup_folder_var).grid(row=1, column=1, padx=5, pady=5)

        ttk.Label(self.advanced_frame, text="Shares Source Path:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.shares_src_var = tk.StringVar(value="C:\\Users\\USER\\Desktop")
        ttk.Entry(self.advanced_frame, textvariable=self.shares_src_var).grid(row=2, column=1, padx=5, pady=5)

        ttk.Button(self.advanced_frame, text="Save & Return", command=self.show_main_screen).grid(row=3, column=0, columnspan=2, pady=20)

    def show_main_screen(self):
        self.advanced_frame.pack_forget()
        self.main_frame.pack(fill=tk.BOTH, expand=True)

    def show_advanced_screen(self):
        self.main_frame.pack_forget()
        self.advanced_frame.pack(fill=tk.BOTH, expand=True)

    def start_backup(self):
        self.backup_button.config(state="disabled")
        self.advanced_button.config(state="disabled")
        self.cloud_backup_checkbox.config(state="disabled")
        self.screen.delete(1.0, tk.END)
        threading.Thread(target=self.perform_backup, daemon=True).start()

    def perform_backup(self):
        try:
            self.update_screen("Starting backup process...", "white")
            
            DRIVE_NAME = self.drive_name_var.get()
            CUR_DATE = "31.3." + str(datetime.datetime.now().year)
            
            backup_folder = self.backup_folder_var.get()
            backup_drive = None

            self.update_screen("Checking backup folder...", "white")
            if not os.path.exists(backup_folder):
                raise FileNotFoundError("The backup folder does not exist.")
            # if not os.listdir(backup_folder):
            #     raise ValueError("The backup folder is empty.")
            self.update_screen("✓ Backup folder check complete", "green")
            
            self.update_screen("\nCopying shares directory from desktop...", "white")
            try:
                self.copy_shares_directory()
            except Exception as e:
                self.update_screen(f"! Failed to copy shares directory: {str(e)}", "red")
                raise  # Re-raise the exception to stop execution

            self.update_screen("Checking for backup drive...", "white")
            drives = os.popen("wmic logicaldisk get deviceid, volumename").read()
            drives = [drive.split() for drive in drives.split('\n') if drive.strip()]
            
            drive_exists = False
            for drive in drives:
                if len(drive) > 1 and drive[1] == DRIVE_NAME:
                    backup_drive = [drive[0], drive[1]]
                    drive_exists = True
                    break
            
            if not drive_exists:
                raise ValueError(f"The drive with the name {DRIVE_NAME} does not exist.")
            self.update_screen(f"✓ Backup drive '{DRIVE_NAME}' found", "green")

            drive_backup_folder = f"{backup_drive[0]}\\backup"
            if not os.path.exists(drive_backup_folder):
                self.update_screen("Creating backup folder on the drive...", "white")
                os.mkdir(drive_backup_folder)
                self.update_screen("✓ Backup folder created on the drive", "green")

            self.update_screen("Copying files and folders...", "white")
            destination_folder = f"{drive_backup_folder}\\{CUR_DATE}"
            if not os.path.exists(destination_folder):
                os.mkdir(destination_folder)

            for item in os.listdir(backup_folder):
                src_path = os.path.join(backup_folder, item)
                dst_path = os.path.join(destination_folder, item)
                if os.path.isfile(src_path):
                    shutil.copy2(src_path, dst_path)
                elif os.path.isdir(src_path):
                    shutil.copytree(src_path, dst_path)
            
            self.update_screen("✓ Files and folders copied successfully", "green")            

            if self.cloud_backup_var.get():
                self.update_screen("\nStarting cloud backup...", "white")
                try:
                    cloud_destination = f"mega:backups/{CUR_DATE}"
                    rclone_command = f"rclone copy {destination_folder} {cloud_destination} --create-empty-src-dirs"
                    result = subprocess.run(rclone_command, shell=True, capture_output=True, text=True)
                    
                    if result.returncode == 0:
                        self.update_screen("✓ Cloud backup completed successfully", "green")
                    else:
                        raise Exception(f"Cloud backup failed: {result.stderr}")
                except Exception as e:
                    self.update_screen(f"! Cloud backup failed: {str(e)}", "red")
                    self.update_screen("Continuing with local backup only.", "yellow")

            self.update_screen("\nSUCCESS", "green")
            self.update_screen(f"Backup for {CUR_DATE} complete.", "green")
            # Clear the backup folder contents after successful backup
            for item in os.listdir(backup_folder):
                if os.path.isfile(os.path.join(backup_folder, item)):
                    os.remove(os.path.join(backup_folder, item))
                else:
                    shutil.rmtree(os.path.join(backup_folder, item))

        except Exception as e:
            self.update_screen(f"\nFAILURE\n\nError: {str(e)}\n", "red")
            self.update_screen("Please take a screenshot of this screen and contact Samir.", "red")
        finally:
            self.backup_button.config(state="normal")
            self.advanced_button.config(state="normal")
            self.cloud_backup_checkbox.config(state="normal")

    def update_screen(self, message, color):
        self.screen.insert(tk.END, message + "\n")
        self.screen.tag_add(color, f"end-{len(message)+1}c linestart", "end-1c")
        self.screen.tag_config(color, foreground=color)
        self.screen.see(tk.END)
        self.update_idletasks()

    def copy_shares_directory(self):
        src = self.shares_src_var.get()
        dst = self.backup_folder_var.get()
        date = str(time.localtime().tm_year)[2:]
        to_find = 'shares'

        def search_dir(directory):
            res = []
            for root, dirs, files in os.walk(directory):
                for dir in dirs:
                    if to_find.lower() in dir.lower():
                        res.append(os.path.join(root, dir))
   
            self.update_screen(f"Found {len(res)} results", "white")
            
            if len(res) > 1:
                res = [r for r in res if date in r]
   
            return res[0] if res else None
       
        dir = search_dir(src)
        if dir:
            self.update_screen(f"Directory found: {dir}", "white")
            new_dir = os.path.join(dst, f'shares 31.3.{date}')
            shutil.copytree(dir, new_dir)
            self.update_screen("✓ Shares directory copied successfully", "green")
        else:
            raise FileNotFoundError("Shares directory not found")

if __name__ == "__main__":
    app = BackupApp()
    app.mainloop()