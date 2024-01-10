def computepay():
    hrs = input("Enter Hours:")
    hsfn= float(hrs)
    value= input('Hours Value:')
    vlufn=float(value)
    
    if hsfn < 40:
        valorfinal= hsfn*vlufn
    else:
        valorfinal= 40 * vlufn + ((1.5 * vlufn) * (hsfn - 40))
    
    return valorfinal
    

p = computepay()
print("Pay", p)