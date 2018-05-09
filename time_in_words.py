#!/bin/python3

import sys

def generate_all_times():
    return {str(h)+ ':' + str(m) if m > 9 else str(h)+ ':' + '0' + str(m) : to_time(h,m) for h in range(1,13) for m in range(0,60)  }
    
def timeInWords(h, m):
    
    if h < 1 or h > 12 or m < 0 or m > 59:
        raise ValueError('hours 1-12 mins 0-59 required')
    
    hours = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve']
    mins = hours + ['thirteen', 'fourteen', 'fifteen', 'sixteen','seventeen','eighteen','nineteen']
    units = ['twenty','thirty','forty','fifty','sixty']

    minutes_in_hour = mins + [ units[x] +' ' + hours[i-1]  for x in range(len(units)) for i in range(1,11)]
    minutes_in_hour = minutes_in_hour[1:60]
    minutes_in_hour = [''] + minutes_in_hour
    
    minutes_in_hour[15] = 'quarter'
    minutes_in_hour[30] = 'half '

    minutes_to = 'minutes_to'
    past = 'past'
    oclock = "o' clock"
    first_30 = [ x + ' minutes '+past for x in minutes_in_hour[1:30] ] + [minutes_in_hour[30] + past]
    last_30 = [x for x in reversed(minutes_in_hour[1:30])]
    last_30 = [x + ' minutes to' for x in last_30]
    all_number = first_30 + last_30
    all_number[44] = 'quarter to'


    all_number[14] = 'quarter past'
    all_number[0] = 'one minute past'
    all_number[58] = 'one minute to'

    t = [ hours[h] + ' '+ oclock ] + [  x  + ' '+ hours[h] for x in all_number[:30]]
    t2 = [x  + ' '+ hours[((h+1) % 12)]  for x in all_number[30:]]
    
    time_hour_mins = t + t2
    return time_hour_mins[m]

if __name__ == "__main__":
    h = int(input().strip())
    m = int(input().strip())
    result = timeInWords(h, m)
    print(result)
