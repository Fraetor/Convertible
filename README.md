# Convertible
A program to detect when a convertible laptop switches to tablet mode, and enable or disable the onscreen keyboard.

### Requirements:
* Python 3.5+,
* GNOME 3,
* Block Caribou GNOME extension (https://github.com/keringar/cariboublocker)

### Installation
1. Install the "Block Caribou" extension from https://extensions.gnome.org/extension/1326/block-caribou/
2. Clone this project with `git clone https://github.com/Fraetor/Convertible.git`
3. Add the line `python3 /path/to/convertible.py &` to your `~/.profile`, replacing the path with the path to this project.
4. Add your user to the "input" group with the command `sudo usermod -a -G input [User]`
5. Run `source ~/.profile` or reboot.

Only currently tested on my ThinkPad L390 Yoga running Ubuntu 19.10. It should work for most modern ThinkPads as is, but
for different models the "input_device" variable will have to be adjusted and perhaps the indexes of the binary data
changed. If it works on you device, or does not then please add an issue so I can add support.
