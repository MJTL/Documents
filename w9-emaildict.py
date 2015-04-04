


senders={'Tom':3,'Alice':7,'Bob':5}

emailmax=''
numbermax=0

emails = senders.keys()

for email in emails:
    number= senders [email]
    if number > numbermax:
        numbermax = number
        emailmax = email

print emailmax, numbermax
