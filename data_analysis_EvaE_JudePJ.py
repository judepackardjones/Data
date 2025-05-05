from csv import reader
from collections import Counter

'''
CLASS DEFINITIONS
'''
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
'''
UTILITY FUNCTIONS
'''
def month_num_to_str(num):
    return ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][num]

def max_min_date(when,string):
    print(f"The maximum {string} where an attack occurred is {max(when)}, and the minimum is {min(when)}")
    
def latest_date(year,month,day):
    print(f"The latest day where a dog attack occurred was on {max(year)}/{max(month)}/{max(day)}")

def first_date(year,month,day):
    print(f"The first day where a dog attack occurred was on {min(year)}/{min(month)}/{min(day)}")
    
#<<<<<<< HEAD








#=======
#>>>>>>> 0285ca986a9fd97b921808ed9a9f74df7cdc5865
'''
EXAMPLES
'''

# # Accessing general info
#for dog in dogs:
#     print(dog.name) # Get all dog's names
#     print(dog.date.day) # Gets all dog's days of attack

# # Accessing specific dog info
# print(dogs[0].name) # Dog #1 is named chloe 

# Finding related info about specific dogs with certain characteristic
# for dog in dogs:
#     if dog.name.lower() == "pablo":
#         print(dog.bite) # There are two dogs named pablo and they both have SEVERE bites

# Counting occurrences of specific value
# print(len([dog for dog in dogs if dog.name.lower() == "zeus"])) # 6 dogs are named zeus

#     for dog in dogs:
#         word_length = len(dog.colours)
#         answer.append(word_length)
#         word_count = len(dog.colours.split())
def main():
    '''
    EXTRACTION
    '''
    dogs = []
    # Enter data into dogs list 
    with open('Dogs Issued Dangerous Dog Orders.csv', newline='') as file: # Reads csv
        read = reader(file)
        for row in read: # Iterates over each row in file and creates a dog object for each and appends to dog list 
            dog = Dog(row)
            dogs.append(dog)
    '''
    DATA ANALYSIS
    '''

    attacks_per_year = len(dogs)/(max([dog.date.year for dog in dogs]) - min([dog.date.year for dog in dogs]))

    attacks_per_month = attacks_per_year / 12

    # Highest month/months of attacks
    highest_month = 0
    year_months = [] # We are using a list because we don't know if there will be a tie. Even though there is not a tie, we will keep this. 
    years = list(dict.fromkeys(dog.date.year for dog in dogs))
    for year in years:
        for month in range(1, 13):
            count = len([0 for dog in dogs if dog.date.month == month and dog.date.year == year]) # We don't care whats appended to the list because we're just counting the length
            if count > highest_month:
                highest_month = count
                year_months.clear()
                year_months.append((year, month))
            elif count == highest_month:
                year_months.append((year, month))
    # Highest year/years of attacks
    highest_year = 0
    highest_years = []
    for year in years:
        count = len([0 for dog in dogs if dog.date.year == year])
        if count > highest_year:
            highest_year = count
            highest_years.clear()
            highest_years.append(str(year))
        elif count == highest_year:
            highest_years.append(str(year))
    h_years_str = " and ".join(highest_years)

    # Month distributions
    month_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for dog in dogs:
        month_counts[dog.date.month - 1] += 1
    

    # Average attacks per year
    print(f"The average attacks per year is: {round(attacks_per_year, 2)}")
    # Average attacks per month
    print(f"The average attacks per month is: {round(attacks_per_month, 2)}")
    # Highest month of attacks ever
    print(f"The highest amount of dog attacks in a single month is {highest_month}, which occurred in {month_num_to_str(year_months[0][1])} {year_months[0][0]}") # Did not want to both making this scalable because they aren't tied anyway
    # Highest year of attacks
    print(f"The highest amount of dog attacks in a single year is {highest_year}, which was in {h_years_str}")
    # Highest average attacks per month
    print(f"The highest monthly average amount of dog attacks is in {month_num_to_str(month_counts.index(max(month_counts)))}, with an average of {round(max(month_counts)/12, 2)} attacks per year")
    # Lowest average attacks per month
    print(f"The lowest monthly average amount of dog attacks is in {month_num_to_str(month_counts.index(min(month_counts)))}, with an average of {round(min(month_counts)/12, 2)} attacks per year")

    # Min maxes
    max_min_date([dog.date.day for dog in dogs], "day")
    max_min_date([dog.date.month for dog in dogs], "month")
    max_min_date([dog.date.year for dog in dogs], "year")

    # First ever attack date  
    first_date([dog.date.year for dog in dogs], [dog.date.month for dog in dogs if dog.date.year == 2017],
            [dog.date.day for dog in dogs if dog.date.month == 2 and dog.date.year == 2017])
    
    # Latest attack date
    latest_date([dog.date.year for dog in dogs], [dog.date.month for dog in dogs if dog.date.year == 2025],
        [dog.date.day for dog in dogs if dog.date.month==3 and dog.date.year == 2025])
    
    # Total and average length of words in sentence values per dog colour
    length_values_colours = []
    for dog in dogs:
        word_count = len(dog.colours.split())
        length_values_colours.append(word_count)
        number_words = len(length_values_colours)
        average_of_words = sum(length_values_colours)/number_words

    print(f"There are {number_words} total words in the dog's colour value, and the average amount of words per dog colour value is {round(average_of_words, 2)}")

    #Top Ten most common words
    top_ten_words = list(dog.name for dog in dogs) + list(dog.colours for dog in dogs) + list(dog.ward_name for dog in dogs) + list(dog.ward_name for dog in dogs)
    top_words_counter = Counter(top_ten_words)
    print(f"The top ten most common words and the amount they're repeated in this file are: {str(top_words_counter)[9:256]}")

    
        #counter_numbers = Counter(dog.date.year)
        #print(counter_numbers)
    #print(f"Item count: [counter_words]")

    
    pass
main()




