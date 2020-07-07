### Practice Project
# The Collatz Sequence
# From: Automate the Boring Stuff with Python CH 03


def collatz(number):        # function for Collatz sequence
    if number % 2 == 0:     # check if even number
        print(number // 2)
        return number // 2
    else:
        print(3 * number + 1)
        return 3 * number + 1

print('Please type in an integer.')
try:
    userNumber = int(input())
except ValueError:          # handle wrong user input
    print("Please don't enter a noninteger string")
    userNumber = int(input())

while userNumber != 1:      # loop until end of Collatz sequence (1) is reached
    userNumber = collatz(userNumber)