# Python List


# indexing ->          0        1          2
names: list[str] = ['Waqas','Tanzeela','Fahham']
# indexing <-         -3       -2         -1
print(names[-2]) # Tanzeela
print(f'My name is {names[0].upper()}')


# Range of Indexes

fruits = ['mango','banana','orange','greaps']
x = fruits[1:3]   # ['banana','orange'] 
x = fruits[:2]    # ['mango', 'banana']
x = fruits[2:]    # ['orange', 'greaps']
print(x)


# Adding Items to a list

fruits = ['mango','banana','orange']
fruits.append('greaps')  # adding last item from index 
print(fruits)   # ['mango','banana','orange','greaps']


# Insert Items to a list

fruits = ['mango','banana','orange']
fruits.insert(2,'greaps')  # adding spacefied index 
print(fruits)   # ['mango', 'banana', 'greaps', 'orange']


# Remove Items from a list

fruits = ['mango','banana','orange']
fruits.remove('mango')  # remove spacefied index
print(fruits)    # ['banana','orange']  


# Pop Items from a list

fruits = ['mango','banana','orange']
fruits.pop()  # remove last item from index
print(fruits)   # ['mango', 'banana']


# Delete Items from a list

fruits = ['mango','banana','orange']
del fruits[1]       # delete spacefied index
print(fruits)       # ['mango', 'orange']


# Getting the length of alist

fruits = ['mango','banana','orange']  
print(len(fruits))   # 3


# Changing an Items Value

fruits = ['mango','banana','orange']  
fruits[1] = 'greaps'
print(fruits)    # ['mango', 'greaps', 'orange']


# Checking if an Item Exists 

fruits = ['mango','banana','orange']  
print('mango' in fruits)   # True


# Extending a List

nums1 = [1,2,3,4,5]
nums2 = [6,7,8,9,10]
nums1.extend(nums2)
print(nums1)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Looping Thruogh a List

fruits = ['mango','banana','orange','greaps']

for fruit in fruits:
 print(fruits)

