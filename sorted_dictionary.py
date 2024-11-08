record = [{ 
    "name": "John", "score": 9 , 'age': 18},
    {"name": "Jane", "score": 8, 'age': 19},
    {"name": "Jim", "score": 7, 'age': 20},
    {"name": "Jill", "score": 6, 'age': 21},
]

from operator import itemgetter
print(sorted(record, key= itemgetter('score','age')))