#micropython time examples

import time
#This looks like it should work to last for a duration
# but it does not because the time.ticks_ms() returns a max and then cycles to zero.
i = time.ticks_ms()

j  = i + 10* 1 * 1000

print (i)
print (j)

while time.ticks_ms() < j:
    print (time.ticks_ms())
    time.sleep(1)
   
print ("done")
#This is the correct method for working out if a duration has passed.
#But does not work if too much time passes
#See https://docs.micropython.org/en/latest/library/time.html
# Calculate deadline for operation and test for it
deadline = time.ticks_add(time.ticks_ms(), 200)
start = time.ticks_ms()
r = 1
while time.ticks_diff(deadline, time.ticks_ms()) > 0:
    r=r+1
    #This sets an upper limit to the wait to handle problem related in https://docs.micropython.org/en/latest/library/time.html
    max_wait_time = 1000000
    if time.ticks_diff(time.ticks_ms(), start) > max_wait_time:
        raise Exception
print (r)

# Find out TICKS_MAX used by this port
print(time.ticks_add(0, -1))