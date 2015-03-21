largest= None
smallest = None


while True:
    user_input = raw_input('Enter an integer number: ')

    if user_input == 'Done':
        break
    try:
        numeric_value = int(user_input)
    except:
        print 'Invalid input'
    else:

        if largest is None or numeric_value > largest:
            largest= numeric_value

        if smallest is None or numeric_value < smallest:
            smallest = numeric_value

print 'Maximum is', largest
print 'Minimum is', smallest



