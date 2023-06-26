def least_difference(a, b, c):
    # Docstrings
    """Return the smallest difference between any two numbers
     among a, b and c.

     >>> least_difference(1, 5, -5)
     4
     """
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)


print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7)
)

help(least_difference)

print(1, 2, 3, sep=' - ')


def greet(who="Anna"):
    print("Hello,", who)


greet()
greet(who="Snakes")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")

help(abs)