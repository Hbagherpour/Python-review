
#Exercise1: Basic classifier: Given price_change_pct = 3.2, write if/elif/else that prints:
#"Strong gain" if > 5
#"Mild gain" if between 0 and 5 (inclusive of 0)
#"Mild loss" if between -5 and 0 (exclusive of 0)
#"Strong loss" if <= -5

price_change_pct = 3.2

if price_change_pct > 5:
    print ("Strong gain")
elif price_change_pct >= 0:
    print("Mild gain")
elif price_change_pct > -5:
    print("Mild loss")
else:
    print("Strong loss")

#Exercise2:Logical operators — trade filter: Given price = 145, volume = 1_200_000, is_market_open = True,
#print "Execute trade" only if price is between 100 and 200 and volume is above 1,000,000 and market is open.
#Otherwise print "Hold".

price = 145
volume = 1200000
is_market_open = True

if  100 < price < 200 and volume > 1000000 and is_market_open:
    print("Execute trade")
else:
    print("Hold") 


#Exercise3:Truthiness practice: Write a function-free snippet that checks a variable ticker_input = "" and
#prints "Please enter a ticker" if it's empty, using truthiness (not == "").

ticker_input = ""
if not ticker_input:
    print("Please enter a ticker")

#Exercise4: Chained comparison: Given rsi = 72 (a real trading indicator, 0–100 scale),
#print "Overbought" if rsi > 70, "Oversold" if rsi < 30,
#otherwise "Neutral" — write it using chained comparison where it makes sense.

rsi = 72
if rsi > 70:
    print("Overbought")
elif rsi < 30:
    print("Oversold")
else:
    print("Neutral")


#Exercise5: Ternary practice: Given open_price = 100, close_price = 98,
#use a ternary expression to set trend = "Up" or trend = "Down", then print it.

open_price = 100
close_price = 98

trend = "Up" if close_price > open_price else "Down"
print(trend)

#Exercise6: Bug hunt:
#score = 85
#   if score = 90:
#       print("A grade")
#What's wrong? Fix it, and explain in a comment why Python catches this particular mistake immediately (unlike some other languages).

# for comparison the == should be used not = , also it does not give any print anything if the condition does not meet the value
# if score = 90: causes a SyntaxError, not just a logic bug.
# Python's grammar strictly separates statements (like assignment "=")
# from expressions (like comparisons "=="). An if-condition must be
# an expression, so using "=" there is invalid before the code even runs.

score = 85
if score == 90:
   print("A grade")
else:
    print("not A grade")
