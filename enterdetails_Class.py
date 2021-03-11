# Code that enters details and then prints them to a textfile

class Customer():
    # creating customers attributes and initializing them
    def __init__(self):
        self.fname = ""
        self.sname = ""
        self.dob = ""
        self.spend = 0
    

    # creating a function to add customers details
    def enterDetails(self):
        self.fname = input("Enter your First Name? ")
        self.sname = input("Enter your surname? ")
        self.dob = input("Enter your date of birth? ")
        self.spend = int(input("Please enter how much you want to spend? "))

        # storing customers details inside a variable
        firstname = self.fname
        surname = self.sname
        dob = self.dob
        spend = self.spend


        # writing customers details to a text file
        userAcc = open("accounts.txt", "a")
        userAcc.write(firstname +" "+ surname +" "+ dob +" "+ str(spend))
        userAcc.write("\n")
        userAcc.close()
        
        #return firstname, surname, dob, spend
    
    # function that reads back details from text file
    def readCustomersDetails(self):
        userAcc = open("accounts.txt","r")
        output = userAcc.readlines()
        return output



# create 3 customers using the customer class and a while loop

while True:
    start = input("Would you like to create a user account? y or n ")
    if start == "y" or start == "n":
        if start == "y":

            c = Customer()
            c.enterDetails()

        elif start == "n":
            break
    else:
        print("Invalid input, please try again")
    

print("Thank you for entering the details")

a = Customer()
cDetails = a.readCustomersDetails()

print("\n")

# read details from textfile one by one using the index
print(cDetails)

# loop to bring all details back
for i in cDetails:
    print(i)


 










        