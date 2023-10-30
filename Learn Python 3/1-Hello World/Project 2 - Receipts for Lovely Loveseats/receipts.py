# 💺 Receipts for Lovely Loveseats project.
# A program that creates receipts for a furniture store's customers.
# José Anderson Ramos Aquino. 

# Task 1 - First item's description.
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""

# Task 2 - First item's price
lovely_loveseat_price = 254.00

# Task 3 - Second item's description.
stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""

# Task 4 - Second item's price.
stylish_settee_price = 180.50

# Task 5 - Third item's description.
luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""

# Task 6 - Third item's price.
luxurious_lamp_price = 52.15

# Task 7 - Set sales tax.
sales_tax = 0.088

# Task 8
customer_one_total = 0

# Task 9
customer_one_itemization = ""

# Task 10
customer_one_total += lovely_loveseat_price

# Task 11
customer_one_itemization += lovely_loveseat_description

# Task 12
customer_one_total += luxurious_lamp_price

# Task 13 
customer_one_itemization += luxurious_lamp_description

# Task 14 - Calculating sales tax.
customer_one_tax = customer_one_total * sales_tax

# Task 15 - Adding sales tax to customer total cost.
customer_one_total += customer_one_tax

# Task 16 - Printing out the heading for the itemization.
print("Customer One Items:")

# Task 17 - Printing out customer one itemization.
print(customer_one_itemization)

# Task 18 - Adding a heading for the total cost.
print("Customer One Total:")

# Task 19 - Printing out the total.
print(customer_one_total)
