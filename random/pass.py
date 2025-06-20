# set a pass, take user input and compare
# if userIn!=pass then timeout x seconds starting x=2
# retake input on each failed attempt upto 5 times and timeout=x*2

import time
import sys


password="Password"
userIn=input("Enter password: ")
# print(userIn, password)

timeout=2
for i in range(4):
    # print(i)
    if userIn==password:
        print("Correct Password")
        sys.exit(0)
    else:
        time.sleep(timeout)
        userIn=input(F"Timed out for {timeout} seconds, Re-enter Password: ")
        timeout*=2

print("Banned for 5 wrong passwords")