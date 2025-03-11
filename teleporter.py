# Apple Teleporter Version 1.0
# By: Apple Inc.
# Date: 2042-01-03

print("Welcome to the Teleporter 1.0.")

print("Please enter the meters you want to teleport in front of you.")
input_meters = input("Meters:")

print("Please enter how many people you want to transport with you.")
input_persons = input("Persons:")

starting_costs = 100
costs_per_meter = 12
costs_per_person = 14


total_costs = starting_costs + (int(input_meters) * costs_per_meter) + (int(input_persons) * costs_per_person)

print("The total costs for teleporting", input_meters, "meters with", input_persons, "persons is", total_costs, "dollars.")