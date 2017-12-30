from parts import part


class CarRepair:

    def __init__(self):
        self.part = input("What part do you need?: ")
        self.part = self.part.capitalize()
        self.cost = part.get(self.part)
        self.labor = 1.75

    # this gets the part and cost from dictionary

    def parts_cost(self):
        if self.part in part:
            print(f"The {self.part} will cost ${self.cost} to order.")

        else:
            print("We don't have that item in stock")

    def estimate(self):

        print("Your estimate for the repair of the %s will be $%.2f." % (self.part, float(self.cost * self.labor)))


Acura = CarRepair()
Acura.parts_cost()
Acura.estimate()
