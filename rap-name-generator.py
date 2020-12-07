# Guided Exploration No. 3
# Connor McCutcheon


# import the random library
import random

# create an empty list named possible_names
possible_names = []
# create and/or open a file to output to
outputFile = open('rap-names-output.txt', 'w')

# opens rap-names.txt and assigns it to variable dataFile
with open('rap-names.txt', 'r') as dataFile:
    # loop that goes through each line of the file
    for name in dataFile:
        # appends a name from each line to the possible_names list and removes the line feed
        possible_names.append(name.rstrip())

# asks how many names to create
count = int(input('How many rap names would you like to create? '))
# asks how many parts each one should have
parts = int(input('How many parts should the name contain? '))

# loops however many times count was set to
for i in range(count):
    # creates an empty list named name_parts
    name_parts = []
    # loops however many times parts was set to
    for j in range(parts):
        # appends a random name from possible_names to name_parts using a range of random numbers as long as the possible_names list
        name_parts.append(possible_names[random.randint(0, len(possible_names)-1)])
    # writes the name to the output file + a new line
    outputFile.write(f"{' '.join(name_parts)}\n")
    # prints the name that was just generated
    print(f"{' '.join(name_parts)}")

# closes the file
outputFile.close()
