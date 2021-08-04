# -*- coding: utf-8 -*-

#Converting timestamps of “yyyy-MM-dd'T'HH:mm:ss.SSSZ” format in Python

from datetime import timedelta,datetime

str_time = "2021-05-27T05:49:24.257+02:00"

#replace the last ':' with an empty string, as python UTC offset format is +HHMM
 
str_time = str_time[::-1].replace(':','',1)[::-1]

try:
    offset = int(str_time[-5:])
except:
    print("Error")

delta = timedelta(hours = offset / 100)
  
time = datetime.strptime(str_time[:-5], "%Y-%m-%dT%H:%M:%S.%f")

time -= delta                #reduce the delta from this time object

print(time)

#extracting HH:MM from datetime column

#convert from string to datetime

df['date_col'] = pd.to_datetime(df['date_col']) 

#to get date only

print(df['date_col'].dt.date)

#to get time:

    print(df['date_col'].dt.time)
    
    #to get hour and minute
    
print(df['date_col'].dt.strftime('%H:%M'))

#Or

date=[]

for str_date in df['date_col']:
    
    date.append(datetime.datetime.strptime(str_date, '%Y%m%d'))