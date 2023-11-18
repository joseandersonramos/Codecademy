#🍕 Len's Slice project.
# Practice with lists method and functions.
# José Anderson Ramos Aquino.

# Pizzas that I sell
print('*Pizzas that I sell*')
toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']
print(toppings)

# Pizza slice prices
prices = [2, 6, 1, 3, 2, 7, 2]
print('\n*Pizza slice prices*')
print(prices)

# Number of $2 slices
num_two_dollar_slices = prices.count(2)
print('\n*Number of $2 slices*')
print(num_two_dollar_slices)

# Number of pizzas
num_pizzas = len(toppings)
print('\n*Number of pizzas*')
print('We sell', num_pizzas, 'different kinds of pizza!')

# Create a 2D list with pizza toppings and prices
pizza_and_prices = [[2, 'pepperoni'], [6, 'pineapple'], [1, 'cheese'], [3, 'sausage'], [2, 'olives'], [7, 'anchovies'], [2, 'mushrooms']]

print('\n*2D list with pizza toppings and prices*')
print(pizza_and_prices)

# Sort the list by price
pizza_and_prices.sort()
print('\n*Sort the list by price*')
print(pizza_and_prices)

# Store the first element of the list
# The cheapest pizza
cheapest_pizza = pizza_and_prices[0]
print('\n*The cheapest pizza*')
print(cheapest_pizza)

# Store the last element of the list
# The most expensive pizza
priciest_pizza = pizza_and_prices[-1]
print('\n*The most expensive pizza*')
print(priciest_pizza)

# Remove the anchovies slice
pizza_and_prices.pop()
print('\n*Remove the anchovies slice*')
print(pizza_and_prices)

# Add peppers to the list
pizza_and_prices.insert(4, [2.5, 'peppers'])
print('\n*Add peppers to the list*')
print(pizza_and_prices)

# Store the 3 lowest cost pizzas in the list
three_cheapest = pizza_and_prices[0:3]
print('\n*Store the 3 lowest cost pizzas in the list*')
print(three_cheapest)