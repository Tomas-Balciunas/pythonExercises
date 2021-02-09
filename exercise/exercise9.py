import random

counter = 0

while True:
    a = random.randint(1, 9)
    userInput = int(input("guess a number from 1 to 9 or exit: "))
    if userInput == "exit":
        print("bye")
        break
    else:
        if userInput == a:
            print("you guessed correctly")
        elif userInput > a:
            print("your guess was too high")
        elif userInput < a:
            print("your guess was too low")