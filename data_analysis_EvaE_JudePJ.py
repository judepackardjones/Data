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

def max_min_date(l,string):
    print(f"The maximum {string} where an attack occurred is {max(l)}, and the minimum is {min(l)}")

max_min_date([dog.date.day for dog in dogs], "day")
# list_dogs_year = [dog.date.year for dog in dogs]
# max_year = max(list_dogs_year)
# min_year = min(list_dogs_year)
# print(f"The most recent (maximum) year there was a dog attack was: {max_year}")
# print(f"The first (minimum) year there was a dog attack was: {min_year}")
# 
# list_dogs_month = [dog.date.month for dog in dogs]
# max_month = (max(list_dogs_month))
# min_month = (min(list_dogs_month))
# print(f"The most recent (maximum) month there was a dog attack was: {max_month}")
# print(f"The first (minimum) month there was a dog attack was: {min_month}")
# 
# list_dogs_day = [dog.date.day for dog in dogs]
# max_day = (max(list_dogs_day))
# min_day = (min(list_dogs_day))
# print(f"The most recent (maximum) day there was a dog attack was: {max_day}")
# print(f"The first (minimum) day there was a dog attack was: {min_day}")

#list_dogs_dates = [dog.date.day for dog in dogs if dog.date.year == 2017 and dog.date.month ==2]
#print(min(list_dogs_dates))
# latest_dogs_month = [dog.date.month for dog in dogs if dog.date.year == max_year]
# latest_month = max(latest_dogs_month)
# latest_dogs_day = [dog.date.day for dog in dogs if dog.date.year == max_year and dog.date.month == latest_month]
# print(f"The most recent dog attack took place on {max_year} / {latest_month} / {max(latest_dogs_day)}")
# 
# first_dogs_month = [dog.date.month for dog in dogs if dog.date.year == min_year]
# first_month = min(first_dogs_month)
# first_dogs_day = [dog.date.day for dog in dogs if dog.date.year == min_year and dog.date.month == first_month]
# print(f"The first ever dog attack took place on {min_year} / {first_month} / {min(first_dogs_day)}")
# 
# 
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

