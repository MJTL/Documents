def computepay(h,r):


        if h <= 40:
                p=r*h
        else:
                p=r*40+(r*1.5*(h-40))

        
        return p

inp=raw_input('Enter hours: ')
hours=float(inp)
inp=raw_input('Enter rate: ')
rate=float(inp)

pay = computepay(hours, rate)
print pay




