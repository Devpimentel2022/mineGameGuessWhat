import sys
import random

secretNumber = random.randint(1,20)
print("I'm thinking of a number from 1 to 20.")
print()

for attempts in range(1,7):
    print("Try to guess the number:")
    print()
    guess = int(input())
    if guess < secretNumber:
        print()
        print("Your attempt was too low.")
        print()
    elif guess > secretNumber:
        print()
        print("Your attempt was too high.")
        print()
    else:
        break

if guess == secretNumber:
    print()
    print("Well done!, You got the number right in "+ str(attempts) + " attempts")
    print()
    exit = input("Type 'exit' to exit: ")
    exit = exit.lower()
    if exit == "exit":
        sys.exit()
    else:
        while True:
            exit = input("Type 'exit' to exit:")
            exit = exit.lower()
            if exit == 'exit':
                 sys.exit()        
    
else:
    print()
    print("What a pity! You couldn't get the number right which was: " + str(secretNumber))
    print()
    exit = input("Type 'exit' to exit: ")
    exit = exit.lower()
    if exit == "exit":
        sys.exit()
    else:
        while True:
            exit = input("Type 'exit' to exit: ")
            exit = exit.lower()
            if exit == 'exit':
                 sys.exit()