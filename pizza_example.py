# Define the Product class (Pizza)
class Pizza:
    def __init__(self):
        self.size = ""
        self.toppings = []
        self.options = []

# Define the abstract Builder class (PizzaBuilder)
from abc import ABC, abstractmethod

class PizzaBuilder(ABC):
    @abstractmethod
    def setPizzaSize(self, size):
        pass

    @abstractmethod
    def addTopping(self, topping):
        pass

    @abstractmethod
    def addOption(self, option):
        pass

    @abstractmethod
    def getPizza(self):
        pass

# Define ConcreteBuilder classes
class MediumPepperoniPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def setPizzaSize(self):
        self.pizza.size = "Medium"

    def addTopping(self):
        self.pizza.toppings.append("Pepperoni")

    def getPizza(self):
        return self.pizza
# ... Define more ConcreteBuilder classes

# Define Director class (PizzaDirector)
class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def constructPizza(self):
        self.builder.setPizzaSize("Medium")
        self.builder.addTopping("Pepperoni")

# Usage
builder = MediumPepperoniPizzaBuilder()
director = PizzaDirector(builder)
director.constructPizza()
pizza = builder.getPizza()
print(f"Size: {pizza.size}")
print("Toppings:", ", ".join(pizza.toppings))

