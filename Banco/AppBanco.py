Accounts = {
    "Daniel": {"Password" : "HolaPerros", "Money" : 2000},
    "Ruth" : {"Password" : "Hermosa", "Money" : 0}
    }


def welcome():
    print("Welcome to the app")
    print("1.- New User") #completed
    print("2.- Deposit") #completed
    print("3.- Withdrawal") #completed
    print("4.- Transferer")
    print("5.- Remove User") #completed
    print("6.- Check money") #completed
    print("7.- All users") #completed
    print("8.- Go out") #completed

def spicing():
    print("*"*20)
    

def new_User():
    name = input("What is your name?: ").capitalize()
    passWord = input("Write your password?: ")
    money = int(input("Select the amount of money you have: "))
    Accounts[name] = {"Password" : passWord, "Money": money}
    print("User created")
    print(Accounts[name])
    

def status(name,passWord):
    if name in Accounts:
        if passWord == Accounts.get(name)["Password"]:
            spicing()
            print("Welcome " + name)
            print("You have $", Accounts[name]["Money"] , "In your account") 
        else:
            print("Password incorrect")
    else:
        print("Name not Found")
        
        
def userRemoved(name, passWord):
    if name in Accounts:
        if passWord == Accounts.get(name)["Password"]:
            spicing()
            deleteAccount = input(("Are you sure about to delete the account?(y/n): ")).upper()
            if deleteAccount == "Y":
                Accounts.pop(name)
                print("Account removed")
            elif deleteAccount == "N":
                pass
            else:
                print("Invalid Option")
        else:
            print("Password incorrect")
    else:
        print("Name not Found")
        
        
def deposit(name, passWord):
    if name in Accounts:
        if passWord == Accounts.get(name)["Password"]:
            spicing()
            depositTrue = "N"
            while (depositTrue == "N"):
                newDeposit = int(input("Write the amount of money: "))
                depositTrue = input("is this the correct amount (y/n)?: ").upper()
                
                if depositTrue == "Y":
                    oldMoney = Accounts[name]["Money"]
                    totalMoney = oldMoney + newDeposit
                    Accounts[name]["Money"] = totalMoney
                    print(Accounts[name])
                    
                elif depositTrue == "N":
                    pass
                
                else:
                    print("Invalid Option")
        else:
            print("Password incorrect")
    else:
        print("Name not Found")
        

def withdrawal(name,password):
    if name in Accounts:
        if passWord == Accounts.get(name)["Password"]:
            spicing()
            withdrwaalaTrue = "N"
            while (withdrwaalaTrue == "N"):
                wirhdrawal = int(input("Write the amount of money: "))
                withdrwaalaTrue = input("is this the correct amount (y/n)?: ").upper()
                
                if withdrwaalaTrue == "Y":
                    oldMoney = Accounts[name]["Money"]
                    totalMoney = oldMoney - wirhdrawal
                    Accounts[name]["Money"] = totalMoney
                    print(Accounts[name])
                    
                elif withdrwaalaTrue == "N":
                    pass
                
                else:
                    print("Invalid Option")
        else:
            print("Password incorrect")
    else:
        print("Name not Found")
        
def transferer(name,password,tansfererName):
    if name in Accounts:
        if password == Accounts.get(name)["Password"]:
            if tansfererName in Accounts:
                spicing()
                transfererTrue = "N"
                while transfererTrue == "N":
                    transfererAmount = int(input("Write the amount of money: "))
                    transfererTrue = input("is this the correct amount (y/n)?: ").upper()
                    if transfererTrue == "Y":
                        oldMoney = Accounts[name]["Money"]
                        totalMoney = oldMoney - transfererAmount
                        Accounts[name]["Money"] = totalMoney
                        print(Accounts[name])
                        
                        oldMoneyTransfered = Accounts[tansfererName]["Money"]
                        totalMoneyTransfered = oldMoneyTransfered + transfererAmount
                        Accounts[tansfererName]["Money"] = totalMoneyTransfered
                        print("The money has been transfered!")
                        
                    elif transfererTrue == "N":
                        pass
                    else:
                        print("Invalid Option")
            else:
                print("Name not found!")
                
        else:
            print("Password Incorrect")
    else:
        print("Name not found!")
        
        
        
        
        
if __name__ == "__main__":
    while(True):
        spicing()
        welcome()
        number_decision = int(input("Choose the the option you want to do:"))
        if number_decision not in [1,2,3,4,5,6,7,8]:
            spicing()
            print("Invalid option")
            
        elif number_decision == 1: #completed
            spicing()
            print("New User")
            new_User()
            
        elif number_decision == 2: #completed
            spicing()
            print("Deposit")
            name = input("What is your name?: ").capitalize()
            passWord = input("What is your password?: ")
            deposit(name,passWord)
            
        elif number_decision == 3:
            spicing()
            print("Withdrawal")
            name = input("What is your name?: ").capitalize()
            passWord = input("What is your password?: ")
            withdrawal(name,passWord)
            
        elif number_decision == 4:
            spicing()
            print("Transferer")
            name = input("What is your name?: ").capitalize()
            passWord = input("What is your password?: ")
            transfererName = input("Write the name of the account to transferer: ").capitalize()
            transferer(name,passWord,transfererName)
            
        elif number_decision == 5:
            spicing()
            print("Remove user")
            name = input("What is your name?: ").capitalize()
            passWord = input("What is your password?: ")
            userRemoved(name,passWord)
            
        elif number_decision == 6: #completed
            spicing()
            name = input("What is your name?: ").capitalize()
            passWord = input("What is your password?: ")
            status(name,passWord)
            
                    
        elif number_decision == 7: #completed
            spicing()
            print(Accounts)
        
        elif number_decision == 8: #completed
            spicing()
            print("Good bye!")
            break
        else:
            print("Invalid Option!")
        