# Parent Class
class Superhero:
    def __init__(self, name, power, city):
        self.name = name
        self.power = power
        self.city = city

    def introduce(self):
        print(f"I am {self.name}, I protect {self.city} with my {self.power}!")

    def save_the_day(self):
        print(f"{self.name} is saving the day with {self.power}!")

# Subclass using Inheritance and Polymorphism
class FlyingSuperhero(Superhero):
    def fly(self):
        print(f"{self.name} is flying high over {self.city}!")

    # Polymorphic method override
    def save_the_day(self):
        print(f"{self.name} swoops down from the sky and saves {self.city} with {self.power}!")

# Creating objects
hero1 = Superhero("Megamind", "amazing intellect", "Metro City")
hero2 = FlyingSuperhero("Metroman", "laser vision", "Metro City")

# Demonstrating Polymorphism
superheroes = [hero1, hero2]
for hero in superheroes:
    hero.introduce()
    hero.save_the_day()

# Extra: Flying Superhero Specific ability
hero2.fly()
