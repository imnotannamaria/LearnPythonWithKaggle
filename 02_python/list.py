planets = [
    'Mercury',
    'Venus',
    'Earth',
    'Mars',
    'Jupiter',
    'Saturn',
    'Uranus',
    'Neptune'
]

# Indexing
print("Indexing")
print(planets[0])   # Mercury
print(planets[1])   # Venus
print(planets[-1])  # Neptune
print(planets[-2])  # Uranus
print("===========================================")

print("Slicing")
print(planets[0:3])    # ['Mercury', 'Venus', 'Earth']
print(planets[:3])     # ['Mercury', 'Venus', 'Earth']
print(planets[3:])     # ['Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
print(planets[1:-1])   # ['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus']
print(planets[-3:])    # ['Saturn', 'Uranus', 'Neptune']
print("===========================================")

print("Changing lists")
planets[3] = 'New Plannet'

planets[:3] = ['Mur', 'Vee', 'Ur']
print(planets)
print("===========================================")

print("List functions")
print(len(planets))
print(sorted(planets))    # The planets sorted in alphabetical order

primes = [2, 3, 5, 7]
print(sum(primes))
print(max(primes))
print("===========================================")

print("List methods")
planets.append("Pluto")    # Add pluto at the end of the list
planets.pop()    # remove the LAST element of the list
print(planets)
print("===========================================")

print("Searching lists")
print(planets.index("Neptune"))
print("Neptune" in planets)
print("Cherry" in planets)
print("===========================================")
