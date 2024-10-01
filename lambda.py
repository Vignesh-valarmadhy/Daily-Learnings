# syntax for lambda function 

lambda arguments : expression

addition = lambda x,y : x + y
print(addition(9,9))

mul = lambda a,b,c,d : a * b * c * d
# function and parameter passed: what we want result 

mul(1,2,3,4)


# write a lamdba function that returns the square of a number

square = lambda x : x**2

print(square(5))


#  Write a lambda function to convert a string to uppercase

hw = "convert this into uppercase"

result = lambda s:s.upper()
print(result(hw))

 
#  write a lambda function that takes a list of
# numbers and returns the maximum value

numbers = [1,2,3,4,5,6,7,8]

maxi= lambda x : max(x)
print(maxi(numbers))

# return the square of the list
num = [1,2,3,4,5,6,7,8]
list(map(lambda x : x**2 , num))
print(list(map(lambda x : x**2 , num)))  # map function is used to



# create a lambda function that checks if a given number is even 
# even = lambda x : x % 2 == 0
print(even(2))
# print(lambda x : x % 2 == 0)  # this will return


num = [1,2,3,4,5,6,7,8]

print(list(map(lambda x : x % 2 == 0, num)))











