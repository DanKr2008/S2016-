from random import random


class Student:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    def work(self):
        self.money += 100
        print(f"{self.name} працює і заробляє гроші.")

    def relax(self):
        if self.money >= 50:
            self.money -= 50
            print(f"{self.name} відпочиває і витрачає гроші.")
        else:
            print(f"{self.name} не має достатньо грошей для відпочинку.")

    def study(self):
        if self.money >= 200:
            self.money -= 200
            print(f"{self.name} вчиться і витрачає гроші на навчання.")
        else:
            print(f"{self.name} не має достатньо грошей для навчання.")

    def change_behavior(self):
        if self.money < 100:
            print(f"{self.name} пішов на роботу, бо не має достатньо грошей.")
            self.work()
        elif self.money > 500:
            print(f"{self.name} змінив пріоритети і більше вчиться.")
            self.study()
        else:
            print(f"{self.name} продовжує звичну поведінку.")

    def live_one_year(self):
        for _ in range(365):
            action = random.choice(['work', 'relax', 'study', 'change_behavior'])
            if action == 'work':
                self.work()
            elif action == 'relax':
                self.relax()
            elif action == 'study':
                self.study()
            elif action == 'change_behavior':
                self.change_behavior()
            print(f"{self.name} має {self.money} грошей.")

