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
count = 0

while guess!= secret:
    count+=1
    guess = input(f"Enter your guess between 1 and {num} : ")
    if guess.isdigit():
        guess=int(guess)

    if guess == secret:
        print("You Got It!")  
    elif guess <secret:
        print("You need to guess higher.Try Again")      
    else :
        print("You need to guess lower. Try Again")
       
        
print(f"It took you {count} guesses.")
print("Thanks For Playing!")
