blue= "HELLO, WORLD!"
green = "Pythön is fun!"
yellow = "this is all lower!"

encoded_blue = blue.encode("utf-8")
encoded_green = green.encode("utf-8")

print(encoded_blue)  
print(encoded_green)  # (special character encoded)

print(blue.islower()) 
print(green.islower())  
print(yellow.islower())  

print(blue.isupper()) 
print(green.isupper())  
print(yellow.isupper())
