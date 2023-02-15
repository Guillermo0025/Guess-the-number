import random as rnd

#now the computer will try to guess the number

def computer_guess(x):
    upper_limit = x
    lower_limit = 0
    guess = 'x'

    while guess != 'y':
        computer_number = rnd.randint(lower_limit, upper_limit)

        print("PLEASE THINK OF A NUMBER FROM 1 TO 1000")
        guess = input(f"is your number: {computer_number}? ('y' is yes, '+' is 'my number is higher', y '-' is 'my number is lower'): ").lower()

        if guess == '+':
            lower_limit = computer_number + 1
        elif guess == '-':
            upper_limit = computer_number-1
        elif guess == 'y':
            print("I WON!")


  
x=1000
computer_guess(x)