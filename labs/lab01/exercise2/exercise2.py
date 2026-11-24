# Lab 01 Exercise 2: Camping Logistics
import math
def calculate_tent_cost(participants,tent_capacity,tent_price):
    each_tent_person = participants/tent_capacity
    total_tent = math.ceil(each_tent_person)
    cost_tent = total_tent * tent_price
    return cost_tent

print(calculate_tent_cost(12, 4, 100))
print(calculate_tent_cost(13, 4, 100))