import random
import sys


def guess(user_number):
    computer_number=random.randint(1, 10)

    attempt = 'yes'

    while attempt == 'yes' :

        if int(computer_number) == int(user_number):
            print("you got the right number!")
        elif int(computer_number) != int(user_number):
            print("the number you introduced does not match with the computer number")
        
        print(f"computer number: {computer_number}")
        
        attempt = input(f"would you like to play again? (yes or no): ")

        while attempt != 'yes' and attempt !='no':
            attempt = input(f"please, enter a 'yes' or 'no': ")

        
        if attempt == "yes":
            user_number = int(input("try to guess the number from 1 to 10: "))
            computer_number = random.randint(1, 10)
        elif attempt == "no":
            print("have a great day!")
    


user_number = int(input("try to guess the number from 1 to 10: "))

guess(user_number)



 

    

    
    




