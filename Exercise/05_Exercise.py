class Person:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))
        self.city = input("Enter your city: ")

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I live in {self.city}.")

# उदाहरणको लागि
person1 = Person()
person1.introduce()
