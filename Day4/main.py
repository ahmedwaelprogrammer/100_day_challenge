import random;
choices= ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    """ , 
    """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    """ ,
    """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """]

print("######################################################")
print("################  Stone Paper scissors ###############")
print("######################################################")
print("______________________________________________________")
user_choice = int(input("Enter 0 for stone and 1 for paper and 2 for scissors: "))
computer_choice = random.randint(0,2); 
print(f"You chosed : {choices[user_choice]}")
print(f"Computer chosed : {choices[computer_choice]}")
## First Case
if user_choice == 0 and computer_choice == 0 :
    print("Draw!")
elif user_choice == 0 and computer_choice == 1 :
    print("Coputer Wins!")
elif user_choice == 0 and computer_choice == 2 :
    print("You Wins!")
## Second Case
elif user_choice == 1 and computer_choice == 0 :
    print("You Wins!")
elif user_choice == 1 and computer_choice == 1 :
    print("Draw!")
elif user_choice == 1 and computer_choice == 2 :
    print("Coputer Wins!")
    ## Third Case
elif user_choice == 2 and computer_choice == 0 :
    print("You Wins!")
elif user_choice == 2 and computer_choice == 1 :
    print("Coputer Wins!")
elif user_choice == 2 and computer_choice == 2 :
    print("Draw!")
else :
    print("Something went wrong please check your input!!")