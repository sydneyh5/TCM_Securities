#Programmer:Sydney Hribar 
#Program Variables & Methods 
#Date: 1.19.2024 

age = 15 #global variable 

def nl():
	print('\n')

def who_am_i(): #This is a function without parameters
	name = "Sydney Hribar" #Local variable
	age = 15
	print("My name is",name,"and I am",age,"years old.")

who_am_i() #to call the function you need the parentheses because they are the parameters

nl()

age += 20

print(age)

nl()

def addOneHundred(num): #num is a Parameter
	print(num + 100)
	
addOneHundred(15) #15 is the Argument which inserts itself into the Parameter

nl()

addOneHundred(0)

nl()

def add(x,y):
	print(x + y)
	
add(8,5)
