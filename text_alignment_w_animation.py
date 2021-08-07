#Replace all ______ with rjust, ljust or center.
import time

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    for char in ((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1)):
        print(char, end='', flush=True)
        time.sleep(0.2)
    print()

#Top Pillars
for i in range(thickness+1):
    for char in (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6):
        print(char, end='', flush=True)
        time.sleep(0.2)
    print()

#Middle Belt
for i in range((thickness+1)//2):
    for char in (c*thickness*5).center(thickness*6):
        print(char, end='', flush=True)
        time.sleep(0.2)
    print()

#Bottom Pillars
for i in range(thickness+1):
    for char in (c*thickness).center(thickness*2)+(c*thickness).center(thickness*6):
        print(char, end='', flush=True)
        time.sleep(0.2)
    print()

#Bottom Cone
for i in range(thickness):
    for char in ((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6):
        print(char, end='', flush=True)
        time.sleep(0.2)
    print()