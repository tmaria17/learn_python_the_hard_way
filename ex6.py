#Sets a variable
types_of_people = 10
#interpolates the variable into the string x
x = f"There are {types_of_people} types of people."
#Set two strings to variables and sets a longer string to y variable with those two strings inside
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
#prit x and y string
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

#sets hilariois to false
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

#prints "Isn't that joke so funny?! False"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
#Combines w and e
print(w + e)
