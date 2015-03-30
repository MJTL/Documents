
raw = []
cleaned = []

fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fname = 'romeo.txt'

fhand = open(fname, 'r')
for line in fhand:
    words = line.split()
    for word in words:
        if word not in cleaned:
            cleaned.append(word)





print sorted(cleaned)





