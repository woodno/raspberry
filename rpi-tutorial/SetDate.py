# SetDate.py

from RTC_DS1307 import RTC

rtc = RTC()
rtc.setDate(seconds = 0, minutes = 8, hours = 18, dow = 2,
            day = 28, month = 6, year = 16)
print "Date set to:", rtc.getDateStr()
