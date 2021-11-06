import random
choices = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

random_number = random.randint(0,2)
computer_selection = choices[random_number]


user_selection = int(input('What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors\n'))
if user_selection == 0:
    print("You have selected: \n")
    print(choices[0])
    print("The computer selected: \n")
    print(computer_selection)
    if computer_selection == choices[0]:
        print('TIE')
    elif computer_selection == choices[1]:
        print('YOU LOSE')
    else:
        print('YOU WIN')
elif user_selection == 1:
    print("You have selected: \n")
    print(choices[1])
    print("The computer selected: \n")
    print(computer_selection)
    if computer_selection == choices[1]:
        print('TIE')
    elif computer_selection == choices[2]:
        print('YOU LOSE')
    else:
        print('YOU WIN')
elif user_selection == 2:
    print("You have selected: \n")
    print(choices[2])
    print("The computer selected: \n")
    print(computer_selection)
    if computer_selection == choices[2]:
        print('TIE')
    elif computer_selection == choices[0]:
        print('YOU LOSE')
    else: 
        print('YOU WIN')
else:
    print('ERROR! PLEASE TRY AGAIN!')