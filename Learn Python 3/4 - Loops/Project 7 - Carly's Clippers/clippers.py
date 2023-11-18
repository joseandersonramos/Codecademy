# 💇‍♀️ Carly's Clippers Project
# José Anderson Ramos Aquino

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

print("**Carly's Clippers hair styles**" + "\n" + str(hairstyles) + "\n")
print("**Prices**\n" + str(prices))
print("\n**Last week data**\n" + str(last_week) + "\n")

# The average price of a cut
total_price = 0

for price in prices:
  total_price += price

average_price = total_price / len(prices)

print("**Average Haircut Price**\n" + str(average_price))

# Cut all prices by 5 dollars
new_prices = [price - 5 for price in prices]
print("\n**Cut all prices by 5 dollars**\n" + str(new_prices))

# Last week revenue
total_revenue = 0

for i in range(0, len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("\n**Total Revenue**\n" + str(total_revenue))

# Average daily revenue
average_daily_revenue = total_revenue / 7
print('\n**Average daily revenue**')
print(average_daily_revenue)

# Cuts under 30
cuts_under_30 = [hairstyles[i] for i in range(len(new_prices)) if new_prices[i] < 30]
print('\n**Cuts under 30**\n' + str(cuts_under_30))

