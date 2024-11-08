name  = ['nick' , 'rob', 'john', 'harry']
age = [18, 17, 19 ,20]
grade = ['A', 'B', 'c' , 'A']

for x in zip(name, age, grade):
    print(x)


mylist = [[1,2,3,4], 
          [5,6,7,8], 
          [9,10,11,12]]

for x in zip(*mylist):
    print(x)
