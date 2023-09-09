import requests as rclass
import sqlite3
from datetime import datetime
import time


class ParseHtml:
    def __init__(self, url, db_path):
        self.Counter = 0
        self.Url = url
        self.DbPath = db_path
        self.Result = {}

    def get_temperature(self):
        response = rclass.get(self.Url)
        response_text = response.text
        start_index = response_text.find('data-testid="TemperatureValue">') + len('data-testid="TemperatureValue">')
        end_index = response_text.find('<', start_index)
        temperature = response_text[start_index:end_index]

        if any(char.isdigit() for char in temperature) and '°' in temperature:
            return temperature.strip()[:-1]
        else:
            return None

    def insert_data(self, datetime, temperature):
        conn = sqlite3.connect(self.DbPath)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO weather_data (date_time, temperature) VALUES (?, ?)", (datetime, temperature))
        conn.commit()
        conn.close()

    def fetch_data(self):
        try:
            temperature = self.get_temperature()

            if temperature is not None:
                current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.insert_data(current_datetime, temperature)
                print(f"Додано дані: {current_datetime}, Температура: {temperature}°C")
            else:
                print("Failed to fetch temperature data.")
        except Exception as e:
            print(f"Сталася помилка: {e}")


        time.sleep(1800)
        self.fetch_data()


def main():
    url = "https://www.metoffice.gov.uk/weather/forecast/gcvwr3zrw#?date=2023-09-09"
    db_path = "weather_data.db"
    parser = ParseHtml(url, db_path)
    parser.fetch_data()


if __name__ == "__main__":
    main()