import random

print("Number guessing game")
print("Guess a random number between 1 & 9")
number = random.randint(1,9)
chances = 0
#guess = input("Enter your guess ")

while chances < 5 :
    
    guess = int(input("Enter your guess "))
    if guess == number :
        print("CONGRATS ! YOU WON !")
        break
    elif guess > number : 
        print("Your guess was too high !")
        print("Guess a number lower than " ,guess)
    elif guess < number:
        print("Your guess was too low !")
        print("Guess a number higher than " , guess)
        chances += 1
     

if chances > 5:
    print("YOU LOSE!!! The number is", number)