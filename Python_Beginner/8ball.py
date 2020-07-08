# magic 8ball, function practice (https://automatetheboringstuff.com/2e/chapter3/)

import random

def eightball(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My replay is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
r = random.randint(1,9)
fortune = eightball(r)
print(fortune)


# improved using lists:
messages = ['It is certain',
'It is decidedly so',
'Yes, definetly',
'Reply hazy, try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful']

print(messages[random.randint(0, len(messages)-1)]) # no fixed size of list, easily add more messages