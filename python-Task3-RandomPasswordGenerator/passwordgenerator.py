import random
import string

while True:
    try:
        length = int(
            input("Enter length of wanted password(minimum 8 characters required) : ")
        )
        if length < 8:
            print("Password length must be at least 8.")
        else:
            break
    except ValueError:
        print("enter valid number not alphabet ")

print("Enter a character type which you want to include in your password ")
while True:
    yes = 0
    print("at least 2 types must be selected")
    upper_case = input("upper_case (y/n) : ").lower()
    while upper_case not in ["y", "n"]:
        print("Invalid input.")
        upper_case = input("upper_case (y/n) : ").lower()

    if upper_case == "y":
        yes += 1
    lower_case = input("lower_case (y/n) : ").lower()
    while lower_case not in ["y", "n"]:
        print("Invalid input.")
        lower_case = input("lower_case (y/n) : ").lower()
    if lower_case == "y":
        yes += 1

    numbers = input("numbers (y/n) : ").lower()
    while numbers not in ["y", "n"]:
        print("Invalid input.")
        numbers = input("numbers (y/n) : ").lower()
    if numbers == "y":
        yes += 1

    symbols = input("symbols (y/n) : ").lower()
    while symbols not in ["y", "n"]:
        print("Invalid input.")
        symbols = input("symbols (y/n) : ").lower()
    if symbols== "y":
        yes += 1

    if yes>=2:
        break
    else:
        print("choose at lest 2 character type")

character_pool=""
if upper_case == "y":
    character_pool+=string.ascii_uppercase
if lower_case == "y":
    character_pool += string.ascii_lowercase
if numbers == "y":
    character_pool += string.digits
if symbols == "y":
    character_pool += string.punctuation

while True:
   generated_password=""
   for i in range(0,length):
      choice = random.choice(character_pool)
      generated_password+=choice
   print(generated_password)
   repeat=input("if you want to generate another passwor  type \"yes\" if not then type \"no\" ").lower()
   while repeat not in ["yes","no"]:
      print("Enter valid input")
      repeat=input("if you want to generate another passwor  type \"yes\" if not then type \"no\" ").lower()
   if repeat=="no":
      print("Thank you")
      break
