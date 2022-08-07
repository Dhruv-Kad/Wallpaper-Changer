from wallchanger import changer
from currentime import fulltime
from timer import main
import random
import time
from colorama import Fore
# fulltime() - Gets current time
# changer() - Wallpaper changer
# main() - Optional timer
manual = input("Do you want to manually or automatically choose the wallpaper uptime? (A/M): ")
convman = manual.upper()


while 1 == 1:
    fulltime()
    if convman == 'M':
        changer()
        main()
    elif convman == 'A':
        raw0 = random.randint(600, 900)
        min0 = int(raw0/60)
        str0 = str(min0)
        print(str0 + " minute cycle ")
        changer()
        time.sleep(raw0)
    else:
        print( Fore.RED + "Please input yes or no")
        break



