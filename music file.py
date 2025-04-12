print("hello new world!")
from pysine import sine
import time
sine(frequency = 440.0, duration = 1.0)
c = 260
csharp = 275
d = 292
dsharp = 309
e = 328
f = 347
fsharp = 368
g = 390
gsharp = 413
a = 437
asharp = 463
b = 491
chigher = 520

def YouNeedtoCalmDown():
    #start of 1st line
    sine(frequency=d, duration=0.3)
    time.sleep(0.1)
    sine(frequency=d, duration=0.25)
    time.sleep(0.1)
    sine(frequency=d, duration=0.25)
    time.sleep(0.1)
    sine(frequency=d, duration=0.3)
    time.sleep(0.1)
    sine(frequency=fsharp, duration=0.5)
    time.sleep(0.1)
    sine(frequency=d, duration=0.3)
    time.sleep(0.1)
    sine(frequency=d, duration=0.25)
    time.sleep(0.1)
    sine(frequency=d, duration=0.25)
    time.sleep(0.1)
    sine(frequency=d, duration=0.25)
    #end of 1st line
    time.sleep(0.1)
    #start of 2nd line
    sine(frequency=a/2, duration=0.35)
    time.sleep(0.1)
    sine(frequency=d, duration=0.25)
    time.sleep(0.05)
    sine(frequency=d, duration=0.25)
    time.sleep(0.1)
    sine(frequency=d, duration=0.25)
    time.sleep(0.1)
    sine(frequency=d, duration=0.25)
    time.sleep(0.1)
    sine(frequency=fsharp, duration=0.5)
    time.sleep(0.1)
    sine(frequency=d, duration=0.25)
    time.sleep(0.1)
    sine(frequency=d, duration=0.25)
    time.sleep(0.1)
    sine(frequency=d, duration=0.25)
    time.sleep(0.1)
    sine(frequency=d, duration=0.25)
    time.sleep(0.1)
    sine(frequency=d, duration=0.3)
    #end of 2nd line
    time.sleep(0.1)
    #start of 3rd line
    sine(frequency=d, duration=0.3)
YouNeedtoCalmDown()    
