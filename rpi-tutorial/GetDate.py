# GetDate.py

from RTC_DS1307 import RTC

rtc = RTC()
print "Current date:", rtc.getDateStr()
