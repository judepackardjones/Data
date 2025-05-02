from csv import reader

dogs = []
class Date: # Contains date data for easier accessibility
    def __init__(self, date_string): # Creates date object based on a date string
        l = date_string.split("-") # Splits something like "2024-02-08" to ["2024", "02", "08"], which are each parsed into ints 
        self.day = int(l[2])
        self.month = int(l[1])
        self.year = int(l[0])
    
class Dog: # Contains dog data
    def __init__(self, info): # Takes important info from each row. We can modify later if we want to get different data from the file
        self.name = info[2]
        self.colours = info[4]
        self.ward_name = info[6]
        self.bite = info[7]
        self.date = Date(info[9])

with open('Dogs Issued Dangerous Dog Orders.csv', newline='') as file: # Reads csv
    read = reader(file)
    for row in read: # Iterates over each row in file and creates a dog object for each and appends to dog list 
        dog = Dog(row)
        dogs.append(dog)

def max_min_date(when,string):
    print(f"The maximum {string} where an attack occurred is {max(when)}, and the minimum is {min(when)}")

max_min_date([dog.date.day for dog in dogs], "day")
max_min_date([dog.date.month for dog in dogs], "month")
max_min_date([dog.date.year for dog in dogs], "year")


def latest_date(year,month,day):
        print(f"The latest day where a dog attack occurred was on {max(year)}/{max(month)}/{max(day)}")

latest_date([dog.date.year for dog in dogs], [dog.date.month for dog in dogs if dog.date.year == 2025],
            [dog.date.day for dog in dogs if dog.date.month==3 and dog.date.year == 2025])

def first_date(year,month,day):
        print(f"The first day where a dog attack occurred was on {min(year)}/{min(month)}/{min(day)}")

first_date([dog.date.year for dog in dogs], [dog.date.month for dog in dogs if dog.date.year == 2017],
            [dog.date.day for dog in dogs if min(dog.date.month) and dog.date.year = 2017])



'''
EXAMPLES
'''

# # Accessing general info
# for dog in dogs:
#     print(dog.name) # Get all dog's names
#     print(dog.date.day) # Gets all dog's days of attack

# # Accessing specific dog info
# print(dogs[0].name) # Dog #1 is named chloe 

# Finding related info about specific dogs with certain characteristic
# for dog in dogs:
#     if dog.name.lower() == "pablo":
#         print(dog.bite) # There are two dogs named pablo and they both have SEVERE bites

# Counting occurences of specific value
# print(len([dog for dog in dogs if dog.name.lower() == "zeus"])) # 6 dogs are named zeus

