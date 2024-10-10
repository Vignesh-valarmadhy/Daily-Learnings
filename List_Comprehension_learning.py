num = [1,2,5]

# num =[i*2 for i in [1,2,5]]
# print(num)  

# def timeSix(num):
#     return num * 2

# result = [timeSix(i) for i in num] #if i > 2]
# print(result)

string = ["intro", "to", "list", "comprehension"]
dicts = [{"name":"John"}, {"name":"henry"}]

# result = []
# for i in dicts:
#     result.append(i['name'])
#     print(result)

result = [i['name'] for i in dicts]
print(result)   