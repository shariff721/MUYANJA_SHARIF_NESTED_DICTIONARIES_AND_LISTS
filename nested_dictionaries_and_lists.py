
# 1. update values in dictionaries and lists

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
print(x)
students[0]['last_name'] = 'Bryant'
print(students)

sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
z[0]['y'] = 30

print(z)



# 2. iterate through dictionaries

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary(students):
    for x in students:
        print(f"first_name - {x['first_name']}, last_name - {x['last_name']}")

iterateDictionary(students)




# 3. Get values from a list of dictionaries

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


def iterateDictionary2(a,b):
    for i in students:
        if a == 'first_name':
            print(i['first_name'])
        elif a == 'last_name':
            print(i['last_name'])

iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)



# 4. iterate through dictionary with list values

dojo = {
'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(a):
    for key,values in a.items():
        print(f"{len(a[key])} {key}")
        for value in values:
            print(value)

printInfo(dojo)
