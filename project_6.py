'''
In this article, I’ll walk you through how to make a rock, paper, and scissors game with Python.
In the rock, paper and scissors game our goal is to create a command-line game
where a user has the option to choose between rock, paper and scissors and 
if the user wins the score is added, and at the end when the user finishes the game, the score is shown to the user.
'''

import random 

choices = ["Rock", "Paper", "Scissors"]
user_point = 0
computer_point = 0

while True:
    computer_choice = random.choice(choices)
    user_choice = str(input("Rock, Paper or  Scissors?\n")).capitalize() #capitalize() in Python is used to convert the first character of a string to uppercase and the remaining characters to lowercase.
    
    if(user_choice == "Stop"):
        print("Final Scores\n")
        print("User Score {}".format(user_point))
        print("Computer Score {}".format(computer_point))
        break
    
    
    elif(computer_choice == user_choice):
        print("tie!")
    
    
    elif(computer_choice == "Rock"):
        if(user_choice == "Paper"):
            print("user win!")
            user_point +=1
        else: 
            print("computer win")
            computer_point +=1
    
    
    elif(computer_choice == "Paper"):
        if(user_choice == "Scissors"):
            print("user win!")
            user_point +=1
        else: 
            print("computer win")
            computer_point +=1
    

    elif(computer_choice == "Scissors"):
        if(user_choice == "Rock"):
            print("user win!")
            user_point +=1
        else: 
            print("computer win")
            computer_point +=1
        
        
        


    
    