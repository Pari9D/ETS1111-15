brown='the qUCIck bRoWn fOx JUMPES oVEr thE LazY DOG'
blue='tHe SKy is Blue'
green='.'
print(brown.split())
print(green.join(brown))
print(' -|- '.join([brown,blue,green]))
print(all(word.isalpha() for word in [brown, blue, green]))
print(green.isalpha)