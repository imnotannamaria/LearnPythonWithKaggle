# Combining Boolean Values

def can_run_for_president(age, is_natural_born_citizen):
    """Can someone of the given age and citizenship status run for president in the US?"""
    # The US Constitution says you must be a Natural Born citizen *and* at least 35 years old

    # and | or | not
    return is_natural_born_citizen and (age >= 35)


print(can_run_for_president(19, True))
print(can_run_for_president(55, False))
print(can_run_for_president(55, True))

help(can_run_for_president)


# Boolean conversion
print(bool(1))  # all numbers are treated as true, except 0
print(bool(0))
print(bool("asf"))  # all strings are treated as true, except the empty string ""
print(bool(""))
# Generally empty sequences (strings, lists, and other types we've yet to see like lists and tuples)
# are "falsey" and the rest are "truthy"


def sign(num):
    if num > 0:
        return 1
    elif num == 0:
        return 0
    else:
        return -1


print(sign(-4))

test = True
print("Boolean test: ", int(test))

