
# *** Find the largest Prime Number after 1 hour ***

#import the time functions
from datetime import date, datetime, timedelta
from time import sleep


#create the Strat and Finish variables
start_time = datetime.now()
#end_time = start_time + timedelta(hours=1)
end_time = start_time + timedelta(seconds=10)


#Show Starting Time and the Finishing Time and Get Ready To Start
print("Start Time Is: ",start_time)
sleep(1)
print("Start Time Is: ",end_time)
sleep (2)
print()
print("You Ready.....",end = " ")
sleep(1)
print("Here We Go...",end = " ")
sleep(1)
print("See You In 1 Hour.... It's going to be a big number !")
sleep (3)


#Calculate and show the PRIME NUMBERS for the time between the Start_Time and the End_Time (1 Hour) 
num = 2
while(datetime.now() < end_time):        
    for i in range(2,num):
 
        if num%i == 0:
            break         
    else:
        print(num)
    num = num+1
    
    
    