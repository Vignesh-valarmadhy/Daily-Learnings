class Person:
    amount = 0
    def __init__(self,name , age , height):
        # print("Hello World")
        # self.name = "Mike"
        # self.age = 34

        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1

    def __del__(self):
        Person.amount -= 1


    # def __del__(self):
    #     print("object deleted")

    def __str__(self):
        return "Name :{} , Age :{} , Height :{}".format(self.name , self.age , self.height)

    def get_older(years):
        self.age += years




P = Person("Mike" , 30 , 180)
# print(P.name)
# print(P.age)
# print(P.height)

# P.name = "Henry"
# print(P.name)

# x = HelloWorld(self)


# del P
P2 = Person("Sara", 15 ,156)
print(P,P2)
print("Before deleting",Person.amount)
del P2
print("after deleting", Person.amount)


