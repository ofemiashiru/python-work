#rockpaperscissors

import random

choices = ("rock","paper","scissors")

yourScore = 0
cpuScore = 0

def checkWinner(you, cpu):
    #You chose Rock
    if you == choices[0] and cpu == choices[0]:
        result = "Draw"
        return result
    elif you == choices[0] and cpu == choices[1]:
        result = "Computer Wins"
        return result 
    elif you == choices[0] and cpu == choices[2]:
        result = "You Win"
        return result

    #You chose Paper
    elif you == choices[1] and cpu == choices[0]:
        result = "You Win"
        return result
    elif you == choices[1] and cpu == choices[1]:
        result = "Draw"
        return result
    elif you == choices[1] and cpu == choices[2]:
        result = "Computer Wins"
        return result 

    #You chose Scissors
    elif you == choices[2] and cpu == choices[0]:
        result = "Computer Wins"
        return result 
    elif you == choices[2] and cpu == choices[1]:
        result = "You Win"
        return result
    elif you == choices[2] and cpu == choices[2]:
        result = "Draw"
        return result


count = 1
while count < 4:
    print("\nRound", count)
    userChoice = input("choose rock, paper or scissors? ").lower()
    cpuChoice = random.choice(choices)
    
    if userChoice != choices[0] and userChoice != choices[1] and userChoice != choices[2]:
        print("Invalid entry... try again")
    
    elif userChoice == choices[0]:
        print("You chose", userChoice)
        print("Computer chose", cpuChoice)
        if checkWinner(userChoice,cpuChoice) == "You Win":
            yourScore +=1
            print("\n" + checkWinner(userChoice,cpuChoice))
        elif checkWinner(userChoice,cpuChoice) == "Computer Wins":
            print("\n" + checkWinner(userChoice,cpuChoice))
            cpuScore +=1
        elif checkWinner(userChoice,cpuChoice) == "Draw":
            print("\n" + checkWinner(userChoice,cpuChoice))
        count += 1
    elif userChoice == choices[1]:
        print("You chose", userChoice)
        print("Computer chose", cpuChoice)
        if checkWinner(userChoice,cpuChoice) == "You Win":
            yourScore +=1
            print("\n" + checkWinner(userChoice,cpuChoice))
        elif checkWinner(userChoice,cpuChoice) == "Computer Wins":
            print("\n" + checkWinner(userChoice,cpuChoice))
            cpuScore +=1
        elif checkWinner(userChoice,cpuChoice) == "Draw":
            print("\n" + checkWinner(userChoice,cpuChoice))
        count += 1
    elif userChoice == choices[2]:
        print("You chose", userChoice)
        print("Computer chose", cpuChoice)
        if checkWinner(userChoice,cpuChoice) == "You Win":
            yourScore +=1
            print("\n" + checkWinner(userChoice,cpuChoice))
        elif checkWinner(userChoice,cpuChoice) == "Computer Wins":
            print("\n" + checkWinner(userChoice,cpuChoice))
            cpuScore +=1
        elif checkWinner(userChoice,cpuChoice) == "Draw":
            print("\n" + checkWinner(userChoice,cpuChoice))
        count += 1
        
    

print("-----------------------------------------")

print("You scored:", yourScore)

print("Computer scored:", cpuScore)

if yourScore > cpuScore:
    print("You beat the computer")
elif yourScore < cpuScore:
    print("The Computer beat you")
elif yourScore == cpuScore:
    print("You scored the same! Its a draw!")







