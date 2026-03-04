import asyncio
import time

async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)
##Example 1 The await causes the function to be called and await till after it finishes
##  Therefore expected to take 4 seconds


# async def main():
#     print(f"started at {time.strftime('%X')}")
# 
#     await say_after(2, 'hello')
#     await say_after(2, 'world')
# 
#     print(f"finished at {time.strftime('%X')}")


#Example 2  Create Task allows functions to run concurrently
#Because of the await order task1 is always finished before task 2
# Note it runs in two seconds now
# async def main():
#     task1 = asyncio.create_task(
#         say_after(2, 'hello'))
# 
#     task2 = asyncio.create_task(
#         say_after(2, 'world'))
# 
#     print(f"started at {time.strftime('%X')}")
# 
#     # Wait until both tasks are completed (should take
#     # around 2 seconds.)
#     await task1
#     await task2
# 
#     print(f"finished at {time.strftime('%X')}")


#Example 3 This example shows that task1 and task2
#are never called because an asyncio await has to be called to allow concurrent
#tasks to be called
# async def main():
#     task1 = asyncio.create_task(
#         say_after(2, 'hello'))
# 
#     task2 = asyncio.create_task(
#         say_after(2, 'world'))
# 
#     print(f"started at {time.strftime('%X')}")
# 
#     time.sleep(1)
#     
#     print(f"finished at {time.strftime('%X')}")

#Example 4 This example does allow task1 and task2 to be called
#In this case you can't be sure what task finishes first
# async def main():
#     task1 = asyncio.create_task(
#         say_after(2, 'hello'))
# 
#     task2 = asyncio.create_task(
#         say_after(2, 'world'))
# 
#     print(f"started at {time.strftime('%X')}")
# 
#     await asyncio.sleep(4)
# 
#     
#     print(f"finished at {time.strftime('%X')}")
    
#Example 5 This example does allow task1 and task2 to be called
#But because control is allowed to return to the main program
#before task1 and task2 are complete they never finish.

# async def main():
#     task1 = asyncio.create_task(
#         say_after(2, 'hello'))
# 
#     task2 = asyncio.create_task(
#         say_after(2, 'world'))
# 
#     print(f"started at {time.strftime('%X')}")
# 
#     await asyncio.sleep(1)
# 
#     
#     print(f"finished at {time.strftime('%X')}")
    
#Example 6 This example allows task1 and task2 to complete
#because they are given a series of 1 second slices of time to work
#Notice the printing of the finish time never occurs as the program is always waiting.
async def main():
    task1 = asyncio.create_task(
        say_after(2, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")
    while True:
        await asyncio.sleep(1)

    
    print(f"finished at {time.strftime('%X')}")  
asyncio.run(main())
