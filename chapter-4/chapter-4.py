print("------------------")

magicians = ['Alice', 'David', 'Bob']

for magician in magicians:
    print(magician.title() + ", that was a great tick!")
    print("I can't wait to see another one")

print("Thank you, everyone. That was a great magic show!")

print("------------------")

for value in range(1, 6):
    print(value)

numbers = list(range(1, 21))
print(numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

print("------------------")

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

print("------------------")

squares = [value**2 for value in range(1, 11)]
print(squares)

print("------------------")

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("First three players:")
for player in players[:3]:
    print(player.title())

print("Last three players:")
for player in players[-3:]:
    print(player.title())

print("------------------")

my_foods = ['food 1', 'food 2', 'food 3']
friend_foods = my_foods[:]

my_foods.append('food 4')
friend_foods.append('food 5')

print(my_foods)
print(friend_foods)

print("------------------")

print("Original dimensions:")
dimensions = (100, 200)
for dimension in dimensions:
    print(dimension)

print("Modified dimensions:")
dimensions = (200, 400)
for dimension in dimensions:
    print(dimension)