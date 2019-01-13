print("------------------")

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[-1])
print(bicycles[0].title())
#print(bicycles[23])
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

print("------------------")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

print("------------------")

motorcycles = []
print(motorcycles)
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

print("------------------")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

print("------------------")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
#del motorcycles[25]
print(motorcycles)

print("------------------")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

print("------------------")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
first_motorcycle = motorcycles.pop(1)
print(motorcycles)
print(first_motorcycle)

print("------------------")

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)

print("------------------")

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

print("------------------")

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

print("------------------")

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
print(sorted(cars))
print(cars)

print("------------------")

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)

print("------------------")

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

print("------------------")