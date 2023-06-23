# Functions with ONE argument example
import math


def get_pay(num_hours):
    # Pre-tax pay, based on receiving $15/hour
    pay_pretax = num_hours * 15
    # After-tax pay, based on being in 12% tax bracket
    pay_aftertax = pay_pretax * (1 - .12)
    return pay_aftertax


# Calculate pay based on working 40 hours
pay_fulltime = get_pay(40)
print("One argument example: ", pay_fulltime)


# Functions with multiple arguments example
def get_pay_with_more_inputs(num_hours, hourly_wage, tax_bracket):
    # Pre-tax pay
    pay_pretax = num_hours * hourly_wage
    # After-tax pay
    pay_aftertax = pay_pretax * (1 - tax_bracket)
    return pay_aftertax


higher_pay_aftertax = get_pay_with_more_inputs(40, 24, .22)
print("Multiple arguments example: ",higher_pay_aftertax)

# Functions with NO arguments example


# Define the function with no arguments and with no return
def print_hello():
    print("This is a functions with NO arguments example!")


# Call the function
print_hello()

# Question 1
# It should return the expected cost of a house with that number of bedrooms and bathrooms.  Assume that:
# - the expected cost for a house with 0 bedrooms and 0 bathrooms is `80000`.
# - each bedroom adds `30000` to the expected cost
# - each bathroom adds `10000` to the expected cost.


def get_expected_cost(beds, baths):
    inital_value = 80000
    bedroom_value = 30000 * beds
    bathroom_value = 10000 * baths

    value = inital_value + bedroom_value + bathroom_value
    return value


print("Question 1: ", get_expected_cost(2, 2))

