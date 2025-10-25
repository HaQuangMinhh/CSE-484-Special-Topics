user_input = float(input("Enter the total sales: "))

countryTax = user_input * 0.025 
stateTax = user_input * 0.05
totalTax = countryTax + stateTax

print(f"Country tax: {countryTax}")
print(f"State Tax: {stateTax}")
print(f"Total Tax: {totalTax}")