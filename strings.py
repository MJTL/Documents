x='X-DSPAM-Confidence:  0.8475'
#print x
pos=x.find(':')

#print pos
num=float (x[pos+3:])
print num


