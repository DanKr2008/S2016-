def safe_calculate(func):
    def wrapper(expression):
        try:
            result = func(expression)
            return result
        except Exception as e:
            return f"Помилка обчислення: {e}"
    return wrapper

class StudentSimulator:
    def __init__(self, name):
        self.name = name
        self.current_day = 0

    def __iter__(self):
        return self.generator()

    def generator(self):
        while self.current_day < 5:
            if self.current_day == 0:
                yield f"{self.name} прокрався першого дня на пари"
            elif self.current_day == 1:
                yield f"{self.name} дуже втомився і не пішов на пари"
            elif self.current_day == 2:
                yield f"{self.name} зробив декілька домашніх завдань"
            elif self.current_day == 3:
                yield f"{self.name} завершив тиждень успішно"
            self.current_day += 1

    @staticmethod
    def calculate(expression):
        return eval(expression)


student = StudentSimulator("Максим")


for day in student:
    print(day)


result1 = student.calculate("2 + 2")
print(result1)

result2 = student.calculate("10 / 0")
print(result2)