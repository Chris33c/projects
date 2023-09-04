"""

Author: Chris Cox
Program: Phone Numbers
Date: 2/11/2023
input: This program takes the user input of a last name or first and last name 
output: returns the phone number associated with that name. Returns error if no name is found.

"""
search = input("Enter a last name, or a first and last name. Press '.' when finished: ")
#check for alpha characters, throw error if not. Code still produces print statement even if search is alpha.  Need to fix.
#check for length of search
while True:    
    lowercase = search.lower()
    search = lowercase.split()
 #code does not execute if search is alpha.  Need to fix.
    if len(search) == 1:
        first_name = ""
        last_name = search[0]
    if len(search) > 1 and len(search) <= 2:
        first_name = search[0] + " "
        last_name = search[1]
    elif len(search) >= 2:
        print("Error.  You may only enter one name")
    #for loop through phones variable matching first name and last name with search or just last name
    PhoneNumbers = open('phones.txt', 'r')
    found_person = False
    numbers = PhoneNumbers.readlines()
    while True:
        numbers = numbers.strip('\n')
        numbers = numbers.lower()
        NameSearch = numbers.find(last_name)
        if numbers == "":
            break
    if NameSearch == True:
        " ".join(numbers)
        numbers = numbers.strip([NameSearch])
        print(numbers)
    else:
        print("Name not found. Please try again")
    if first_name + last_name in numbers:
            #return slice after first space
        print(numbers,numbers[-1:10])
        found_person = True
    if not found_person:
        print("Name not found. Please try again")
        #prompt user to enter another name, exit while loop when user enters '.'
    search = input("Enter a last name, or a first and last name. Press '.' when finished: ")
    if search ==  "":
        break
print("Goodbye!")    