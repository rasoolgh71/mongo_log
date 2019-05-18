
import os
import random
import uuid
import datetime
from unidecode import unidecode


def jalali_to_gregorian(jy,jm,jd):
    if(jy>979):
        gy=1600
        jy-=979
    else:
        gy=621
    if(jm<7):
        days=(jm-1)*31
    else:
        days=((jm-7)*30)+186
    days+=(365*jy) +((int(jy/33))*8) +(int(((jy%33)+3)/4)) +78 +jd
    gy+=400*(int(days/146097))
    days%=146097
    if(days > 36524):
        gy+=100*(int(--days/36524))
        days%=36524
        if(days >= 365):
            days+=1
    gy+=4*(int(days/1461))
    days%=1461
    if(days > 365):
        gy+=int((days-1)/365)
        days=(days-1)%365
    gd=days+1
    if((gy%4==0 and gy%100!=0) or (gy%400==0)):
        kab=29
    else:
        kab=28
    sal_a=[0,31,kab,31,30,31,30,31,31,30,31,30,31]
    gm=0
    while(gm<13):
        v=sal_a[gm]
        if(gd <= v):
            break
        gd-=v
        gm+=1
    return [gy,gm,gd]


def change_date_to_english(value, mode=1):
    if mode == 3:
        y, m, d = value
        pdate = jalali_to_gregorian(int(y), int(m), int(d))
        date_time = datetime.datetime(pdate[0], pdate[1], pdate[2])
        return date_time
    if mode == 2:
        y, m, d = unidecode(value).split('/')
        pdate = jalali_to_gregorian(int(y), int(m), int(d))
        date_time = datetime.datetime(pdate[0], pdate[1], pdate[2])
        return date_time
    value = unidecode(value)
    stime, date = value.split(' ')
    stime = unidecode(stime)
    year, month, day = date.split('/')
    date = jalali_to_gregorian(int(year), int(month), int(day))
    string_date = "{y} {m} {d} ".format(y=date[0], m=date[1], d=date[2])
    string_date_time = string_date + stime
    date_time = datetime.datetime.strptime(string_date_time, "%Y %m %d %H:%M:%S")
    return date_time



