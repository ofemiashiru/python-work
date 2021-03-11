#roulette game created and developed by Oluwafemi Ashiru

import random

wallet = float(input("Deposit cash? "))

print("\nWallet = £"+ str(wallet))

while wallet > 0:
    typeOfBet = input("\nType of bet: \"odds\", \"evens\" or \"number\"? Type quit to end betting ") 
    if typeOfBet !="number" and typeOfBet !="odds" and typeOfBet !="evens"  and typeOfBet !="quit": #validation
        print("Invalid input")
    else:
        if typeOfBet == "number":
            userBet = float(input("How much do you want to bet? "))
            userNumber = int(input("What number will it be? "))
            wheelNumber = random.randrange(1,37)
            print("The wheel landed on number:", wheelNumber)
            if userNumber == wheelNumber:
                winnings = userBet * 35
                print("You won £" + str(winnings))
                wallet = (wallet - userBet) + winnings
                print("You now have £" + str(wallet))
            else:
                print("You lost £" + str(userBet))
                wallet = wallet - userBet
                print("You have £"+ str(wallet), "in your wallet")

        if typeOfBet == "odds":
            userBet = float(input("How much do you want to bet? "))
            wheelNumber = random.randrange(1,37)
            print("The wheel landed on number:", wheelNumber)
            if wheelNumber % 2 != 0:
                winnings = userBet 
                print("You bet right and you won £" + str(winnings))
                totalWinnings = userBet + winnings
                wallet = (wallet - userBet) + totalWinnings
                print("You now have £" + str(wallet))
            else:
                print("You lost £" + str(userBet))
                wallet = wallet - userBet
                print("You have £"+ str(wallet), "in your wallet")

        if typeOfBet == "evens":
            userBet = float(input("How much do you want to bet? "))
            wheelNumber = random.randrange(1,37)
            print("The wheel landed on number:", wheelNumber)
            if wheelNumber % 2 == 0:
                winnings = userBet 
                print("You bet right and you won £" + str(winnings))
                totalWinnings = userBet + winnings
                wallet = (wallet - userBet) + totalWinnings
                print("You now have £" + str(wallet))
            else:
                print("You lost £" + str(userBet))
                wallet = wallet - userBet
                print("You have £"+ str(wallet), "in your wallet")

        if typeOfBet == "quit":
            print("Goodbye!")
            print("Thank you for playing.")
            break

print("\nWallet = £"+ str(wallet))

if wallet < 0:
    print("\nYou are in debt to the casino.")
elif wallet > 0:
    print("\nEnjoy your winnings.")
elif wallet == 0:
    print("\nYou have no more money left, please deposit more cash")




