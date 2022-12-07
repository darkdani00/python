


#students = {
#    "Alice": ["ID0001",26,"A"],
#    "Bob": ["ID0002",20,"B"],
#    "Claire":["ID0003",29,"C"],
#   "Daniel":["ID0004",22,"A"]
#    }

#print(students["Alice"])

#print(students["Daniel"])


students = {
    "Alice": {"ID":"ID0001","Age":26,"Grade":"A"},
    "Bob": {"ID":"ID0002","Age":22,"Grade":"B"},
    "Claire": {"ID":"ID0003","Age":20,"Grade":"A"},
    "Daniel": {"ID":"ID0004","Age":29,"Grade":"C"}
    }
print(students["Daniel"])

numero = int(input("numero: "))

oldMoney = students.get("Daniel")["Age"]

newMoney =  oldMoney + numero

students["Daniel"]["Age"] = newMoney

print(students["Daniel"])






#print(students)

#print(students["Daniel"])
#user = input("Nombre: ").capitalize()
#id = int(input("ID:" ))
#age = int(input("Age: "))
#grade = input("Grade: ")
#students[user] = {"ID": id, "Age": age, "Grade": grade}

#if "ID0004" == students.get("Daniel")["ID"]:
#    print("hola")
#    print(students.get("Daniel")["ID"])

    


#students["Fred"] = 30

#print(students)

#del students["Fred"]

#print(students)
