## Backup Script

This script is a simple backup application that allows you to back up multiple source directories to a destination directory. It provides a graphical user interface (GUI) using the Tkinter library.

### Features

- Select multiple source directories to be backed up.
- Choose a destination directory where the backups will be stored.
- Review log files and count the number of backups.
- Send a notification after each successful backup.
- Progress bar to track the backup progress.
  Error handling for file and directory operations.

### Prerequisites

- Python 3.x
- Tkinter library
- Requests library

### Usage

1. Clone the repository or download the script file.
2. Install the required libraries by running the following command:

```bash
pip install tkinter requests
```

3. Run the script using the following command:

```bash
python backup_script.py
```

4. The GUI window will open.
5. Click the "Browse" button next to "Source directories" to select the directories you want to back up.
6. Click the "Browse" button next to "Destination directory" to select the directory where the backups will be stored.
7. Click the "Backup" button to start the backup process.
8. The progress bar will show the progress of the backup operation.
9. The log field will display the status of each backup and any errors encountered.
10. After the backup is complete, a notification will be sent.

### Configuration

The name and path of the log file can be configured by modifying the `LOG_FILE` variable in the script.
The NTFY topic name can be set by modifying the `NTFY_TOPIC` variable in the script.

#### License

This script is licensed under the MIT License.

#### Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

Contact
If you have any questions or suggestions, please feel free to [contact me](https://samirkabra.com).
