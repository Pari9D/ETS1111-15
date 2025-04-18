supplier1= {"apple", "banana", "cherry", "date"}
supplier2 = {"banana", "cherry", "elderberry", "fig"}

print('\nAll Fruits=', supplier1.union(supplier2),'\n')
print('Common Fruits=',supplier1.intersection(supplier2),'\n')
print('Only suplier1 fruits',supplier1.difference(supplier2),'\n')

