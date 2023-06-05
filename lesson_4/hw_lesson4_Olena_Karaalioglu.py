class Human:
    favorite_drink = "beer"

    def __init__(self,age:int):
        self.age = age
        if age <= 18:
            self.favorite_drink = 'juice'

    def drink (self):
        print(f'{self.__class__.__name__} who is {self.age} years old, likes to drink {self.favorite_drink} ')

class Worker(Human):
    def __init__(self, age, salary):
        super().__init__(age)
        if salary >= 1000 and age >= 18:
            self.favorite_drink = "whiskey"

print(Human.favorite_drink)
Human(10).drink()
Human(25).drink()

Worker(30,500).drink()
Worker(12,400).drink()
Worker(19,2000).drink()
Worker(22,500).drink()
