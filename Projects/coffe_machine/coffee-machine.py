espresso_d = {"water": 250, "beans": 16, "price": 4}
latte = {"water": 350, "milk": 75, "beans": 20, "price": 7}
cappuccino = {"water": 200, "milk": 100, "beans": 12, "price": 6}


class CoffeeMachine:
    # setup dicts containing static information on the quantities needed to make each drink.

    def __init__(self, water, milk, beans, money=None, cups=None):
        self.water = int(water)
        self.milk = int(milk)
        self.beans = int(beans)
        if money is None:
            self.money = 0
        else:
            self.money = int(money)

        if cups is None:
            self.cups = 0
        else:
            self.cups = int(cups)

    @staticmethod
    def getvalue(__dictionary, value):
        for k in __dictionary:
            if k in [value]:
                yield __dictionary[k]

    def cups_available(self, key):
        if key is "espresso":
            water = [n for n in CoffeeMachine.getvalue(espresso_d, "water")]
            beans = [n for n in CoffeeMachine.getvalue(espresso_d, "beans")]
            return min(self.water // water[0], self.beans // beans[0])
        elif key is "latte":
            water = [n for n in CoffeeMachine.getvalue(latte, "water")]
            milk = [n for n in CoffeeMachine.getvalue(latte, "milk")]
            beans = [n for n in CoffeeMachine.getvalue(latte, "beans")]
            return min([self.water // water[0], self.milk // milk[0], self.beans // beans[0]])
        elif key is "cappuccino":
            water = [n for n in CoffeeMachine.getvalue(cappuccino, "water")]
            milk = [n for n in CoffeeMachine.getvalue(cappuccino, "milk")]
            beans = [n for n in CoffeeMachine.getvalue(cappuccino, "beans")]
            return min([self.water // water[0], self.milk // milk[0], self.beans / beans[0]])

    def espresso(self, num_of_cups):
        self.water -= (espresso_d["water"] * num_of_cups)
        self.beans -= (espresso_d["beans"] * num_of_cups)
        self.money -= (espresso_d["price"] * num_of_cups)
        self.cups -= num_of_cups
        return

    def latte(self, num_of_cups):
        self.water -= (latte["water"] * num_of_cups)
        self.milk -= (latte["milk"] * num_of_cups)
        self.beans -= (latte["beans"] * num_of_cups)
        self.money -= (latte["price"] * num_of_cups)
        self.cups -= num_of_cups
        return

    def cappuccino(self, num_of_cups):
        self.water -= (cappuccino["water"] * num_of_cups)
        self.milk -= (cappuccino["milk"] * num_of_cups)
        self.beans -= (cappuccino["beans"] * num_of_cups)
        self.money -= (cappuccino["price"] * num_of_cups)
        self.cups -= num_of_cups
        return

    def print_contents(self):
        return f"The coffee machine has: \n", \
               "{0} of water \n".format(self.water), \
               "{0} of milk \n".format(self.milk), \
               "{0} of beans \n".format(self.beans), \
               "{0} of disposable cups \n".format(self.cups), \
               "{0} of money \n".format(self.money)

    def fill(self, water=None, milk=None, beans=None, cups=None):
        if water is not None:
            self.water += int(water)

        if milk is not None:
            self.milk += int(milk)

        if beans is not None:
            self.beans += int(beans)

        if cups is not None:
            self.cups += int(cups)

        return self.water, self.milk, self.beans, self.cups

    def buy(self, coffee, num_of_cups):
        desired_coffee = str(coffee)

        if desired_coffee == "espresso":
            if self.cups_available(coffee) == 0:
                self.print_contents()
            else:
                self.espresso(num_of_cups)
                self.print_contents()
        elif desired_coffee == "latte":
            if self.cups_available(coffee) == 0:
                self.print_contents()
            else:
                self.latte(num_of_cups)
                self.print_contents()

        elif desired_coffee == "cappuccino":
            if self.cups_available(coffee) == 0:
                self.print_contents()
            else:
                self.cappuccino(num_of_cups)
                self.print_contents()
        else:
            print("wrong coffee specified {0}, This machine can only provide, espresso, latte and cappuccino."
                  .format(desired_coffee))

    def take(self):
        earnings = self.money
        self.money -= earnings
        return earnings


if __name__ == '__main__':
    # initialize a coffee machine with the values below.
    test_1 = CoffeeMachine(500, 540, 120, 550, 9)
    # print out values after initializing the class above.
    print(test_1.water, test_1.milk, test_1.beans, test_1.money, test_1.cups)
    print(test_1.cups_available("espresso"))
    # buy two espressos
    test_1.buy("espresso", 2)
    # print out values after we have brought the correct quantity of items.
    print(test_1.water, test_1.milk, test_1.beans, test_1.money, test_1.cups)
    # take earnings from the coffee machine.
    print(test_1.take())
    # print out current earnings once we have taken them away.
    print(test_1.money)

