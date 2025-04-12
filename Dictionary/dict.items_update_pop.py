Profile={"Name": "Parahem",
        "University": "AASTU",
        "Year": "3rd",
        "Course": "OPP"}

print(Profile.items())

print('----------------------------------------------')

for keys,values in Profile.items():
    print(keys+'=>'+values)

print('----------------------------------------------')

Profile.update({'Department':'EME'})
for keys,values in Profile.items():
    print(keys+'=>'+values)

print('-----------------------------------------------')

X=Profile.pop('Course')
print('\nRemoved Cource:',X)


print('\nUpdated profile:')
for keys,values in Profile.items():
    print(keys+'=>'+values)
