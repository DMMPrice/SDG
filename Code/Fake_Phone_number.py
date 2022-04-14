import random

# Generation empty list for phone number
phone_no = []

# the first number should be in the range
# the other 9 numbers can be in the range 0 to 9
phone_no.append(random.randint(6, 9))

# the for loop is used to append the others 9 numbers
# the others 9 numbers can be in the range of 0 to 9
for i in range(1, 10):
    phone_no.append(random.randint(0, 9))

# printing the number
for i in phone_no:
    print(i, end='')
