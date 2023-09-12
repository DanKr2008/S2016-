import requests
import re
import datetime


# Функція для отримання курсу долара
def get_dollar_rate():
    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&json"
    response = requests.get(url)
    data = response.json()
    return data[0]['rate']


# Запит у користувача для вибору опції
while True:
    option = input(
        "Виберіть необхідну опцію (1 - купівля валюти у NBU, 2 - дізнатися про температуру повітря у Києві): ")

    if option == '1' or option == '2':
        break
    else:
        print("Будь ласка, введіть 1 або 2.")

if option == '1':
    hrn_amount = float(input("Введіть суму у гривнях: "))
    dollar_rate = get_dollar_rate()

    if dollar_rate:
        result = hrn_amount / dollar_rate

        # Збереження в базу даних (ви можете використати SQLite або будь-яку іншу БД)
        # Наприклад, якщо ви використовуєте SQLite:
        import sqlite3

        conn = sqlite3.connect('converter.db')
        c = conn.cursor()

        c.execute("INSERT INTO money (id, currency, hrn, result) VALUES (?, ?, ?, ?)",
                  (1, dollar_rate, hrn_amount, result))

        conn.commit()
        conn.close()

        print(f"Збережено в базу даних: {1}, {dollar_rate}, {hrn_amount}, {result}")

    else:
        print("Не вдалося отримати курс долара.")

elif option == '2':
    # Отримання температури повітря у Києві
    response = requests.get("https://www.metoffice.gov.uk/weather/forecast/gcvwr3zrw#?date=2023-09-12")
    content = response.text
    match = re.search(r'<span class="temperature-value">([\d.]+)</span>', content)

    if match:
        temperature = match.group(1)

        # Збереження в базу даних (ви можете використати SQLite або будь-яку іншу БД)
        # Наприклад, якщо ви використовуєте SQLite:
        import sqlite3

        conn = sqlite3.connect('converter.db')
        c = conn.cursor()

        current_date = datetime.datetime.now().strftime('%d.%m')
        c.execute("INSERT INTO weather (id, date, result) VALUES (?, ?, ?)",
                  (1, current_date, temperature))

        conn.commit()
        conn.close()

        print(f"Збережено в базу даних: {1}, {current_date}, {temperature}")

    else:
        print("Не вдалося отримати температуру повітря.")
