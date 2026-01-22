import time
from termcolor import colored
def pre_study():
    
    print("\nOkie, answer a few questions first: \n")

    subj = input(f"What's the {colored('Subject','cyan')} you'll be studying?: ")
    aim = input(f"What's the {colored('theme/topic','cyan')} of the session?: ")
    
    while True:
        try:
            dur = int(input(f"What will be the {colored('duration','cyan')} of the session? (in minutes): "))      
            return subj, aim, dur
        except (TypeError, ValueError):
            print("what even is that duration?")


def ini_study(rcrd):
    print(f"\n ꉂ(˵˃ ᗜ ˂˵) | Studying {colored(rcrd[0].title(),'magenta')} ~ Topic: {colored(rcrd[1], 'light_blue')}\n")
    sec = rcrd[2] * 60

    while sec >= 0:
        h,rem = divmod(sec,3600)
        m,secs = divmod(rem,60)

        if h > 0:
            s_timer = f"{h:02d}:{m:02d}:{secs:02d}"
        else:
            s_timer = f"{m:02d}:{secs:02d}"

        print(f"Tick-Tock: {s_timer}     ", end='\r')
        time.sleep(1)
        sec -= 1
    print(f"⸜(｡˃ ᵕ ˂ )⸝♡ | Session over. Yayyy! \n 🔖")

    return
