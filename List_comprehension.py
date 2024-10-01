# Provide a concise way to create a list 
# They consist of bracket by a for clause and can also
# include if clauses 
#  this allows for a powerfull filtering and transformation 
# of iterables in a compact form 




#  start with expressiion then do transformation

# num = [2, 4, 5]

# natural_number = [num * 2 for num in range(1,11)]
# natural_number

# print(list(map(lambda x: x*2, num)))

# Syntax

# [expression for item in iterable]

# print([x*2 for x in num])


#  using If logic

# [expression for item in iterable if condition ]

# check even numbers from 1 to 20

# print([num for num in range(1,20+1) if num%2 == 0])

# fruits = ['banana', 'mango', 'apples', 'cherry']

# print([i for i in fruits if len(i)>5])


#  use list comprehension to create a list of square of first five natural numbers 

# print([i**2 for i in range(1,5+1) ])


# # use a list comprehension to filter out negative numbers in a list
# numbers = [1, -3 , -8 ,- 40 , 8 ,9 ,6 ,5, 2 ]
# print([i for i in numbers if i >0 ])
