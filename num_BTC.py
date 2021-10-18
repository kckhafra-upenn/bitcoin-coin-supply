import math

def num_BTC(b):
    c = float(50)
    c = b*c
    if(b>210000):
        results=0
        quotient = b/210000
        remainder = b%210000
        multiplier = float(50)
        while(quotient>0):
            results = (210000*multiplier) + results
            multiplier=multiplier/2
            quotient=quotient-1
        
        total=results+(remainder * multiplier)
    print("C: ",total)
    return total

num_BTC(813574)
