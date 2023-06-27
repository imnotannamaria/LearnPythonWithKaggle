print("String syntax")

print("01 - Using {\"\" or \'\'}")
print('What\'s up?')   # What's up?
print("What's up?")    # What's up?
print("====================")

print("02 - Using {/}")
print("Look, a mountain: /\\")    # Look, a mountain: /\
print("====================")


print("03 - Using {\\n}")
print("1\n2\n3")
print("====================")


print("04 - Using {end=}")
print("prodologica", end='')
print("damente", end='')
print()    # prodologicadamente
print("====================")

print("05 - Indexing")
planet = 'Pluto'
print(planet[0])    # P
print("====================")

print("06 - Slicing")
name = 'Roberto'
print(name[-5:])    # berto
print("====================")

print("07 - Looping")
text = 'Infinite'
print([char+'! ' for char in text])    # ['I! ', 'n! ', 'f! ', 'i! ', 'n! ', 'i! ', 't! ', 'e! ']
print("====================")

print("String methods")
print("08 - To Upper")
claim = "Pluto is a planet!"
print(claim.upper())    # PLUTO IS A PLANET!
print("====================")

print("09 - To Lower")
claim = "PLUTO IS A PLANET!"
print(claim.lower())    # pluto is a planet!
print("====================")

print("10 - Indexing")
indexing = "Indexing"
print(indexing.index('xing'))    # 4
print("====================")

print("11 - startswith")
text_start = "Starts with"
print(text_start.startswith("Start"))    # True
print("====================")

print("12 - endswith")
text_end = "Ends with"
print(text_end.endswith('with'))    # True
print("====================")

print("13 - split")
words = "Good Choice"
print(words.split())   # ['Good', 'Choice']

datestr = '1956-01-31'
#  split on something other than whitespace, in the down case "-"
year, month, day = datestr.split('-')
print(year, month, day)
print("====================")

print("13 - join")
print('/'.join([month, day, year]))   # 01/31/1956

print(' 🪓 '.join([word.upper() for word in words]))    # G 🪓 O 🪓 O 🪓 D 🪓   🪓 C 🪓 H 🪓 O 🪓 I 🪓 C 🪓 E
print("====================")

print("13 - format")
person = "Maria Júlia"
position = 1
format_ex = "{}, you'll always be the {}th place in my {}".format(person, position, "❤")
print(format_ex)

pluto_mass = 1.354
population = 52910390
print("Pluto mass with 3 decimal points: {:.3}".format(pluto_mass))   # 1.35
print("Pluto mass with 3 decimal points and format as percent: {:.3%}".format(pluto_mass))    # 135.400%
print("Pluto mass separate with commas: {:,}".format(population))    # 52,910,390
print("====================")
