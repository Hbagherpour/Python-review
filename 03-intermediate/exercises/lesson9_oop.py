#Exersise 1: Basic class: Create a Stock class with __init__(self, ticker, price, shares), a method position_value() returning price * shares, and a __str__ method that prints like: "AAPL: 10 shares @ $227.35".
#Create two instances and print both.


class Stock:
    def __init__(self, ticker, price, shares):
        self.ticker = ticker
        self.price = price
        self.shares = shares

    def position_value(self):
        return self.price * self.shares

    def __str__(self):
        return f"{self.ticker}: {self.shares} shares @ ${self.price:.2f}"


stock1 = Stock("AAPL", 227.35, 10)
stock2 = Stock("GOOGL", 2750.00, 5)

print(stock1)
print(stock2)

#Exercise 2: Method that mutates state: Add a method update_price(self, new_price) to your Stock class that updates self.price.
#Create an instance, print its value before and after calling update_price.

class Stock:
    def __init__(self, ticker, price, shares):
        self.ticker = ticker
        self.price = price
        self.shares = shares

    def position_value(self):
        return self.price * self.shares

    def update_price(self, new_price):
        self.price = new_price

    def __str__(self):
        return f"{self.ticker}: {self.shares} shares @ ${self.price:.2f}"

stock1 = Stock("AAPL", 227.35, 10)
print(stock1)

stock1.update_price(230.00)
print(stock1)

#Exercise 3: Class attribute: Add a class attribute exchange = "NASDAQ" to Stock.
#reate two instances and print .exchange on both, proving they share the same value without you setting it individually.

class Stock:
    exchange = "NASDAQ"

    def __init__(self, ticker, price, shares):
        self.ticker = ticker
        self.price = price
        self.shares = shares

    def position_value(self):
        return self.price * self.shares

    def update_price(self, new_price):
        self.price = new_price

    def __str__(self):
        return f"{self.ticker}: {self.shares} shares @ ${self.price:.2f}"   


stock1 = Stock("AAPL", 227.35, 10)
stock2 = Stock("GOOGL", 2750.00, 5)

print(stock1.exchange)
print(stock2.exchange)

#Exercise 4: Inheritance: Create a base class Asset with __init__(self, name, price) and a method describe() returning f"{self.name}: ${self.price:.2f}".
#Make Stock inherit from Asset using super().__init__(), keeping its own shares attribute and position_value() method.
#Create a Stock instance and call both describe() (inherited) and position_value() (its own).

class Asset:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        return f"{self.name}: ${self.price:.2f}"

class Stock(Asset):
    def __init__(self, ticker, price, shares):
        super().__init__(ticker, price)
        self.shares = shares

    def position_value(self):
        return self.price * self.shares

stock1 = Stock("AAPL", 227.35, 10)
print(stock1.describe())
print(f"Position value: ${stock1.position_value():.2f}")

#Exercise 5: Encapsulation practice: Create a Portfolio class with an internal _holdings list (starts empty).
#Add a method add_stock(self, stock) that appends a Stock instance to _holdings, and a method total_value(self) that loops through _holdings and sums up each stock's position_value().
#Test it by adding 2-3 stocks and printing the total.

class Asset:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        return f"{self.name}: ${self.price:.2f}"

class Stock(Asset):
    def __init__(self, ticker, price, shares):
        super().__init__(ticker, price)
        self.shares = shares

    def position_value(self):
        return self.price * self.shares

    def __str__(self):
        return self.describe() + f", {self.shares} shares"

    def __repr__(self):
        return self.__str__()

class Portfolio:
    def __init__(self):
        self._holdings = []

    def add_stock(self, stock):
        self._holdings.append(stock)

    def total_value(self):
        return sum(stock.position_value() for stock in self._holdings)

#Test the Portfolio class
portfolio = Portfolio()
print(f"Total portfolio value: ${portfolio.total_value():.2f}") 
stock1 = Stock("AAPL", 227.35, 10)
portfolio.add_stock(stock1)
print(portfolio._holdings)
print(f"Total portfolio value: ${portfolio.total_value():.2f}")
stock2 = Stock("GOOGL", 2750.00, 5)
portfolio.add_stock(stock2) 
print(portfolio._holdings)
print(f"Total portfolio value: ${portfolio.total_value():.2f}")

#Exercise 6: Bug hunt:
"""
    class Stock:
       def __init__(self, ticker, price):
           ticker = ticker
           price = price

   apple = Stock("AAPL", 227.35)
   print(apple.ticker) 
"""
#What happens when you run this, and why?
#Fix it, and explain the role self. plays that's missing here.

class Stock:
       def __init__(self, ticker, price):
           self.ticker = ticker
           self.price = price

apple = Stock("AAPL", 227.35)
print(apple.ticker)

"""
When you run the original code, it will raise an AttributeError because the instance variables ticker and price are not being set correctly.
The variables ticker and price are local to the __init__ method and do not belong to the instance of the class.
By using self.ticker and self.price, we are assigning the values to the instance variables of the Stock class, which allows us to access them later using the instance (apple in this case).
"""
