# script for pasting
from time import sleep
with open("/home/cid/Desktop/lafskh/code tantra/file.txt","r+") as f:
    txt = f.read()

for line in txt.split("\n"):
    sleep(0.051)
    keyboard.press_key("<shift>")
    keyboard.fake_keypress("<tab>",repeat=20)
    keyboard.release_key("<shift>")
    keyboard.send_keys(line)
    keyboard.send_keys("<enter>")
    