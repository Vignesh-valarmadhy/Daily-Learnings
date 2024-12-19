import sqlite3

class Person:

    def __init__(self, id_number = -1 , first = "" , last= "", age = -1):
        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.connect('mydata.db')
        self.cursor = self.connection.cursor()
    
    def load_person(self , id_number):
        self.cursor.execute (""" SELECT * FROM persons
        WHERE id = {} """.format(id_number))

        results = self.cursor.fetchone()
        self.id_number = id_number
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]
    
    def insert_person(self):
        self.cursor.execute(""" 
        INSERT INTO persons VALUES
        ({} , '{}' , '{}' , {})
        """.format(self.id_number , self.first , self.last , self.age))
        self.connection.commit()
        self.connection.close()

    # def insert_person(self):
    #     self.cursor.execute("SELECT id FROM persons WHERE id = ?", (self.id_number,))
    #     if self.cursor.fetchone():
    #         print(f"Error: ID {self.id_number} already exists.")
    #         return

    #     self.cursor.execute(""" 
    #     INSERT INTO persons (id, first_name, last_name, age) VALUES (?, ?, ?, ?)
    #     """, (self.id_number, self.first, self.last, self.age))
    #     self.connection.commit()
    #     self.connection.close()



# connection = sqlite3.connect('mydata.db')

# cursor = connection.cursor()

# cursor.execute("""  
# CREATE TABLE IF NOT EXISTS persons (
# id INTEGER PRIMARY KEY,
# first_name TEXT,
# Last_name TEXT,
# age INTEGER) """)

# cursor.execute (""" 
# INSERT INTO persons 
# VALUES
# (1,'paul' , 'Smith' , 24),
# (2,'Mark' , 'Johnson' ,42),
# (3,'John' , 'Smith' , 30)""")

# cursor.execute(""" SELECT * FROM persons WHERE last_name = 'Smith' """)

# rows = cursor.fetchall()
# print(rows)

# connection.commit()

# connection.close()


p1 = Person(4, "Alex", "Johnaon", 78)
p1.insert_person()

# p1.load_person(1)

# print(p1.first)
# print(p1.last)
# print(p1.age)
# print(p1.id_number)

connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()


cursor.execute("SELECT * FROM persons")
results = cursor.fetchall()
print(results)
connection.close()