
from datetime import datetime   
from playsound import playsound
alarm_time = input("enter the time of alarm to be set: HH/MM/SS\n")
splitted = alarm_time.split("/")
while True:
    current_time = datetime.now()
    if(splitted[0]==current_time.strftime("%H")):
        if(splitted[1] == current_time.strftime("%M")):
            if(splitted[2] == current_time.strftime("%S")):
                print("Uyanma vaktısı")
                break

'''
ALTERNATİF KOD 

from datetime import datetime   
from playsound import playsound
alarm_time = input("Enter the time of alarm to be set:HH:MM:SS\n")
alarm_hour=alarm_time[0:2]
alarm_minute=alarm_time[3:5]
alarm_seconds=alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Setting up alarm..")
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_period==current_period):
        if(alarm_hour==current_hour):
            if(alarm_minute==current_minute):
                if(alarm_seconds==current_seconds):
                    print("Wake Up!")
                    playsound('audio.mp3')
                    break
'''
