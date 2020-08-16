"""
# this coffee machine was developed by Gary louis stewart for the jetbrains academy python developer track.
# gary.stewart@outlook.com
# uses pep8 styling
"""


class Coffee:
    def __init__(self, water, milk, beans, cost):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cost = cost


class CoffeeType:
    espresso = Coffee(250, 0, 16, 4)
    latte = Coffee(350, 75, 20, 7)
    cappuccino = Coffee(200, 100, 12, 6)


class MachineResources:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550

    def make_cup_of_coffee(self, coffee):
        response = "Sorry, not enough {0}!"
        water = self.water - coffee.water
        milk = self.milk - coffee.milk
        beans = self.beans - coffee.beans
        cups = self.cups - 1

        if water < 0:
            print(response.format("water"))
        elif milk < 0:
            print(response.format("milk"))
        elif beans < 0:
            print(response.format("beans"))
        elif cups < 0:
            print(response.format("cups"))
        else:
            print("I have enough resources, making you a coffee!")
            self.water = water
            self.milk = milk
            self.beans = beans
            self.cups = cups
            self.money += coffee.cost

    def make_coffee(self):
        choice = input("What do you want to buy? 1 - "
                       "espresso, 2 - latte, 3 - cappuccino, back - return to main menu.")
        if choice == "1":
            self.make_cup_of_coffee(CoffeeType.espresso)
        elif choice == "2":
            self.make_cup_of_coffee(CoffeeType.latte)
        elif choice == "3":
            self.make_cup_of_coffee(CoffeeType.cappuccino)

    def resources_remaining(self):
        print(f"The coffee machine has \n" +
              f"{self.water} of water \n" +
              f"{self.milk} of milk \n" +
              f"{self.beans} of beans \n" +
              f"{self.cups} of cups \n" +
              f"${self.money} of money \n")

    def fill(self):
        response = "Write how many {0} of {1} do you want to add"
        self.water += int(input(response.format("ml", "water")))
        self.milk += int(input(response.format("ml", "milk")))
        self.beans += int(input(response.format("g", "beans")))
        self.cups += int(input(response.format("disposable cups", "coffee")))

    def take(self):
        print(f"I just gave you ${self.money}")
        self.money = 0


class CoffeeMachine:
    def __init__(self):
        self.cup_of_coffee = CoffeeType()
        self.resources = MachineResources()
        self.needed_cups = 0
        self.cups_affordable = 0
        self.run_coffee_machine()

    def run_coffee_machine(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit): \n")

            if action == "buy":
                self.resources.make_coffee()
            elif action == "fill":
                self.resources.fill()
            elif action == "take":
                self.resources.take()
            elif action == "remaining":
                self.resources.resources_remaining()
            elif action == "exit":
                break


machine = CoffeeMachine()

