from datetime import date
from datetime import datetime
from colorama import Fore, Back, Style

def fulltime():
#Todays date
    now = date.today()
#Hour and minute conversions
    current = datetime.now()
    hour = int(current.strftime("%H"))
    minute = current.strftime("%M")
    transdate = now.strftime("%B, %d, %Y")
    cycle = ""
#Checks if time is AM or PM
    if hour >= 12:
        convhour =  str(hour - 12)
        cycle = "PM"
    else:
        convhour = str(hour)
        cycle = "AM"
    print("The date is " + Fore.YELLOW + Style.BRIGHT + Back.BLACK + transdate +  " and it is currently " + convhour + " " + cycle +  " and " + minute + " minutes" + Back.RESET)

if __name__ == "__main__":
    fulltime()
