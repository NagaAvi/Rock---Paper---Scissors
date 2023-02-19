import random

options = ["1", "2", "3"]

computer_choice = random.choice(options)
print("Enter Your Choice")
print("Enter the number (ex: if you pick rock input 1)")
print(" ----------------------------------")
print("| Rock(1) | Paper(2) | Scissors(3) |")
print(" ----------------------------------")
user_choice = input()

if user_choice == computer_choice:
    print("It's a tie!\n")
elif user_choice == "1":
    if computer_choice == "2":
        print("Computer Wins!\n")
    else:
        print("You Win!\n")
elif user_choice == "2":
    if computer_choice == "3":
        print("Computer Wins!\n")
    else:
        print("you win!\n")
elif user_choice == "3":
    if computer_choice == "1":
        print("Computer Wins!\n")
    else:
        print("You Win!\n")
else:
    print("We're sorry for inconvinence. There is some error! Please try again!\n")
