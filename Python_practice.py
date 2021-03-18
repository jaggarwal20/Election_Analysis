# counties = ["Arapahoe","Denver", "Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# # if-else statement
# temperature = int(input("What is the temperature outside?"))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the window.")

# # nested-if 

# # What is the score?
# score = int(input("What is the score?"))

# #Determine the grade
# if score >= 90:
#     print('Your grade is an A')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
#     print('Your grade is a D.')
# else: print('Your grade is an F.')

# in and not in
counties = ["Arapahoe","Denver", "Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

#for loops
for county in counties:
    print(county)

#range()
for number in range(5):
    print(number)

for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe":422829,"Denver":463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(county)

for county, voters in counties_dict.items():
    print(county, voters)