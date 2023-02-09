import random

def guess (name, ran, count):

    while count < 21:
        print("Take a guess.")
        num = int(input())
        count += 1
        if num == ran:
            print("Good job, " +name+ "! You guessed my number in" ,count, "guesses!")
            break
            
        elif num > ran:
            print("Your guess is too high.")
                 
        elif num < ran:
            print("Your guess is too low.")
            
            
print("Hello! What is your name?")
name = input()
print("Well, " +name+ ", I am thinking of number between 1 and 20")
ran = random.randrange(1, 21)
count = 0
guess(name, ran, count)
