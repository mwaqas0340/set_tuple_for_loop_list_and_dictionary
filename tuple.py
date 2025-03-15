# Python Tuple
# A tuple is created by round brackets().

fruits = ('mango','banana','orange')
print(fruits)  # ('mango', 'banana', 'orange')

# Other way create Tuple
fruits = (('mango','banana','orange'))
print(fruits) # ('mango', 'banana', 'orange')

# Indexing
fruits = ('mango','banana','orange')
print(fruits[1])  # banana

# Negative Indexing
fruits = ('mango','banana','orange')
        #   -3       -2       -1
print(fruits[-3])  # mango

# Range of Indexing
fruits = ('mango','banana','orange')
print(fruits[0:2]) # ('mango', 'banana')
 
# Checking of an Item Exists
fruits = ('mango','banana','orange')
print('mango' in fruits) # True

# Combine Tuple
fruits1 = ('mango','banana')
fruits2 = ('orange','greaps')
print(fruits1+fruits2)  # ('mango', 'banana', 'orange', 'greaps')

# Looping Through a Tuple 
fruits = ('mango','banana','orange')
for fruit in fruits:
 print(fruits)

# Tuples are Immutable

# In Python tuples are immutable(unchangeable)
# It means you can NOT add, remove or change its items