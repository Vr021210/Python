light = 0
from pylab import time

space = '''
'''

while light == 0 or 1:
    time.sleep(0.3)
    if light == 0:
        print("light is off")
        time.sleep(0.3)
    elif light == 1:
        print("light is on")
        time.sleep(0.3)
    
    time.sleep(0.3)    
    lightINPUT = input("Light trigger? ")
    print(space)
    
    if lightINPUT == 'yes':
        if light == 0:
            light = 1
        elif light == 1:
            light = 0