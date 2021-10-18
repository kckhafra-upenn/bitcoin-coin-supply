import math

def num_BTC(b):
    c = float(50)
    c = b*c
    if(b>210000):
        d = b/210000
        e=0
        while(d>0):
            e = (210000*50)/2 +e
            d=d-1
        print("HAlves: ",e)
        c = e + ((b%210000)*50)
    print(c)
    return c

num_BTC(648559)
