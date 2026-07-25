
#Exercises1: Clean messy input: Given raw_ticker = "  aapl.O  \n", clean it up so the result is exactly "AAPL" (strip whitespace, remove .O, uppercase).
raw_ticker = "  apple.0  \n"
print(raw_ticker.strip().upper()[0:5])
print(raw_ticker.strip().upper().replace(".0", ""))

#(Exercises2: a real financial identifier — first 2 chars = country code, next 9 = security identifier, last 1 = check digit), extract and print each of the three parts separately using slicing.
isin = "US0378331005"

country_code = isin[0:2]
security_id = isin[2:11]
check_digit = isin[-1]

print(country_code)
print(security_id)
print(check_digit)


#Exercises3: ormatting report: Given
#company = "Apple Inc."
#price = 227.3
#change_pct = 0.0182
#Print: Apple Inc.: $227.30 (+1.82%) using an f-string with proper formatting (no manual rounding/multiplying — use format specs).

company = "Apple Inc."
price = 227.3
change_pct = 0.0182

print(f"{company}: ${price:.2f} ({change_pct:.2%})")


#Exercises4: Bug hunt:
#   ticker = "TSLA"
#   ticker[0] = "M"
#   print(ticker)
#What happens when you run this? Explain why in a comment, and write the correct way to change "TSLA" to "MSLA".

# TypeError: 'str' object does not support item assignment
# Strings are immutable in Python — you cannot change a character
# in place. You must build a new string instead.

ticker = "TSLA"
ticker= "M" + ticker[1:]
print(ticker)

#Exercises5: Bonus (join): Given tickers = ["AAPL", "MSFT", "GOOG", "AMZN"],
#print them as a single comma-separated string, but wrap each ticker in quotes: "AAPL", "MSFT", "GOOG", "AMZN".

tickers = ["AAPL", "MSFT", "GOOG", "AMZN"]
quoted = [f'"{t}"' for t in tickers]

result = ", ".join(quoted)
print(result)