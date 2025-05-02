from csv import reader

dogs = []
class Date:
    def __init__(self, date_string):
        l = date_string.split("-")
        self.day = l[2]
        self.month = l[1]
        self.year = l[0]
class Dog: # Creates a dog object containing important info 
    def __init__(self, info):
        self.name = info[2]
        self.colours = info[4]
        self.ward_name = info[6]
        self.bite = info[7]
        self.date = Date(info[9])

with open('Dogs Issued Dangerous Dog Orders.csv', newline='') as file:
    read = reader(file)
    for row in read:
        dog = Dog(row)
        dogs.append(dog)
