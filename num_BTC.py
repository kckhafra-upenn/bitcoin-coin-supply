import math

def num_BTC(b):
    fl = float(50)
    c=0
    results=0
    quotient = b/210000
    remainder = b%210000
    multiplier = float(50)
    if(b>210000):    
        while(quotient>0):
            results = (210000*multiplier) + results
            multiplier=multiplier/2
            quotient=quotient-1
        r = remainder * multiplier
        c=results+r
    else:
        c = b*fl
    return c
# print("NUM: ",num_BTC(813574))