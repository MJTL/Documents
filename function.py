def square_diff(a, b):
    result = a**2 - b**2
    if result > 100:
        print "Bigger than 100"
    else:
        print "Less than 100"


for i in range(10, 100):
    square_diff(i, 15)
    for j in range(25, 30):
        square_diff(i, j)