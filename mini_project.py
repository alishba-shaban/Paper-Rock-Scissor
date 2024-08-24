import random
item_list = ["rock","paper","scissor"]
comp_choice = random.choice(item_list)
print("Welcome Rock,Paper,Scissor Game")
while True:
    user_choice  = input("Enter your move = Rock,Paper,Scissor: ")
    print(f"user choice = {user_choice}")
    print(f"Computer choice = {comp_choice}")
    if user_choice==comp_choice:
        print("Both chooses same!!Math tie")

    if user_choice=="rock" and comp_choice =="paper":
        print("paper covers rock, computer win")
    if user_choice=="rock" and comp_choice =="scissor":
        print("rock break scissor, you win")
    if user_choice=="paper" and comp_choice =="scissor":
        print("scissor cuts paper,computer win")
    if user_choice=="paper" and comp_choice =="rock":
        print("paper covers rock, you win")
    if user_choice=="scissor" and comp_choice =="rock":
        print("rock break scissor, computer win")
    if user_choice=="scissor" and comp_choice =="paper":
        print("scissor cuts paper,you win")

    user  = input("Press E to end this game and C to continue!!")
    if  user =="e":
        print("Thank you for using this game")
        break
    elif user == "c":
        continue