#This sets the total cars to 100
cars = 100
#This sets the space in the cars to 4.0
space_in_a_car = 4.0
#sets the number of drivers
drivers = 30
#sets the number of passengers
passengers = 90
#an equation for the numbr of cars not being use
cars_not_driven = cars - drivers
#number of cars for each driver
cars_driven = drivers
#the capacity of the carpool
carpool_capacity = cars_driven * space_in_a_car
#equation for the average number of passenger per car
average_passengers_per_car = passengers / cars_driven


print("There are ", cars, "cars available.")

print("There are only ", drivers, "drivers available.")

print("There will be ", cars_not_driven, "empty cars today.")

print("We have ", passengers, "to carpool today.")

print("We need to put about ", average_passengers_per_car , "in each car.")