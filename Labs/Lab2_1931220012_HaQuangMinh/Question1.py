import math 

square_feet = float(input("Enter the square feet: "))
price_per_gallon = float(input("Enter the price of paint per gallon: $"))


gallons = math.ceil(square_feet / 112)
# Celi làm tròn lên
print(f"Gallons of paint required: {gallons}")

hours = (square_feet / 112) * 8
print(f"Gallons of paint required: {hours}")

paintCost = gallons * price_per_gallon
print(f"Gallons of paint required: {paintCost}")

laborCost = hours * 35
print(f"Gallons of paint required: {laborCost}")

totalCost = paintCost + laborCost
print(f"Gallons of paint required: {totalCost}")