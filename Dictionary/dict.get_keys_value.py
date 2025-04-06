Profile={"Name": "Parahem",
        "University": "AASTU",
        "Year": "3rd",
        "Course": "OPP"}
print(Profile.get('Name'))
print(Profile.get('fav_food'))
print(Profile.get('fav_food','N/A'))

print('------------------------------------------------')
print(Profile.keys())

print('------------------------------------------------')
for key in Profile:
    print('key:',key)
    
print('------------------------------------------------')

print(Profile.values())

print('------------------------------------------------')
for value in Profile:
    print('value:',value)