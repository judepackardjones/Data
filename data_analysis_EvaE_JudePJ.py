from csv import reader # Reading from csv
from collections import Counter # Counting occurences of values 

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
        self.code = info[1]
        self.name = info[2]
        self.breed = info[3]
        self.colours = info[4]
        self.ward_name = info[6]
        self.bite = info[7]
        self.loc = info[8]
        self.date = Date(info[9])
        # We take almost all rows because they are significant for counting, but no other purpose
'''
UTILITY FUNCTIONS
'''
def month_num_to_str(num):
    return ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][num]

def max_min_date(when,string): 
    print(f"The maximum {string} where an attack occurred is {max(when)}, and the minimum is {min(when)}")
    
def latest_date(year,month,day): # Formats the date 
    print(f"The most recent day where a dog attack occurred was on {month_num_to_str(month)} {day}, {year}")

def first_date(year,month,day): # Formatting. We could probably combine the two functions but this seems a bit clearer for this purpose
    print(f"The first day where a dog attack occurred was on {month_num_to_str(month)} {day}, {year}")

def format_occurrence_tuple(tup): # Formats a tuple in the form of (word, number of occurrences)
    return str(tup[0]).capitalize() + ": found " + str(tup[1]) + " times"

def format_top_three(top): # Formats a list of three occurrence tuples. 
    return f"{format_occurrence_tuple(top[0])}, {format_occurrence_tuple(top[1])}, and {format_occurrence_tuple(top[2])}"

def split_values(value_list, s_char): # Splits a value like BROWN / TAN into ["BROWN", "TAN"] or PRIVATE PROPERTY to ["PRIVATE", "PROPERTY"], depending on s_char
    split_values = []
    for values in value_list:
        values = values.split(s_char)
        for value in values:
            split_values.append(value.strip())
    return split_values

# Git added this I don't want to touch it
#<<<<<<< HEAD








#=======
#>>>>>>> 0285ca986a9fd97b921808ed9a9f74df7cdc5865 
# I hope that isn't a private key, my git is public

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
    # Collections of important info (dog_days isn't needed more than once)
    dog_months = [dog.date.month for dog in dogs]
    dog_years = [dog.date.year for dog in dogs]

    # Average attacks per year 
    attacks_per_year = len(dogs)/(max(dog_years) - min(dog_years))

    # Average attacks per month
    attacks_per_month = attacks_per_year / 12

    # Highest month/months of attacks
    month_counter = Counter([(dog.date.year, dog.date.month) for dog in dogs]).most_common()
    month_threshold = month_counter[0][1]
    highest_months = [x[0] for x in month_counter if x[1] == month_threshold]


    # Highest year/years of attacks
    year_counter = Counter(dog_years).most_common()
    year_threshold = year_counter[0][1]
    highest_years = [str(x[0]) for x in year_counter if x[1] == year_threshold]
    h_years_str = " and ".join(highest_years)

    # Month distributions
    month_counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for dog in dogs:
        month_counts[dog.date.month - 1] += 1
    
    # Split colour value to individual colours 
    split_colours = split_values([dog.colours for dog in dogs], "/")
    
    # Split breed value to individual breeds
    split_breeds = split_values([dog.breed for dog in dogs], "/")

    # These next ones have no real world meaning but are required for the challenge portion

    # Split loc value to words 
    split_locs = split_values([dog.loc for dog in dogs], " ")

    # Split bite value into words
    split_bites = split_values([dog.bite for dog in dogs], " ")

    #Top Ten most common words

    top_ten_words = [dog.code for dog in dogs] + [dog.name for dog in dogs] + split_breeds + split_colours + [dog.ward_name for dog in dogs] + split_bites + split_locs
    top_words_counter = Counter(top_ten_words).most_common()[:10]
    top_words_formatted = []
    for x in top_words_counter:
        top_words_formatted.append(format_occurrence_tuple(x))
    top_words_formatted = ", ".join(top_words_formatted)

    # Total and average length of words in sentence values per dog colour
    length_values_colours = []
    for dog in dogs:
        word_count = len(dog.colours.split("/"))
        length_values_colours.append(word_count)
        
    number_words = len(length_values_colours)
    average_of_words = sum(length_values_colours)/number_words

    # Latest day
    max_year = max(dog_years)
    max_month =max([dog.date.month for dog in dogs if dog.date.year == max_year])
    max_day = max([dog.date.day for dog in dogs if dog.date.year == max_year and dog.date.month == max_month])

    # Earliest day
    min_year = min(dog_years)
    min_month = min([dog.date.month for dog in dogs if dog.date.year == min_year])
    min_day = min([dog.date.day for dog in dogs if dog.date.year == min_year and dog.date.month == min_month])

    # Most common names
    most_common_names = Counter([dog.name for dog in dogs]).most_common()[:3]

    # Most common colours
    most_common_colours = Counter(split_colours).most_common()[:3]

    # Most common breeds 
    most_common_breeds = Counter(split_breeds).most_common()[:3]

    '''
    DISPLAY FINDINGS
    '''

    # Average attacks per year
    print(f"The average attacks per year is: {round(attacks_per_year, 2)}")
    
    # Average attacks per month
    print(f"The average attacks per month is: {round(attacks_per_month, 2)}")

    # Highest average attacks per month
    print(f"The highest monthly average amount of dog attacks is in {month_num_to_str(month_counts.index(max(month_counts)))}, with an average of {round(max(month_counts)/12, 2)} attacks per year")

    # Lowest average attacks per month
    print(f"The lowest monthly average amount of dog attacks is in {month_num_to_str(month_counts.index(min(month_counts)))}, with an average of {round(min(month_counts)/12, 2)} attacks per year")

    # Highest month of attacks ever
    print(f"The highest amount of dog attacks in a single month is {month_threshold}, which occurred in {month_num_to_str(highest_months[0][1])} {highest_months[0][0]}") # Did not want to both making this scalable because they aren't tied anyway

    # Highest year of attacks
    print(f"The highest amount of dog attacks in a single year is {year_threshold}, which was in {h_years_str}")

    # Most common occurrences
    print(f"The top three most common names for dogs with the Dangerous Dog classification are {format_top_three(most_common_names)}")
    print(f"The top three most common colours for dogs with the Dangerous Dog classification are {format_top_three(most_common_colours)}")
    print(f"The top three most common breeds for dogs with the Dangerous Dog classification are {format_top_three(most_common_breeds)}")

    # Min maxes
    max_min_date([dog.date.day for dog in dogs], "day")
    max_min_date(dog_months, "month")
    max_min_date(dog_years, "year")
    
    # First ever attack date  
    first_date(min_year, min_month, min_day)
    
    # Latest attack date
    latest_date(max_year, max_month, max_day)
    
    # Amount of colour words and average 
    print(f"There are {number_words} total words in all dog's colour values, and the average amount of words per dog colour value is {round(average_of_words, 2)}")

    # Overall most common words
    print(f"The top ten most common words and the amount they're repeated in this file are: {top_words_formatted}")

main()