print("01 - With list comprehensions")
squares = [n**2 for n in range(10)]
print(squares)    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print("=====================")

print("02 - Without list comprehensions")
squares = []
for n in range(10):
    squares.append(n**2)
print(squares)    # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print("=====================")

print("03 - Example")
planets = ['Venus', 'Earth', 'Mars', 'Uranus']
short_planets = [planet for planet in planets if len(planet) < 6]
print(short_planets)    # ['Venus', 'Earth', 'Mars']
print("=====================")


print("04 - Example")
loud_short_planets = [
    planet.upper() + '!'
    for planet in planets
    if len(planet) < 6
]
print(loud_short_planets)    # ['VENUS!', 'EARTH!', 'MARS!']
print("=====================")

print("05 - With list comprehensions")


def count_negatives(nums):
    n_negative = 0
    for num in nums:
        if num < 0:
            n_negative = n_negative + 1
    return n_negative


print(count_negatives([5, -1, -2, 0, 3]))  # 2
print("=====================")

print("05 - Without list comprehensions")


def count_negatives(nums):
    return len([num for num in nums if num < 0])


print(count_negatives([5, -1, -2, 0, 3]))  # 2
print("=====================")

