import shutil
from datetime import timedelta
import time
import datetime

#shutil.copyfile(r'C:\Users\invad\Desktop\Figure_1.png', r'C:\Users\invad\Desktop\Figure_1_10')
#shutil.copystat(r'C:\Users\invad\Desktop\Figure_1.png', r'C:\Users\invad\Desktop\Figure_1_10')

#a = print(list(shutil.disk_usage('C:')))

#a = datetime.datetime.today().hour
#now = datetime.datetime.now()
#b = now.strftime('%b %d %W %p %w %A')
#c = time.gmtime()
#print(a)
#print(b)
#print(c)


#day1 = timedelta(seconds= -1).seconds
#now = datetime.datetime.date(datetime.datetime.now())
#year_2000 = datetime.date(2009,6,30)
#delt1 = now - year_2000
#print(delt1)


#lab661----photo
now = time.time()
today1 = datetime.datetime.now()

today2 = today1.strftime('%c')





