my_List = [1,2,3,4,5]
odd = filter((lambda x:x%2), my_List)
print(list(odd))


herr_List = [1,-2,-3,4,-5]
# filter() function with lambda function
positive = filter((lambda x:x>0), herr_List)
print(list(positive))
