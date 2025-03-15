# Python Set

# a set is created by round brackets{}.

fruits = {'mango','banana','orange'}
print(fruits)  # {'banana', 'mango', 'orange'}

# Other way create Set
fruits = (('mango','banana','orange'))
print(fruits)  # ('mango', 'banana', 'orange')

# Adding Items to a Set
fruits = {'mango','banana','orange'}
fruits.add('greaps')
print(fruits)  # {'banana', 'greaps', 'mango', 'orange'}

# Removing an Item
fruits = {'mango','banana','orange'}
fruits.remove('banana')
print(fruits)  # {'mango', 'orange'}

# Checking if an Items Exists 
fruits = {'mango','banana','orange'}
print('mango' in fruits)  # True

# Combine Two Sets
x = {1,2,3}
y = {4,5,6}
x.update(y)
print(x)  # {1, 2, 3, 4, 5, 6}

# Accessing Item
fruits = {'mango','banana','orange'}
for fruit in fruits:
    print(fruits)


fruits = {'mango','banana','orange'}
fruits.discard('banana')
print(fruits)  # {'orange', 'mango'}

fruits = {'mango','banana','orange'}
fruits.pop()
print(fruits)  # {'mango', 'banana'}