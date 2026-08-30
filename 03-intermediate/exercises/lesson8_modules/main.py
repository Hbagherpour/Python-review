#Exercise2: main.py (same folder) — import finance_utils and:
#Call calculate_return and apply_commission from it, print results
#Import datetime and print today's date
#Import random and print a random choice from ["AAPL", "MSFT", "GOOG", "TSLA"]
#Use json.dumps() to convert this dict to a JSON string and print it: {"ticker": "AAPL", "price": 227.35}

from finance_utils import calculate_return, apply_commission
print(calculate_return(145, 157.5))
print(apply_commission(150))
print(apply_commission(150, 0.002))

import datetime
print(datetime.date.today())

import random
print(random.choice(["AAPL", "MSFT", "GOOG", "TSLA"]))  

from json import dumps
data = {"ticker": "AAPL", "price": 227.35}  
print(dumps(data))



#Exercise3: Test the __main__ behavior: Run finance_utils.py directly (should print your test call),
#then run main.py (should NOT print that test call, only main.py's own output).
#Add a comment in main.py explaining in your own words why the test call doesn't run when imported.

"""The test call in finance_utils.py doesn't run when imported because the code inside 
the if __name__ == "__main__": block only executes when the file is run directly, 
not when it is imported as a module.
"""


#Exercise4: Bug hunt (conceptual — no fixed file, just answer in a comment in main.py):
#from finance_utils import *
#from other_module import *
#Why is this considered bad practice, even if it technically works? Name a concrete problem it could cause.


"""Importing all symbols from modules using * can lead to namespace pollution, making it unclear which symbols are defined in the current scope. It can also cause naming conflicts if multiple modules have symbols with the same name."""
