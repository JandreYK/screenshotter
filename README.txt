Screenshotter is a Python script designed to automatically take screenshots whenever the left mouse button is clicked. This can be particularly useful for creating visual documentation, capturing moments during gameplay, or any other activity requiring frequent screenshots.

How It Works
When the script is running, it listens for left mouse clicks. Each time a left click is detected, it captures the current screen and saves the screenshot as a JPEG file in the specified output folder.

Requirements
Python 3.x
Pillow library (for handling image captures)
pynput library (for monitoring mouse events)
You can install the required libraries using pip:

  pip install pillow pynput

Usage
Run the script and follow the prompts in the console:

Confirm that you are ready to start the screenshot process.
Specify the folder where screenshots will be saved.
Provide a prefix for naming the screenshot files.
Ensure that the specified folder exists and that you have write permissions to save files there.

The script will then run in the background, taking screenshots on each left mouse click.

To stop the script, type END in the console.


Notes
Make sure the folder you specify for saving screenshots has write permissions.
The screenshots are saved with a filename pattern of [prefix]_[timestamp].jpg.
