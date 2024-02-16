#Password Generator Project
import random

#create lists of letters, both capital letters and lower case
#lists of numbers
#and a list of symbols usually accepted by most online accounts
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#introduce user to generator
print("Welcome to the PyPassword Generator!")

#create variable for letters, symbols and numbers and store how many of each the user wants
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#create a variable to store the combination of the letters symbols and numbers
password = ("")


#for numbers in range 1 to the users preference, use the random.choice function to pick a random letter and add to the password variable
for number_of_letters in range(1,(nr_letters + 1)):
    password += random.choice(letters)

#for numbers in range 1 to the users preference, use the random.choice function to pick a random symbol and add to the password variable
for number_of_symbols in range(1,(nr_symbols + 1)):
    password += random.choice(symbols) 

#for numbers in range 1 to the users preference, use the random.choice function to pick a random number and add to the password variable
for number_of_number in range(1,(nr_numbers + 1)):
    password += random.choice(numbers)


#convert the easy mode password into a list of seperate characters.
password_list = list(password)

#create a variable that the final password will be stored in
random_password = ("")

#shuffle the list, to create a random order to the numbers, symbols and letters.
random.shuffle(password_list)

#for loop to take the characters out of the list again to form the password 

for i in password_list:
    #add the characters to the variabel random password to form the final password
    random_password += i

#print the final password for the user
print (f" Your random password is {random_password}")

