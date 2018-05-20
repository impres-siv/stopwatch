 #! python3
#automate the boring stuff!
import time


print('Press ENTER to trigger a lap.  Press Ctrl-C to quit.')
input()                    # press Enter to begin
print('aaaannnnnnnddddd GO')
startTime = time.time()    
lastTime = startTime
lapNum = 1
try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)
        totalTime = round(time.time() - startTime, 2)
        print('Lap #%s: %s (%s)' % (lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time() # reset the last lap time
except :
# Handle the Ctrl-C exception to keep its error message from displaying.
    print('\nDone.')



