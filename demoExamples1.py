myVariableName = "Pema" #Camel Case

MyVariableName = "Pema" #Pascal Case

my_variable_name = "Pema" #Snake Case

#STRING
print('Hello World!')
print("Hello World!")

multipleLines = '''This is a string
that spans multiple lines.'''

print(multipleLines)

a = 1
b = 2
c = a + b
print(type(c)) #Data Type of c is int
c = str(c) #Type Casting
print(type(c)) #Data Type of c is now str  


#INTEGERS 
a = -1
print(type(a)) #Data Type of a is int
print(a) #Output: -1

pi = 3.14
print(type(pi)) #Data Type of pi is float
pi = int(pi) #Type Casting
print(type(pi)) #Data Type of pi is now int

#FLOAT 
Full_marks = 100
print(type(Full_marks)) #Data Type of Full_marks is int
Full_marks = float(Full_marks) #Type Casting
print(type(Full_marks)) #Data Type of Full_marks is now float

#Boolean 
a = bool(0) #False
b = bool(1) #True
print(type(a)) #Data Type of a is bool
print(type(b)) #Data Type of b is bool
a = bool("") #False
b = bool("Hello") #True 


#None 
a = 1
b = 2
c = None
print(type(c)) #Data Type of c is NoneType
c = a + b
print(type(c)) #Data Type of c is now int

print(1%2) #Output: 1
print(2 ** 3) #Output: 8
print(10 // 3) #Output: 3

