import random

print("Welcome, let's play!")

number = input("Enter a number: ")

if number.isdigit():       # ----> checks if number is integer type
    number = int(number)
    if number <=0:          #----> checks if number is zero or less
        print("enter a number greater than zero.")

else:
    print("please enter a integer type not others")

random_number = random.randrange(number)

guesses = 0 # stores the number of guesses

while True:
    guesses += 1

    guess_number = input("guess the number: ")

    if guess_number.isdigit():
        guess_number = int(guess_number)
    else:
        print("please enter a number")
        continue    # goes back to while

    if guess_number == random_number:
        print("yeah, you got it!")
        break      # breaks out of while

    elif guess_number > random_number:
        print("you were above the range")
        
    else:
        print("you were below the range")

print("You got it in", guesses, "guesses")
