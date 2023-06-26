# Tuples are almost exactly the same as lists. They differ in just two ways.
# 1: The syntax for creating them uses parentheses instead of square brackets
# 2: They cannot be modified (they are immutable).

t = (1, 2, 3)
print(t)

# Tuples are often used for functions that have multiple return values.


def get_data():
    name = "Anna"
    age = 21
    height = 1.57
    return name, age, height


print(get_data())

print("Name:", get_data()[0])
print("Age:", get_data()[1])
print("Height:", get_data()[2])
