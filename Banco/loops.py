

#answer = input("Why is the skye blue?: ").lower()

#while answer != "just because":
#    answer = input("Why?: ").strip().lower()

students = {
    "male": ["Tom", "Juan" ,"Charlie"],
    "female": ["Sara","Daniela","Ruth"]
}

for gender in students.keys():
    for name in students[gender]:
        if "a" in name:
            print (name)