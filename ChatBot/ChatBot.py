# chatbot.py

import datetime

# Отримання поточного року
current_year = datetime.datetime.now().year

# Виведення привітання
print(f"Hello! My name is DICT_Bot.")
print(f"I was created in {current_year}.")

# Запитання про ім'я користувача
print("Please, remind me your name.")

# Зчитування ім'я користувача зі стандартного введення
user_name = input()

# Привітання користувача за ім'ям
print(f"What a great name you have, {user_name}!")

# Запитання та вгадування віку
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")

# Зчитування залишків від ділення на 3, 5 та 7
remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())

# Визначення віку за формулою
your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

# Виведення віку та привітання з програмуванням
print(f"Your age is {your_age}; that's a good time to start programming!")

# Запитання про лічильник
print("Now I will prove to you that I can count to any number you want.")

# Зчитування числа від користувача
num = int(input())

# Виведення лічильника від 0 до введеного числа
for i in range(num + 1):
    print(f"{i} !")

# Перевірка знань програмування
print("Let's test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")

# Очікування правильної відповіді від користувача
while True:
    answer = input("> ")
    if answer == "2":
        break
    else:
        print("Please, try again.")

# Завершення повідомлення
print("Completed, have a nice day!")
print("Congratulations, have a nice day!")
