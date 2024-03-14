class Pet():
    name = None
    fullness = 0

    def __init__(self, name):
        self.name = name


    def eat(self, food):
        print(self.name + " is eating " + food + "...")
        if food == "caesium":
            self.fullness = self.fullness + 45
        elif food == "plutonium-239":
            self.fullness = self.fullness - 30
        elif food == "grass":
            self.fullness = self.fullness + 1
        elif food == "hdmi cable":
            self.fullness = self.fullness + 12
        elif food == "baby":
            self.fullness = self.fullness + 85


        print(self.name + " is now " + str(self.fullness) + "% full")
        if self.fullness < 50:
            print(self.name, " starved.")


pet_owner_name = input("What is your name?")
print("Welcome, ", pet_owner_name)

pet_1 = Pet("Gabby")
pet_1.eat("caesium")


# Caesium = 50 fullness
# Plutonium-239 = -30 fullness
# Grass = 1 fullness
# hdmi cable = 12 fullness
# baby = 85 fullness
