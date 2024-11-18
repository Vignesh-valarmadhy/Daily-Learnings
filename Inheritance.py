class Person:
    def __init__(self,name,age,height):
        self.name = name
        self.age = age
        self.height = height
    
    def __str__(self):
        return "Name : {} , Age : {} , Height : {}".format(self.name , self.age , self.height)
    
    def get_older(years):
        self.age += years


class Worker(Person):
    def __init__(self , name , age, height , salary):
        super(Worker,self).__init__(name, age , height)
        self.salary = salary 
    def __str__(self):
        text = super(Worker,self).__str__()
        text += ",salary {}".format(self.salary)
        return text

    def cal_yearly_salary(self):
        return self.salary * 12

Worker1 = Worker("Henry", 40 , 176, 35000)
print(Worker1)

print(Worker1.cal_yearly_salary())

        

