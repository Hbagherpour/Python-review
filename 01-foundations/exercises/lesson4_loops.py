#Exercises1: Basic iteration: Given prices = [150.2, 152.8, 148.5, 155.1, 149.9],
#loop through and print each one formatted to 2 decimal places.

prices = [150.2, 152.8, 148.5, 155.1, 149.9]
for price in prices:
    print(f"{price:.2f}")


#Exercises2: Accumulator pattern: Using the same prices list,
#calculate and print the average price — no built-in sum()/avg() shortcuts,
#use a loop to add them up manually (this pattern — accumulate in a loop — is fundamental,
#you'll use it everywhere before you learn the shortcuts).

prices = [150.2, 152.8, 148.5, 155.1, 149.9]

total = 0
count = 0

for price in prices:
    total = total + price 
    count += 1

average = total / count

print (average)


#Exercises3: Filtering with continue: Given daily_returns = [1.2, -0.5, 3.1, -2.8, 0.4, -1.1],
#loop through and print only the positive returns, skipping negative ones using continue.

daily_returns = [1.2, -0.5, 3.1, -2.8, 0.4, -1.1]

for i in daily_returns:
    if i < 0:
        continue
    print(i)

#Exercises4: Early exit with break: Given prices = [100, 102, 105, 98, 110, 95],
#loop through and print each price, but stop immediately (using break) the first time a price drops below 100
#(after having already gone above it once — i.e. just stop at the first price < 100 you encounter,
#print a message saying at which index it happened).

prices = [100, 102, 105, 98, 110, 95]
index = 0 

for price in prices:
    if price < 100:
        break
    print(price) 
    index += 1
print(f"The price dropped at index {index}")

#Exercise5: enumerate practice: Given portfolio = ["AAPL", "MSFT", "TSLA", "NVDA"],
#print each with a 1-based position number: "1: AAPL", "2: MSFT", etc.

portfolio = ["AAPL", "MSFT", "TSLA", "NVDA"]

for i, ticker in enumerate(portfolio, start=1):
    print(f"{i}: {ticker}")


#Exercise6: while loop — compound growth: Starting with investment = 5000 and an annual growth rate of 7%,
#use a while loop to calculate how many full years it takes for the investment to exceed 10000.
#Print the number of years and the final value.

investment = 5000
years = 0

while investment < 10000:
    investment = investment * 1.07
    years += 1
print(f"Took {years} years to exceed 10000 as {investment:.2f}")

#Exercise7: Bug hunt: 
"""
   count = 0
   prices = [10, 20, 30]

   while count < len(prices):
       print(prices[count])
"""
#What happens when you run this? Explain why in a comment, and fix it.

# Count starts at 0 and the while-condition (count < len(prices)) stays True forever
# The loop will iterate without stopping. Because there is no accumulator in the loop to add up each loop, the count always stays at 0. 
# To fix the issue, count +=1 was added to accumulate the loop iterations 

count = 0
prices = [10, 20, 30]
print(len(prices))

while count < len(prices):
       print(prices[count])
       count += 1