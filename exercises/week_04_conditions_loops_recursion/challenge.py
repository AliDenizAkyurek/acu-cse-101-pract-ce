"""Weeks 04–05: Three short challenges.

Replace each pass with your code. Keep function names and parameters unchanged.
Return answers; do not print them or use input(). No imports are needed.
Use practice.py as a guide. Tests check results; your TA can review your approach.
"""


# 1. Conditions: describe a temperature in degrees Celsius.
# Below 10: return "cold". From 10 through 25: return "warm".
# Above 25: return "hot". Use if / elif / else.
# Examples: -3 -> "cold", 10 -> "warm", 25 -> "warm", 26 -> "hot".
# Assume temperature is a number. Pay attention to the exact boundaries.
def describe_temperature(temperature):
    pass


# 2. Iteration: COUNT the even positive integers from 1 through n (inclusive).
# Use a for or while loop with a condition. Add 1 to a counter per match;
# do not add the even number itself. Zero is not part of the range.
# Examples: n = 5 -> 2 (the numbers 2 and 4); n = 6 -> 3; n = 0 -> 0.
# Assume n is a non-negative integer. No matching numbers means return 0.
def count_evens(n):
    pass


# 3. Recursion: return 2 raised to the non-negative integer power n.
# Use a base case and call this function with n - 1 for the smaller problem.
# Rule: 2 to the power 0 is 1. Each next power is 2 times the previous one.
# Examples: n = 0 -> 1; n = 1 -> 2; n = 3 -> 8 (2 * 2 * 2).
# Assume n is a small non-negative integer. Practice recursion, not ** or pow().
def power_of_two(n):
    pass
