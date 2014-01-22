#Forteller hvor mange biler
cars = 100
#Hvor stor plass
space_in_a_car = 4.0
#Hvor mange sjaforer
drivers = 30
#Hvor mange passasjerer
passengers = 90
#Hvor mange biler som ikke blir kjort
cars_not_driven = cars - drivers
#hvor mange biler som blir kjort
cars_driven = drivers
#Hvor god plass det er i alle biler som blir kjort
carpool_capacity = cars_driven * space_in_a_car
#hvor mange passasjerer per bil
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We need to put about", average_passengers_per_car, "in each car."
