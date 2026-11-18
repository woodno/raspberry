import re
timeString = "10:23:09.00"
#timeSplit = timeString.split(":")
timeSplit = re.split(r"[:.]", timeString)  
print ("Hours = ", timeSplit[0])
print ("Minutes = " , timeSplit[1])
print ("Secs = ", timeSplit[2])