total = 0
sum = 0
max = 0

fname = raw_input('Enter file name: ')
if len(fname) == 0:
    fname = 'mbox-short.txt'
fhand = open(fname, 'r')
for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        total = total + 1   # equivalent to total += 1
        raw = line[20:]
        number = float(raw)

        if number > max:
            max=number
            print 's',max

        sum = sum + number  # equivalent to sum += number

        print line
        print sum

print 'M', max

print total
result = 0
result = sum/total

print 'Average spam confidence', result
