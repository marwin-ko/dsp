###################################### Q5 ######################################
from datetime import date

def num_days(start,stop):
    if '-' in start and stop:
        start = start.split('-')
        stop  = stop.split('-')
        if start[1].isalpha() and stop[1].isalpha():
            start[1] = d[start[1]]
            stop[1]  = d[stop[1]]
            start = [start[1],start[0],start[2]]
            stop  = [stop[1],stop[0],stop[2]]
    elif start.isdigit() and stop.isdigit() :
        start = [start[0:2],start[2:4],start[4:]]
        stop  = [stop[0:2],stop[2:4],stop[4:]]
    start = map(int,start)
    stop  = map(int,stop)
    d0 = date(start[2],start[0],start[1])
    d1 = date(stop[2],stop[0],stop[1])
    delta = d1-d0
    return delta.days

####a)
date_start = '01-02-2013'
date_stop = '07-28-2015'
print num_days(date_start,date_stop)    #ANSWER: 937 days

####b)
date_start = '12312013'
date_stop = '05282015'
print num_days(date_start,date_stop)    #ANSWER: 513 days

####c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
month = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
num   = range(1,13)
d = dict(zip(month,num))
print num_days(date_start,date_stop)    #ANSWER: 7850 days
