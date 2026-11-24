# Lab 01 Exercise 1: Road Trip Budgeter
# Write your code below:

def is_budget_sufficient(one_way_km,budget):
    litre_needed = (one_way_km*2)/10
    price = litre_needed * 2
    return budget >= price

# Test your code here
print("Testing Road Trip Budgeter...")
print(is_budget_sufficient(100,40))
print(is_budget_sufficient(100,39))