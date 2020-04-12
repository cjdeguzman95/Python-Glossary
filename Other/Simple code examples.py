from random import randrange
import pyodbc

# Palindrome function uses slicing and control flow statements to find define palindromes in a given list
def palindrome():
    words = ["mum", "bee", "holiday", "hannah"]

    for word in words:
        reversed_word = word[::-1]
        if word == reversed_word:
            return "is palindrome"
        else:
            return "is not a palindrome"


# Function that checks largest number from user input using IF statements
def largest_number(n1, n2, n3):
    n1 = input("Give me a number: ")
    n2 = input("Give me a second number: ")
    n3 = input("Give me a third number: ")

    if n1 > n2 and n3:
        return "The first number, {}, is the largest".format(n1)
    elif n2 > n1 and n3:
        return "The second number, {}, is the largest".format(n2)
    else:
        return "The third number, {}, is the largest".format(n3)


# Uses modulus to sort range of values into evens and odds - creates and returns sorted lists
numbers = range(20)
even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print(even_numbers, odd_numbers)


# while loop and random library
TRY = 3
target = randrange(10)

while TRY != 0:
    guess = input("Guess what number I'm thinking: ")
    if guess != target:
        print("Wrong number")
        TRY -= 1
    else:
        print("Congratulations! That's correct!")
        break
else:
    print("Sorry. You're out of guesses!")

# connecting to MSSQL via the PYODBC module
# lists the total orders for each product - only displays products that have orders
server = "localhost,1433"
database = "Northwind"
username = "SA"
password = "Passw0rd2018"

docker_Northwind = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';'
                                  'UID='+username+';PWD='+ password)

cursor = docker_Northwind.cursor()

orders = cursor.execute("SELECT ProductName, SUM(UnitsOnOrder) AS 'Total' FROM Products GROUP BY ProductName HAVING SUM(UnitsOnOrder) > 0 ORDER BY 'Total' DESC;").fetchall()
for x in orders:
    print(x.ProductName, x.Total)

# nested dictionaries - fortune teller game
fortune = {
    "red": {
        "fortune one": "You will meet someone special this week!",
        "fortune two": "You have a secret admirer!"
    },
    "green": {
        "fortune three": "Now is a good time to invest in some stocks!",
        "fortune four": "Be careful how you spend your money this week - you are set to lose a lot!"
    },
    "blue": {
        "fortune five": "Don't worry, failure is the chance to do better next time!",
        "fortune six": "You will receive great feedback this week!"
    },
    "yellow": {
        "fortune seven": "Check in on your friends this week, they are missing you!",
        "fortune eight": "Remember to share good fortune as well as bad with your friends!"
    }
}

running = True
name = input("Tell me your name and let me tell you your fortune: ")
print("Hi {}, what do you want to know about?".format(name))
print("Choose a colour:\nRed for Love\nGreen for Money\nBlue for Work \nYellow for Friendship")
colour = input()

while running:
    try:
        chosen_number = int(input("Now choose either 1 or 2: "))
    except ValueError:
        print("{}, please insert a numeric character!".format(name.capitalize()))
    else:
        if chosen_number < 1 or chosen_number > 2:
            print("You can only choose 1 or 2 {}! Try again.".format(name.capitalize()))
        else:
            for colour in fortune:
                if colour.lower() == "red":
                    if chosen_number == 1:
                        print(fortune["red"].get("fortune one"))
                    else:
                        print(fortune["red"].get("fortune two"))
                    break
                elif colour.lower() == "green":
                    if chosen_number == 1:
                        print(fortune["green"].get("fortune three"))
                    else:
                        print(fortune["green"].get("fortune four"))
                    break
                elif colour.lower() == "blue":
                    if chosen_number == 1:
                        print(fortune["blue"].get("fortune five"))
                    else:
                        print(fortune["blue"].get("fortune six"))
                    break
                elif colour == "yellow":
                    if chosen_number == 1:
                        print(fortune["yellow"].get("fortune seven"))
                    else:
                        print(fortune["yellow"].get("fortune eight"))
                    break
            running = False