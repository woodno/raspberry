import machine

rtc = machine.RTC()
# Format: (year, month, day, weekday, hours, minutes, seconds, subseconds)
# Weekday is usually 0-6 (Monday = 0)
#You can safely pass 0 to all dates for the weekday as the RTC
#Does not validate the weekday against the date.
rtc.datetime((2026, 11, 13, 3, 19, 30, 0, 0))

# Verify current time
print(rtc.datetime())