import random
# Array of all lowercase letters
lowercase_letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ,'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]


# Array of numbers as strings
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Array of common symbols
symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
    '{', '}', '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/', '\\', '|', '~', '`'
]

user_lowChars = 0
user_capChars = 0
user_numbers = 0
user_symbols = 0

print("**************************** PASS MAKER *************************")
print("****************************____________*************************")
print("")
user_lowChars = int(input("Enter number of chars in the pass: "))
user_numbers = int(input("Enter number of numbers in the pass: "))
user_symbols = int(input("Enter number of Symbols in the pass: "))

password = [];
for i in range(1 , user_lowChars+1):
    password.append(lowercase_letters[random.randint(0,len(lowercase_letters) -1)])
for i in range(1 , user_numbers+1):
    password.append(numbers[random.randint(0,len(numbers) -1)])
for i in range(1 , user_symbols+1):
    password.append(symbols[random.randint(0,len(symbols) -1)])

print(password)
final_pass_array = []
for i in password:
    final_pass_array.append(" ");

print("____________")
final_pass = []
for i in range(0 , 1000):
    nRand = random.randint(0 , len(password) -1)
    nRand2 = random.randint(0 , len(password) -1)
    for i in range(0 , len(password)):
        if final_pass_array[nRand] == " " and password[nRand2] != " ":
            final_pass_array[nRand] = password[nRand2]
            password[nRand2] = " ";
        else: 
            break;
passSTR = ""
for i in final_pass_array:
    passSTR += i
print(final_pass_array)
print(passSTR)