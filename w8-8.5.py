
total = 0

fname = raw_input('Enter file name: ')
if len(fname) == 0:
    fname = 'mbox-short.txt'
fhand = open(fname, 'r')
for line in fhand:
    if line.startswith('From') and not line.startswith('From:'):
        line = line.rstrip()
        words = line.split()
        total+=1
        print words[1]
print 'There were',total,'lines in the file with From as the first word'




