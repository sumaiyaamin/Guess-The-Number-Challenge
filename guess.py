print("\tGUESS THE NUMBER CHALLENGE\n")
import random

flag = True
while flag:
    num =input("Enter a number for an upper bound : ")
    if num.isdigit():
        print("Let's Play!")
        num = int(num)
        flag = False
    else:
        print("Invalid Input!")

secret = random.randint(1,num)
guess = None
count = 1

while guess!= secret:
    guess = input(f"Enter your guess between 1 and {num} : ")
    if guess.isdigit():
        guess=int(guess)

    if guess == secret:
        print("You Got It!")   
    else:
        print("Try Again!")
        count+=1

print(f"It took you {count} guesses.")
print("Thanks For Playing!")


