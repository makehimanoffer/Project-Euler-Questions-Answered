import random

guessesTaken=0

print('Hello! What is your name?')
myName=input()

number= random.randint(1,20)
print('Well' + myName + ', I am thinking of a number between 1 and 20')
while guessesTaken<6:
    print('take a guess')
    guess=input()
    guess=int(guess)
    guessesTaken= guessesTaken + 1

    if guess<number:
        print('your guess is too low')

    if guess>number:
        print('your guess is too high')

    if guess==number:
        print('your guess is correct')
        break

if guess == number:
    guessesTaken= str(guessesTaken)
    print('gg ' + myName)

if guess!= number:
    number= str(number)
    print("nope chucktesta")
    
    
