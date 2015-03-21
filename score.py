rawstr=raw_input('Enter a score between 0.0 and 1.0: ')
ival=float(rawstr)

if ival>1 or ival <0:
        print 'out of score'
elif ival >=0.9:
        print'A'
elif ival >=0.8:
        print'B'
elif ival >=0.7:
        print'C'
elif ival >=0.6:
        print'D'
elif ival <0.6:
        print 'F'
else:
        print 'out of range'


