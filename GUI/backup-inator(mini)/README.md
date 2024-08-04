### A simple custom made backup script (Compiled to exe for windows) using python

It:

1. Gathers data from specific locations (With folders matching certain names)
2. Stores the data into an intermediary folder in another drive
3. Backs up the data into a external drive with a specific name, also backs it up to the cloud using Rclone
4. Deletes the intermediary folder

most of these params can be edited by going to the "Advanced" tab in the GUI, but some path names might be hardcoded in the script itself.
