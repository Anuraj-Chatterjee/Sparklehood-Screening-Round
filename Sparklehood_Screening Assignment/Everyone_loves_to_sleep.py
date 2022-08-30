import math
import fileinput

hours = 0
minutes = 0

list_hours_minutes = []

test_cases = 0
number_of_alarms = 0
bed_time_hour = 0
bed_time_minutes = 0
sleep_time =0
sleep_hours=0
sleep_minutes=0

file_variable  = open("Input.txt","r")
file_variable_1 = open("Output.txt","w")

test_cases = int(file_variable.readline())

for i in range(0,test_cases) :
    number_of_alarms,bed_time_hour,bed_time_minutes = list(map(int, file_variable.readline().split()))
    bed_time_combined = bed_time_hour*60 + bed_time_minutes
    list_hours_minutes=[]
    for j in range(0,number_of_alarms) :
        hours,minutes = list(map(int, file_variable.readline().split()))
        list_hours_minutes.append(hours*60 + minutes)
    list_hours_minutes.sort()
    for j in range(0,number_of_alarms-1) :
        if bed_time_combined == list_hours_minutes[j] :
            sleep_time=0
            break
        elif bed_time_combined > list_hours_minutes[j] and bed_time_combined < list_hours_minutes[j+1] :
            sleep_time=list_hours_minutes[j+1] - bed_time_combined
            break
    if bed_time_combined == list_hours_minutes[number_of_alarms-1] :
        sleep_time = 0
    elif bed_time_combined > list_hours_minutes[number_of_alarms-1] :
        sleep_time = 1440 - bed_time_combined + list_hours_minutes[0]
    else :
        sleep_time = list_hours_minutes[0] - bed_time_combined
    sleep_hours = int(sleep_time/60)
    sleep_minutes = sleep_time%60

    file_variable_1.write(str(sleep_hours)+" "+str(sleep_minutes) + "\n")
file_variable.close()
file_variable_1.close()