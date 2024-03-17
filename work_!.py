#Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.

input_list = []
for x in range(5):
    value = int(input("Enter your number: "))
    input_list.append(value)

Summ = sum(input_list)
print(f"The sum of your numbers list is: {Summ}")

#Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.

book_list = []

for x in range(6):
    book = str(input("Enter your favourite books: "))
    book_list.append(book)
    book_tuple = tuple(book_list)

print(book_tuple)

for book in book_tuple:
    print(f"\t{book}\n")

#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.

people = {}

people["name"] = str(input("Enter your name: "))
people["age"] = str(input("Enter your age: "))
people["color"] = str(input("Enter your favourite color: "))

for k,v in people.items():
    print(f"{k}: {v}")

#Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.

set_1 = set()
set_2 = set()
for x in range(3):
    value = int(input("Enter your number: "))
    set_1.add(value)

for x in range(3):
    value = int(input("Enter your number: "))
    set_2.add(value)

print(set_1)
print(set_2)

set_3 = set_1.union(set_2)
print(set_3)

#Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.

word_list = []
for i in range(5):
    word = str(input("Enter your word: "))
    word_list.append(word)

odd_word_list = [word for word in word_list if len(word) % 2 == 1]
