import os
import random
import time
#List of wallpapers
sampledict = {
    "0": "Baki.jpg",
    "1": "JOJO.png",
    "2": "4k-bridge.png",
    "3": "Baki.jpg",
    "4": "Korosensei.png",
    "5": "Eren.jpg",
    "6": "Dragon.jpg",
    "7": "FalseLove.jpg",
    "8": "GoblinSlayer.jpg",
    "9": "JinRoh.jpg",
    "10": "Quintrooplets.png",
    "11": "SpyXFamily.png",
    "12": "Toradora.jpg",
    "13": "TrainGirl.jpg",
    "14": "WeNeverLearn.png",
    "15": "ubuntu-mate.png"
}
#Changes wallpaper
def changer():
    value = str(random.randint(0,15))
    finalval = sampledict[value]
    print("The new picture is: " + finalval)
    os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/dhruv/Pictures/Wallpapers/" + finalval )

if __name__ == "__main__":
    changer()
