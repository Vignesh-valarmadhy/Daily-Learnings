# works for tuple sorting 
record = [('Nicolas', 18 ,51),
          ('Rob', 21 ,25),
          ('John', 19 , 45),
          ('Harry' , 5 ,12)]
# print(sorted(record))

from operator import itemgetter
k = itemgetter(1)

print (sorted(record, key=itemgetter(1,2)))

