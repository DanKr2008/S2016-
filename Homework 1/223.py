import random


class Cat:
    def __init__(self, name):
        self.name = name
        self.hunger = 0
        self.boredom = 0

    def __str__(self):
        return f"{self.name}: Hunger={self.hunger}, Boredom={self.boredom}"

    def play(self):
        self.boredom -= 1
        print(f"{self.name} грає.")

    def eat(self):
        self.hunger -= 1
        print(f"{self.name} їсть.")

    def sleep(self):
        print(f"{self.name} спить.")
        self.hunger += 1
        self.boredom += 1

    def check_status(self):
        if self.hunger <= 0:
            self.hunger = 0
        if self.boredom <= 0:
            self.boredom = 0

        if self.hunger >= 5:
            print(f"{self.name} хоче їсти!")
        if self.boredom >= 5:
            print(f"{self.name} хоче гратись!")

    def live(self):
        while True:
            action = random.choice(["play", "eat", "sleep"])
            if action == "play":
                self.play()
            elif action == "eat":
                self.eat()
            else:
                self.sleep()

            self.hunger += 1
            self.boredom += 1
            self.check_status()


if __name__ == "__main__":
    cat = Cat("Мурзик")
    cat.live()