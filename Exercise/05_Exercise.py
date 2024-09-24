class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I live in {self.city}.")

# उदाहरणको लागि
person1 = Person("Ram", 25, "Kathmandu")
person1.introduce()
