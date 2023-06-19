# Stopwatch

import time
import msvcrt

print("hi this is a stopwatch made by shook-s ")

def start():
    global start_stop
    timimg = 0
    if start_stop == "Y":
        print("Press N and enter it to stop")
        time.sleep(1)
        while start_stop == "Y":
            time.sleep(0.1)
            timimg += 0.1
            print(round(timimg, 3))
            if msvcrt.kbhit():
                key = msvcrt.getch().decode()
                if key.lower() == "n":
                    print(f"You final time is {timimg}")
                    break
        return timimg


while True:
    start_stop = input("Do you want to start the stopwatch Y/N\n")
    if start_stop in ["Y","y",'1','N','n','2']:
        if start_stop in ["Y","y",'1']:
            start_stop = "Y"
            start()
        else:
            print("bye bye")
        break
    else:
        print("You have to pick either Y or N")
