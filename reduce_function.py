import functools
my_List = [1,2,3,4,5]

prod = (functools.reduce((lambda x,y : x * y), my_List))
print(prod)

# 1*1 = 1
# 2*1 = 2
# 3 * 2 = 6
# 4 * 6 = 24
# 5*24 = 120

greatest = (functools.reduce((lambda x,y : y if (y>x) else x), my_List))
print(greatest)
