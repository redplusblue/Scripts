# Pre.py

## Purpose: 
To open three programs, Throttlestop, MSI Afterburner, and Vibrance GUI to load my configurations (Undervolt/Overclock as well as custom NVDIA colour scheme) and decrease brightness of one of my monitors. 
Script also saves the process ID of the processes into a text file after its run, which it checks for if run again, and if there are process IDs, it clears the process tree and restores brightness, also deletes the file to avoid confusion.

## Screenshot: 
<img src="files/preview.png">

## Python libraries used: 
<ul>
<li><code>subprocess[sp]</code></li>
<li><code>screen_brightness_control[sbc]</code></li>
<li><code>time</code></li>
<li><code>art</code></li>
<li><code>psutil</code></li>
<li><code>os</code></li>
<li><code>sys</code></li>

## Also see [Pre.bat](google.com)
