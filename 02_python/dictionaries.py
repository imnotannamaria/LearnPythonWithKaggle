print("Dictionaries")
# data structure for mapping keys to values.

numbers = {
    'one': 1,
    'two': 2,
    'three': 3
}

print("Geting dictionaries: ", numbers['one'])  # 1

# Adding data
numbers['eleven'] = 11

# Chaging the value
numbers['one'] = '01'

print(numbers)

for num in numbers:
    print("{} = {}".format(num, numbers[num]))
print("=====================")

print("Dictionary Comprehensions")
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[0] for planet in planets}
print(planet_to_initial)
# { 'Mercury': 'M',
# 'Venus': 'V',
# 'Earth': 'E',
# 'Mars': 'M',
# 'Jupiter': 'J',
# 'Saturn': 'S',
# 'Uranus': 'U',
# 'Neptune': 'N' }

print('Saturn' in planet_to_initial)    # True
print('Betelgeuse' in planet_to_initial)     # False

# Get all the initials, sort them alphabetically, and put them in a space-separated string.
print(' '.join(sorted(planet_to_initial.values())))

for planet, initial in planet_to_initial.items():
    print("{} begins with \"{}\"".format(planet.rjust(10), initial))


doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]


def word_search(doc_list, keyword):
    # list to hold the indices of matching documents
    indices = []
    # Iterate through the indices (i) and elements (doc) of documents
    for i, doc in enumerate(doc_list):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
        normalized = [token.rstrip('.,').lower() for token in tokens]
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i) 
    return indices


print(word_search(doc_list, 'car'))


def multi_word_search(documents, keywords):
    keyword_to_indices = {}
    for keyword in keywords:
        keyword_to_indices[keyword] = word_search(documents, keyword)
    return keyword_to_indices


print(multi_word_search(doc_list, ['casino', 'they']))
