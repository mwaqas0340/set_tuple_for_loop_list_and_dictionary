# A dictionary is written with curly brackets.


person = {
    'first_name': 'Muhammad',
    'last_name': 'Waqas',
    'age': 21,
    'is_married': False
}
# value add or update in dictionary
person['hobby'] = 'Playing cricket'
print(person)


person = {
    'first_name': 'Muhammad',
    'last_name': 'Waqas',
    'age': 23,
    'is_married': False
}

# First method to access dictionary value
print(person.get('first_name'))
print(person.get('last_name'))


# Second method to access dictionary value
x = person['first_name']
y = person['last_name']
print(x)
print(y)


person = [{
    'first_name': 'Muhammad',
    'last_name': 'Waqas',
    'age': 21,
    'is_married': False
},{
    'first_name': 'Muhammad',
    'last_name': 'Fahham',
    'age': 19,
    'is_married': False
}
]
person.pop()
print(person)


# Nested dictionary

students={
    'student1':{
        'first_name': 'Muhammad',
        'last_name': 'Waqas',
        'age': 21,
    },
    'studen2':{
        'first_name': 'Muhammad',
        'last_name': 'Fahham',
        'age': 19,
    }
}
print(students)


person = {
  'student1': {
    'name': 'Waqas',
    'cast': 'Rajput',
    'age': 23
    },
  'student2': {
    'name': 'Ahmer',
    'cast': 'Malik',
    'age': 19
    }
}
for person in person:
    print(person)