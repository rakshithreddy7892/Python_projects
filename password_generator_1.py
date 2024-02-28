#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

x=[0,1,2]
password=''
n=nr_letters + nr_symbols + nr_numbers
for i in range(n):
    choice= random.choice(x)
    if choice == 0:
        password+=random.choice(letters)
        nr_letters-=1
        if nr_letters==0:
            x.remove(0)
    elif choice == 1:
        password+=random.choice(numbers)
        nr_numbers-=1
        if nr_numbers==0:
            x.remove(1)

    elif choice == 2:
        password+=random.choice(symbols)
        nr_symbols-=1
        if nr_symbols==0:
            x.remove(2)

print(f"Your password is: {password}")