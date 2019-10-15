from sense_hat import SenseHat
from time import sleep
hat = SenseHat()
hat.low_light = True
g = [0,255,0]     #green
r = [255,0,0]     #red
w = [255,255,255] #white
y = [255,255,0]   #yellow
o = [0,0,0]       #black
b = [0,0,255]     #blue
level1 = [r,r,r,r,r,r,r,r,
          r,r,r,o,o,o,r,r,
          r,o,o,o,b,o,r,r,
          r,o,o,b,o,b,o,r,
          r,r,r,o,b,o,o,r,
          r,r,r,o,o,o,r,r,
          r,r,r,r,r,r,r,r,
          r,r,r,r,r,r,r,r]
hat.clear()

def transition(speed):
    i=0
    while i<8:
        j=0
        while j<8:
            if(i%2!=0 and j%2!=0):
                hat.set_pixel(i,j,r)
            if(i%2!=0 and j%2!=1):
                hat.set_pixel(i,j,g)
            if(i%2!=1 and j%2!=1):
                hat.set_pixel(i,j,y)
            if(i%2!=1 and j%2!=0):
                hat.set_pixel(i,j,b)
            sleep(speed)
            hat.flip_h()
            j=j+1
        i=i+1
#endTransition           

def start(level):
    transition(0.02)
    if (level == level1):
        characterPostition = [5,1]
        hat.set_pixels(level1)
        
#endStart
def updatePosition():
    
    
    



