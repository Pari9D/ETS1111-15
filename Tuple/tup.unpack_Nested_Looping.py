Person = ("Parahem", 20, "Addis Ababa")
Name, Age, City = Person
print('Name;',Name)
print("Age:",Age)
print("City:",City,'\n')

Student = ("Parahem", ("Math", "Science", "History"))
print("Student name:", Student[0])
print("Subjects:", Student[1])
print("First subject:", Student[1][0],'\n')

for Profile in Person:
    print("Personal Pprofile:", Profile)

