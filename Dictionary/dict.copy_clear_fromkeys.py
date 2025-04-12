Profile={"Name": "Parahem",
        "University": "AASTU",
        "Year": "3rd",
        "Course": "OPP"}

X=Profile.copy()

X.update({'Department':'Electromechanical'})

print('\n',X)
print('\n',Profile)

print('\n',X.clear())
print('\n',Profile,'\n')

players = ["Messi", "Ronaldo", "Neymar"]

print(dict.fromkeys(players,'not played'))


