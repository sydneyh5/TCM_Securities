#Programmer:Sydney Hribar
#Program Variables & Methods
#Date: 1.11.2024

quote = "All is fair in love and war!"

#Methods have empty parentheses at the end of them
print(quote)
print(quote.upper()) #uppercase method
print(quote.lower()) #lowercase method
print(quote.title()) #titlecase method
print(len(quote)) #The Amount of characters in the quote/counts the characters and it counts the spaces also

name = "Sydney Hribar" #String
age = 15 #int
gpa = 4.0 #float

print(int(30.1))
print(age)
print(int(gpa)) #takes a float and casts it into an int/ it makes the number with a decimal the same number but without the decimal 
print("\nMy name is " + name + ", and I am " + str(age) + " with a GPA of " + str(gpa) + ".") #concatenate variables while casting int to str

print("\nMy name is" ,name, ", and I am" ,age, "with a GPA of" ,str(gpa) + ".")
#Concatinating using a comma instead of a + while casting our gpa variable into a string to account for the spacing before the period at the end of the line


print("\nMy name is",name,"and I am",str(age),"with a GPA of",str(gpa) + ".") #The , concatenates the variables while the "str" casts the variables "age" and "gpa" which are integers into a string and also adds a space.
 
#Note that it reads program like a book top to bottom and left to right.
 
print("")
 
age += 1 #adds one to the variable age

print(age)
 
print("")
 
age += 10 #adds ten to the variable age

print(age)
print("")

birthday = 1
age += birthday #We can add two variables with the values as Int together
print(age)
