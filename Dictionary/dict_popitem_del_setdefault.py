Profile={"Name": "Parahem",
        "University": "AASTU",
        "Year": "3rd",
        "Course": "OPP"}

print('\n',Profile)

X= Profile.popitem()
print('\nThe deleted Item is :',X)

print('\n',Profile)

del Profile['Year']

print('\n',Profile)

print('----------------------------------------')

Profile.setdefault('Name','Ibrahim')
Profile.setdefault('Hobby','Playing begena')

print('new profile:')

print('\n')

for key,value in Profile.items():
    print(key+'=>'+value,)
print('\n')
