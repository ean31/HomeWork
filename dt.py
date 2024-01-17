#Напечатайте в консоль даты: вчера, сегодня, 30 дней назад

from datetime import datetime, date, timedelta
dt_now = datetime.now()
delta = timedelta(days=1)
delta2 = timedelta(days=30)
dt2 = dt_now - delta
dt3 = dt_now - delta2  
print(dt2)
print(dt_now)
print(dt3)


#Превратите строку "01/01/25 12:10:03.234567" в объект datetime

date_string = '01/01/2025'
date_dt = datetime.strptime(date_string, '%m/%d/%Y')
print(date_dt)


