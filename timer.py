from termcolor import colored
import time

def pre_timer():
    title = input("what you plan to do? (optional, leave blank if needed):  ")
    while True:
        try:
            time = int(input(f"what would the {colored('duration','cyan')} be? (in minutes): "))
            return time, title
        except (ValueError, Exception):
            print("Use the minutes numeric value only.")


        
def ini_timer(ti_details):
    sec = ti_details[0] * 60

    if len(ti_details[1].replace(' ','')) > 0:
        print(f"\nCurrently doin' : {ti_details[1]}")
    else:
        print()
    while sec >= 0:
        h,rem = divmod(sec,3600)
        m,secs = divmod(rem,60)

        if h > 0:
            s_timer = f"{h:02d}:{m:02d}:{secs:02d}"
        else:
            s_timer = f"{m:02d}:{secs:02d}"

        print(f" ⏰ | Tick-Tock :  {s_timer}  ", end='\r')

        time.sleep(1)
        sec -= 1
    return print("Time's up!!")