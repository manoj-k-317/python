#this file exixts in sub branch
import time
mytime = int(input("enter your time: "))
for i in reversed(range (1, mytime)):
    time.sleep(1)
    seconds = int(i%60)
    minutes = int(i/60)%60
    hours = int(i/3600)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")