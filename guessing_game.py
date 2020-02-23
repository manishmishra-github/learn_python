import random

random_number = random.randint(1, 10)
yes = 'y'
print("Hey welcome to the game....\nI have picked my number..Guess it?")

while yes == 'y':
    guess = int(input("your guess:\n"))
    if guess == random_number:
        print("You won")
        yes = input("Want to play again: y/n\n")
        print(yes)
        continue
    elif guess < random_number:
        print("too low")
    else:
        print("too high")
