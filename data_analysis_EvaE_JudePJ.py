from csv import reader

dogs = []
class Dog:
    def __init__(self, name, colours, ward_name, bite, date):
        self.name = name
        self.colours = colours
        self.ward_name = ward_name
        self.bite = bite
        self.date = date

class Date:
    def __init__(self, date_string):
        l = date_string.split("-")
        self.day = l[2]
        self.month = l[1]
        self.year = l[0]


with open('Dogs Issued Dangerous Dog Orders.csv', newline='') as file:
    read = reader(file)
    for row in read:
        dog = Dog(row[2], row[4], row[6], row[7], Date(row[9]))
        dogs.append(dog)
