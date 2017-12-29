from parts import *


class CarRepair:

    def __init__(self):
        self.part = input("What part do you need?: ")
        self.cost = parts.get(self.part)
        self.labor = 1.75

    # this gets the part and cost from dictionary

    def parts_cost(self):

        if self.part in parts:
            print("The %s will cost $%i to order." % (self.part, parts.get(self.part)))

        else:
            print("We don't have that item in stock")

    def estimate(self):

        print("Your estimate for the repair of the %s will be $%.2f." % (self.part, float(self.cost * self.labor)))

