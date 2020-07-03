# Learned at Automate boring Stuff!
# automatetheboringstuff.com

# Import random module
import random

# store a random number between 1 and 20
secretNo = random.randint(1,20)
print('Guess a number between 1 and 20.')

# loop, where the user has 4 chanes to input the correct number
for YourGuess in range(1,5):
    print('Guess please.')
    guess = int(input())
# feedback if the input() number is too low
    if guess < secretNo:
        print('Haha, too low.')
# feedback if the input() number is high
    elif guess > secretNo:
        print('Haha, too high.')
    else:
        break  # if guess is correct, break out of the loop
if guess == secretNo:
    print('Noooice! Correct, my number was ' + str(secretNo) + '!')
else:
    print('Sorry, mate. My number was ' + str(secretNo)  + '.')