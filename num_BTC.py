import math

def num_BTC(b):
    c = float(50)
    c = b*c
    while b>210000:
        b=b/210000
        c = (c/2)
    return c


