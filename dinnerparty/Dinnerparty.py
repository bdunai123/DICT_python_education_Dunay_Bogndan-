import random

def split_expenses(friends_expenses, total_amount):
    # Перевірити коректність введеної кількості людей
    if len(friends_expenses) == 0:
        print("No one is joining for the party")
        return

    # Зчитати загальний рахунок
    total_amount = float(input("Enter the total amount:\n"))

    # Розділити суму порівну між усіма
    amount_per_person = round(total_amount / len(friends_expenses), 2)

    # Оновити значення у словнику
    for friend in friends_expenses:
        friends_expenses[friend] = amount_per_person

    # Запитати користувача, чи хоче він вибрати "щасливчика"
    lucky_choice = input("Do you want to use the 'Who is lucky?' feature? Write Yes/No:\n").lower()

    # Вибрати випадкове ім'я та вивести результат
    if lucky_choice == "yes":
        lucky_person = random.choice(list(friends_expenses.keys()))
        print(f"{lucky_person} is the lucky one!")
        friends_expenses[lucky_person] = 0

        # Перерахувати суму для інших друзів
        remaining_people = len(friends_expenses) - 1
        amount_per_person = round(total_amount / remaining_people, 2)

        for friend in friends_expenses:
            if friend != lucky_person:
                friends_expenses[friend] = amount_per_person

    # Вивести оновлений словник
    print(friends_expenses)

def main():
    # Ініціалізувати словник для зберігання імен та сум грошей кожного друга
    friends_expenses = {}

    # Зчитати кількість людей, які беруть участь у вечері
    num_of_friends = int(input("Enter the number of friends joining (including you):\n"))

    # Перевірити коректність введеної кількості людей
    if num_of_friends <= 0:
        print("No one is joining for the party")
        return

    # Зчитати імена друзів та ініціалізувати словник
    print("Enter the name of every friend (including you), each on a new line:")
    for _ in range(num_of_friends):
        friend_name = input("> ")
        friends_expenses[friend_name] = 0

    # Викликати функцію розділу витрат
    split_expenses(friends_expenses, 0)

if __name__ == "__main__":
    main()
