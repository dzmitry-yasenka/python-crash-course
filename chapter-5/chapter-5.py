print("---------------")

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print("---------------")

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car != 'bmw':
        print(car.title())
    else:
        print(car.upper())

print("---------------")

requested_toppings = ['onions', 'pineapple', 'mushrooms']
if 'mushrooms' in requested_toppings:
    print("mushrooms? - " + str(True))
else:
    print("mushrooms? - " + str(False))
if 'pepperoni' in requested_toppings:
    print("pepperoni? - " + str(True))
else:
    print("pepperoni? - " + str(False))

print("---------------")

age = 22
if age < 6:
    price = 0
elif age < 18:
    price = 5
elif age > 65:
    price = 5
else:
    price = 10
print("your admission for the ticket is $" + str(price))

print("---------------")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

print("---------------")

