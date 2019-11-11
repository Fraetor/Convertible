"""
A program to detect when a convertible laptop switches to tablet mode, and enable or disable the onscreen keyboard.

@author James Frost <jwfab@live.com>
"""
import struct
import subprocess
import time

# We need to read binary from the /dev/input/by-path/XXX file.
# Then we need to process this binary to make it readable.
# Finally we can run commands based on the value.
# Much information for this was acquired from the following sources:
# https://thehackerdiary.wordpress.com/2017/04/21/exploring-devinput-1/
# https://askubuntu.com/questions/591757/how-to-activate-deactivate-a-gnome-shell-extension-from-command-line

input_device = "/dev/input/by-path/platform-thinkpad_acpi-event"


def tablet_mode():
    # print("Tablet Mode")
    subprocess.run(["gnome-extensions", "disable", "cariboublocker@git.keringar.xyz"], check=True)
    return


def laptop_mode():
    # print("Laptop Mode")
    subprocess.run(["gnome-extensions", "enable", "cariboublocker@git.keringar.xyz"], check=True)
    return


def tablet_detector():
    event_file = open(input_device, "rb")
    while True:
        event_bin = event_file.read(24)
        event = struct.unpack('HHI', event_bin[16:])
        if event[0] == 5 and event[1] == 1:
            if event[2] == 1:
                tablet_mode()
            else:
                laptop_mode()
        time.sleep(1)


tablet_detector()
