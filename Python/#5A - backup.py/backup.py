import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
import logging
import datetime
import requests

# Name/path of the log file to store backup information 
LOG_FILE = 'backup_log.txt'

# Global variable for the ntfy topic name
NTFY_TOPIC = 'SET THIS TO YOUR NTFY TOPIC NAME'

class BackupApp:
    """
    A class representing a backup application.

    Attributes:
        root (tk.Tk): The root window of the application.
        source_dirs (list): A list of source directories to be backed up.
        destination_dir (str): The destination directory where the backups will be stored.
        backup_number (int): The number of the backup.

    Methods:
        __init__(self, root): Initializes the BackupApp object.
        browse_source(self): Opens a file dialog to select source directories.
        browse_destination(self): Opens a file dialog to select the destination directory.
        review_log_files(self): Reviews log files and counts the number of backups.
        send_notification(self, message): Sends a notification with the given message.
        backup(self): Performs the backup operation.
    """

    def __init__(self, root):
        """
        Initializes the BackupApp object.

        Args:
            root (tk.Tk): The root window of the application.
        """
        self.root = root
        self.source_dirs = []
        self.destination_dir = ''
        self.backup_number = 1

        # Rest of the code...
class BackupApp:
    def __init__(self, root):
        self.root = root
        self.source_dirs = []
        self.destination_dir = ''
        self.backup_number = 1

        self.source_label = tk.Label(root, text="Source directories:")
        self.source_label.pack()

        self.source_entry = tk.Entry(root, width=50)
        self.source_entry.pack()

        self.source_button = tk.Button(root, text="Browse", command=self.browse_source)
        self.source_button.pack()

        self.destination_label = tk.Label(root, text="Destination directory:")
        self.destination_label.pack()

        self.destination_entry = tk.Entry(root, width=50)
        self.destination_entry.pack()

        self.destination_button = tk.Button(root, text="Browse", command=self.browse_destination)
        self.destination_button.pack()

        self.backup_button = tk.Button(root, text="Backup", command=self.backup)
        self.backup_button.pack()

        self.progressbar = Progressbar(root, orient='horizontal', length=200, mode='determinate')
        self.progressbar.pack()

        self.log_field = tk.Text(root, height=10, width=40)
        self.log_field.pack()

        # Set up logging
        logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

        # Review log files and count the number of backups
        self.review_log_files()

    def browse_source(self):
        dirs = filedialog.askopenfilenames(title="Select source directories")
        self.source_entry.delete(0, tk.END)
        self.source_entry.insert(tk.END, ', '.join(dirs))
        self.source_dirs = dirs

    def browse_destination(self):
        dir = filedialog.askdirectory(title="Select destination directory")
        self.destination_entry.delete(0, tk.END)
        self.destination_entry.insert(tk.END, dir)
        self.destination_dir = dir

    def review_log_files(self):
        try:
            with open(LOG_FILE, 'r') as f:
                log_lines = f.readlines()
                dates = set(line[:10] for line in log_lines)
                self.backup_number = len(dates) + 1
                self.log_field.insert(tk.END, f"Backup number: {self.backup_number}\n")
                self.log_field.see(tk.END)
                self.root.update_idletasks()
        except FileNotFoundError:
            pass

    def send_notification(self, message):
        try:
            requests.post(f'https://ntfy.sh/{NTFY_TOPIC}', data=message.encode('utf-8'))
        except requests.exceptions.RequestException as e:
            self.log_field.insert(tk.END, f"Error sending notification: {str(e)}\n")
            self.log_field.see(tk.END)
            self.root.update_idletasks()

    def backup(self):
        if not self.source_dirs or not self.destination_dir:
            messagebox.showerror("Error", "Please select source directories and destination directory")
            return

        self.progressbar['maximum'] = len(self.source_dirs)
        self.progressbar['value'] = 0

        # Create a subdirectory in the destination directory with the current date
        date_dir = os.path.join(self.destination_dir, datetime.date.today().isoformat())
        os.makedirs(date_dir, exist_ok=True)

        for i, dir in enumerate(self.source_dirs):
            try:
                self.log_field.insert(tk.END, f"Backing up {dir}...\n")
                self.log_field.see(tk.END)
                self.root.update_idletasks()

                if os.path.isfile(dir):
                    shutil.copy2(dir, date_dir)
                else:
                    shutil.copytree(dir, os.path.join(date_dir, os.path.basename(dir)))

                logging.info(f"Backed up {dir} to {date_dir}")

                self.log_field.insert(tk.END, f"Backup of {dir} complete\n")
                self.log_field.see(tk.END)
                self.root.update_idletasks()
            except Exception as e:
                self.log_field.insert(tk.END, f"Error backing up {dir}: {str(e)}\n")
                self.log_field.see(tk.END)
                self.root.update_idletasks()
                logging.error(f"Error backing up {dir}: {str(e)}")

            self.progressbar['value'] += 1
            self.root.update_idletasks()

        self.log_field.insert(tk.END, "Backup complete\n")
        self.log_field.see(tk.END)
        self.root.update_idletasks()

        # Send a notification
        self.send_notification(f"Backup #{self.backup_number} Successful")

if __name__ == "__main__":
    root = tk.Tk()
    app = BackupApp(root)
    root.mainloop()