print("Loops")

print("01 - Example")
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for planet in planets:
    print(planet, end='\n')
print("==============================")

print("02 - Example")
multiplicands = (2, 2, 2, 3, 3, 5)
product = 1
for mult in multiplicands:
    product = product * mult
    print(product)
print("==============================")

print("03 - Example")
s = 'steganograpHy is the practicE of conceaLing a file, ' \
    'message, image, or video within another fiLe, message, ' \
    'image, Or video.'
msg = ''
# print all the uppercase letters in s, one at a time
for char in s:
    if char.isupper():
        print(char, end='\n')
print("==============================")

print("04 - Range")
for i in range(5):
    print("Doing important work. i =", i)
print("==============================")

print("05 - While")
i = 0
while i < 10:
    print(i, end='\n')
    i += 1
print("==============================")
