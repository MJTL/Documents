
total=0
sum=0

emailmax= ''
numbermax= 0

senders = {}


fname = raw_input('Enter file name: ')
if len(fname) == 0:
    fname = 'mbox-short.txt'




fhand = open(fname ,'r')
for line in fhand:
    if line.startswith('From') and not line.startswith('From:'):
        line.split()
        items = line.split()
        email = items[1]

        # senders[email] = senders.get(email, 0) + 1 #Also a valid way to add keys to a dict
        # senders[email] = 1 if email not in senders else senders[email] + 1 #Also a valid way ternary operator
        if email not in senders:
            senders[email] = 1
        else:
            senders[email] += 1







emails = senders.keys()

for email in emails:
    number= senders [email]
    if number > numbermax:
        numbermax = number
        emailmax = email

print emailmax, numbermax