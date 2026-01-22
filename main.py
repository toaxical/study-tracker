from datetime import datetime as dt
import study
import json
import timer 
from tabulate import tabulate

def recordparse(rcrd,id):
    to_apnd = {}
    to_apnd[id] = rcrd

    with open('records.jsonl', 'a') as ap_session:
        try: 
            ap_session.write(json.dumps(to_apnd) + '\n')
        except Exception:
            return 'something went wrong with recording the session! helppppppp!!'

def view_records():
    records = []
    table_details = []

    with open('records.jsonl', 'r') as read_session:
        try:
            for line in read_session:
                records.append(json.loads(line))
        except Exception:
            print(f"An {Exception} occured, pls try again")

        print('\n- - - - - - - - - - - - - - - - - - - - - - - - - -')
        print('📚 Past Study Sessions')
        print('- - - - - - - - - - - - - - - - - - - - - - - - - -')
        if records:
            for task in records:
                for time, details in task.items():
                    details.append(time)
                    if details[2] > 59:
                        hrs,mins = divmod(details[2],60)
                        details[2] = f"{hrs}h{mins}m"
                        table_details.append(details)
                    else:
                        details[2] = f"{details[2]}min"
                        table_details.append(details)
            print(tabulate(table_details, headers=['Subject', 'Goal', 'Duration', 'Date'], tablefmt="orgtbl"))
            print()
        else:
            print(".....Nothing to show here 🎈\n")
    return

def main():
    while True:
        while True:
            try:
                usr_ch = int(input("What yo ahh wanna do? : \n 1. i wanna study lol \n 2. just start a timer bro \n 3. show me my records \n 4. stfu bye\n"))

                if usr_ch == 1:
                    rcrd_id = dt.now().strftime("%Y-%m-%d %H:%M")
                    rcrd = study.pre_study()
                    study.ini_study(rcrd) 
                    recordparse(rcrd,rcrd_id)

                elif usr_ch == 2:
                    ti_details = timer.pre_timer()
                    timer.ini_timer(ti_details)

                elif usr_ch == 3:
                    view_records()

            except (ValueError):
                print("what even is that?\n")
            
            else:
                if usr_ch == 4:
                    break

        if usr_ch == 4:
                    print("\nbye meanie 🙁\n")
                    break

if __name__ == '__main__':
    main()