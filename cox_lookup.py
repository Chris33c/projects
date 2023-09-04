"""
Author: Chris Cox
Date: 2/23/2023
Program: This program formats a text file containing addresses and phone numbers. It then takes a user input and returns the respective information.
"""
#address book declared as empty dictionary and is global
address_book = {}
def ReadFile():
    try:
        with open("address.txt", 'r') as f:
            for line in f:
                line = line.strip('\n')
                line = line.split(',')
                #remove everythign after first index, assign to name
                name = line[0].strip()
                #Mutate to remove name from list and then join the rest of the list
                #assign to address
                line.remove(name)
                name = name.lower()
                #rejoin the list with commas to keep original formatting. This was needed to format the list later.
                address = ','.join(line)
                address_book[name] = address
        #remove extra whitespace from address
        return address_book
    except FileNotFoundError:
        print("File not found")
        exit()

def FormatFile(address_book, name, user_input=1):
    try:
        if user_input == 1:
            Lookup = address_book.get(name)
            Lookup = Lookup.split(',')
            Phone_Number = Lookup[-1]
            print("Phone Number: ", Phone_Number)
    except AttributeError:
        print("Name not found")
        return
    try:
        if user_input == 2:
            Lookup = address_book.get(name)
            #split the list at the commas
            #with list properly formatted we can easily assign each index to a variable
            Lookup = Lookup.split(',')
            Address = Lookup[0]
            City = Lookup[1]
            State = Lookup[2]
            Zip = Lookup[3]
            print("Address: ", Address)
            print("City: ", City)
            print("State: ", State)
            print("Zip: ", Zip)
    except AttributeError:
        print("Name not found")
        #can use function to format output or have to split and reassign at index?
        #would be nice to have a function that takes in a list and formats it
          
def main():
    #the following takes the address_book dictionary and formats it
    #the readfile() is assigned to a variable
    #the program prompts the user for input, and will break if enter is pressed
    try:
        user_input = int(input("Lookup (1) for phone numbers, (2) for addresses: "))
    except ValueError:
            print("Invalid input")
    while True:
        address_book = ReadFile()
        try:
            name = input("Enter space seperated first and last name. Press Enter to quit: ")
        except ValueError:
            print("That is not a valid name. Please try again.")
            continue
        #format name to lowercase to handle case sensitivity
        if name == "":
            print("Goodbye")
            break
        name = name.lower()
        FormatFile(address_book, name, user_input)

        #address book is assigned to argument 1, name is assigned to argument 2, and user_input is assigned to optional argument




main()