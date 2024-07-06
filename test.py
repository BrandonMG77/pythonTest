name = "Brandon"
print(name)
#53:10 4/12/2023
hola = ["hola444","hola2"] #array or list
hola1 = {"hi": "ingles", "hola": "Espanol"} # Dictionary    
print(hola[0])
print(type(hola1))
print(isinstance(hola1, dict))

#Terciary Operator
def isadult(age):
    return True if age > 18 else False
print (isadult(19))
#Bool

done = True

if done:
    print("yes")
else: print("False")

#any # 1:26 

# ENUMS are used in PYTHON to create CONSTANTS  
# 1:32
# I can "extend" an array array.extend([new-thing])

#1:45$Tuples is a like a list but cannot me modified
names = ("Roger", "Zack")

# In a dic you can use "keys" to find the keys. ex dog.keys() you can even return a list list(dog.keys())

# 2:06 Functions

# Optional arguments in functions example:
def hello(name="my friend"):
    print("hello "+ name)

hello("Carlos")
hello()

# 2:11  
#Nested functions 2:18

#2:30   

#2:37 CLASS

class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

        def bark(self):
            print ("woof")
            
roger = Dog("Minu", 7) 

print(roger)
