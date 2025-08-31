#The computer will pick a random number between 1 and 100 and then you have to guess the same number.
import random

def guess_num():
    random_no = random.randint(1, 100)
    guess_on = True
    attempts=0
    while guess_on:
        user_num = int(input("Enter a number: "))
        attempts += 1

        if user_num < 1 or user_num > 100:
            print("Enter a number between 1 and 100.")
            continue

        if user_num < random_no:
            print("Too low")

        elif user_num > random_no:
            print("Too high")

        else:
            print("You got it right!")
            print(f"You guessed it in {attempts} attempts!")
            guess_on = False

guess_num()
do_continue=input("Y to continue,  E to exit")
if do_continue == "Y":
    guess_num()
