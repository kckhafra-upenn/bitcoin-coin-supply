import math

def num_BTC(b):
    c = float(50)
    if(b>210000):
        results=0
        quotient = int(b/210000)
        remainder = b%210000
        multiplier = float(50)
        while(quotient>0):
            results = (210000*multiplier) + results
            multiplier=multiplier/2
            quotient=quotient-1
        r = remainder * multiplier
        c=results+r
    else:
        c = b*c
    return c

# print("NUM: ",num_BTC(813574))
