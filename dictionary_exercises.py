# Problem 1
# Assign the following dictionary to a variable

countries = {
  "Asia":["China", "Mongolia", "India"],
  "South America": ["Brazil", "Argentina", "Chile"],
  "North America": ["United States", "Canada", "Mexico"], "Antarctica": [],
  "Africa": ["South Africa", "Algeria", "Kenya", "Ethiopia", "Egypt"],
  "Europe": ["France", "Germany", "England", "Spain", "Greece", "Italy"],
  "Australia": ["New Zealand", "Australia", "Fiji"]
  }

# Task: Use the dictionary to print the value of "Asia"
# Expected output:
# ["China", "Mongolia", "India"]

print(countries["Asia"])

countries.get("Asia")
print(countries.get("Asia"))

# Task: use the dictionary to print the third item in the value of "Australia"
# Expected output:
# "Fiji"

continent_list = countries["Australia"]
country_want= continent_list[2]
print(country_want)

print(countries["Australia"][2])

countries.get("Australia"[2])
print(countries.get("Australia")[2])

# Task: print a list of all the keys, in alphabetical order
# Expected output:
# ['Africa', 'Antarctica', 'Asia', 'Australia', 'Europe', 'North America',
# 'South America']

list = []

for key in countries:
    list.append(key)
    list.sort()
print(list)

# Problem 2
# Assign the following dictionary to a variable:

employee = {
  "first_name": "Wally",
  "last_name": "McCrea",
  "years_experience": 4,
  "role": "graphic designer"
}

# Use the dictionary keys and string interpolation to print out this string:
# "The candidate, Wally McCrea has
# 4 years of experience as a graphic designer."

fname = employee["first_name"]
lname = employee["last_name"]
years = employee["years_experience"]
r = employee["role"]

sentence = f"The candidate, {fname} {lname} has {years} years of experience as a {r}."

print(sentence)

# Problem 3
# Consider the following dictionary:

my_dict = {'a': 1, 'b': 2, 'c': 3}

# Task: Loop through the dictionary and create a new one where the values are the squares of the current values. Print the new dictionary.
# Expected output:
# {'a': 1, 'b': 4, 'c': 9}

# create a new dictionary
squares = {}

for key in my_dict:
    squares[key] = my_dict[key] ** 2

print(squares)

# Task: Write some code that prints a dictionary where the keys are the squares of the values and the values are the keys.
# Expected output:
# my_dict = {1: 'a', 4: 'b', 9: 'c'}
