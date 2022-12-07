

from audioop import add


users = ["Alice","Bob","Peter","Dan"]

print(len(users))


while True:
    print("Hi my name is Daniel")
    name = input("Whats is your name?: ").strip().capitalize()
    
    if name in users:
        print("Hello " + name )
        remove = input("Would you like to be removed from the system (y/n)?: ").capitalize()
        
        if remove == "Y":
            users.remove(name)
            print(users)
        elif remove == "N":
            print("User not removed")
            
    else:
        print("Name not registered")
        add_user= input("Would you like to be on the system? (y/n): ").capitalize()
        if add_user == "Y":
            users.append(name)
            print(users)
            print("Name registered")
        elif add_user == "N":
            print("Name not registered")
    break