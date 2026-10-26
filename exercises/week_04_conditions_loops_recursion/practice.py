"""Weeks 04–05: Conditions, Loops, and Recursion.

Read one part at a time with your instructor / TA, predict the output, then run
this file. These are worked examples: change the suggested values and run again.
The three independent exercises to submit are in challenge.py.
"""


# PART 1 — Comparisons make Boolean values: True or False (capital letters).
# = assigns a value. == compares two values. != means "not equal".
# Other comparisons: <, <=, >, >=. <= and >= include the boundary.
# age = 18 stores 18; age == 18 asks whether age is equal to 18.
def comparison_examples():
    age = 18
    print(age == 18)        # True
    print(age != 18)        # False
    print(age > 18)         # False: 18 is not greater than itself.
    print(age >= 18)        # True: the boundary is included.
    print(0 <= age <= 18)   # True: Python allows chained comparisons.
    print("18" == 18)       # False: text and an integer are different values.
    # TRY: change age to 17, then 19. Predict each result before running.


# PART 2 — if / elif / else: choose ONE branch, from top to bottom.
# Each condition ends with a colon. Indent its body with four spaces.
# elif means "otherwise, if". else has NO condition and is optional.
# Here zero needs its own branch: it is neither positive nor negative.
def describe_number(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"
    # return immediately leaves the function. Code after it does not run.
    # Without an else or final return, a missed case could return None.


# Order matters when conditions overlap. Put the narrower condition first.
def ticket_price(age):
    if age < 6:
        return 0
    elif age < 18:
        return 10
    else:
        return 20
    # For age 5, both age < 6 and age < 18 are True, but only the first wins.
    # Two separate if statements would check both conditions independently.
    # TRY: ages 5, 6, 17, and 18. Assume ages are non-negative integers.


# PART 3 — Combine conditions; Boolean expressions can be returned directly.
# and: both conditions must be True. or: at least one must be True.
# not: reverses a Boolean. Use parentheses to show how conditions are grouped.
# For Boolean operands:
#   True and False -> False      True or False -> True
#   False and True -> False      False or False -> False
#   True and True -> True        True or True -> True
#   False and False -> False     False or True -> True
def can_enter(age, has_ticket):
    return age >= 12 and has_ticket
    # has_ticket is a Boolean parameter: pass True or False, not "True".
    # No need to write if condition: return True / else: return False.


def is_weekend(day):
    return day == "Saturday" or day == "Sunday"
    # WRONG: day == "Saturday" or "Sunday"
    # Each side of or must express the intended condition. A nonempty string
    # such as "Sunday" counts as True in an if, even when day is "Monday".
    # Comparisons are case-sensitive: "sunday" is not "Sunday".


def can_borrow(has_card, is_staff, is_blocked):
    return (has_card or is_staff) and not is_blocked
    # A card OR staff status is enough, but blocked people cannot borrow.
    # not is evaluated before and, and before or. Parentheses make intent clear.
    # Without parentheses, has_card or is_staff and not is_blocked would let
    # a blocked cardholder through because and is evaluated before or.


# PART 4 — Truthiness and short-circuit evaluation.
# In conditions, 0, "", and None are false; nonzero numbers and nonempty strings
# are true. Note that "False" is a nonempty string, so bool("False") is True!
# and / or can return an operand, not necessarily a Boolean:
# "" or "guest" gives "guest"; "Ada" or "guest" gives "Ada".
# Keep operands Boolean when you want a True/False result.
def is_small_ratio(total, count):
    return count != 0 and total / count < 10
    # and skips its right side when its left side is false. This prevents
    # division by zero. With or, the right side is skipped when the left is true.
    # TRY: (12, 2), (20, 2), (12, 0). The threshold 10 is excluded.


# PART 5 — for repeats once per value in a sequence.
# range(start, stop) INCLUDES start and EXCLUDES stop.
# range(3) gives 0, 1, 2. range(1, 4) gives 1, 2, 3.
# range(0) is empty. range(1, 1) is also empty: zero repetitions.
# range(1, 6, 2) gives 1, 3, 5. The third argument is the step.
# range(3, 0, -1) gives 3, 2, 1. A step of zero is an error.
def sum_with_for(n):
    total = 0                     # Initialize ONCE, before the loop.
    for number in range(1, n + 1): # n + 1 includes n.
        total = total + number    # You can also write: total += number.
    return total                  # Outside the loop: finish ALL additions.
    # n = 3: total changes 0 -> 1 -> 3 -> 6.
    # n = 0: the loop never runs, so the result stays 0.
    # Returning inside the loop would stop after the first addition!


# PART 6 — Put a condition INSIDE a loop to act only on matching values.
# % gives the remainder: number % 2 == 0 means the number is even.
def sum_even_numbers(n):
    total = 0
    for number in range(1, n + 1):
        if number % 2 == 0:
            total += number       # Eight spaces: inside if AND for.
    return total
    # n = 5: visit 1, 2, 3, 4, 5; add only 2 and 4; return 6.
    # n = 0 or 1: no even positive numbers, so return 0.


# PART 7 — while repeats as long as its condition is True.
# Check the condition BEFORE each repetition. It may run zero times.
def sum_with_while(n):
    total = 0
    number = 1
    while number <= n:
        total += number
        number += 1               # Progress! Forgetting this can loop forever.
    return total
    # n = 3: add 1, 2, 3; number becomes 4; 4 <= 3 is False; stop.
    # n = 0: 1 <= 0 is False immediately; return 0.
    # Use for when traversing a known range; while when repeating on a condition.
    # If an experiment loops forever, stop it with Ctrl+C in the terminal.


# PART 8 — break stops a loop; continue skips to the next repetition.
def loop_control_examples():
    for number in range(1, 6):
        if number == 2:
            continue              # Skip printing 2; the for loop advances.
        if number == 4:
            break                 # Stop before printing 4 or reaching 5.
        print(number)             # Prints 1, then 3.
    # break leaves the loop; return leaves the whole function.
    # In a while loop, continue can skip your counter update: take care!


# PART 9 — Recursion: a function calls itself with a SMALLER problem.
# You need (1) a base case that stops and (2) progress toward that case.
# Inputs here are small, non-negative integers; other inputs are out of scope.
def sum_with_recursion(n):
    if n == 0:                    # Base case: no more numbers to add.
        return 0
    return n + sum_with_recursion(n - 1)
    # sum(3) -> 3 + sum(2) -> 3 + 2 + sum(1) -> 3 + 2 + 1 + sum(0)
    # Then return back through the calls: 0 -> 1 -> 3 -> 6.
    # Calling with n instead of n - 1 would never reach the base case.
    # Negative n also moves away from zero here. Only use non-negative n.
    # Python limits recursion depth; use loops for long repetitions.


# This block runs when you press Run / Play, but not when tests import the file.
if __name__ == "__main__":
    print("1. Comparisons:")
    comparison_examples()
    print("2. Branches:", describe_number(-2), describe_number(0), describe_number(2))
    print("   Prices:", ticket_price(5), ticket_price(6), ticket_price(18))
    print("3. and:", can_enter(12, True), can_enter(12, False))
    print("   or:", is_weekend("Sunday"), is_weekend("Monday"))
    print("   Grouping:", can_borrow(True, False, True))
    print("4. Safe division:", is_small_ratio(12, 2), is_small_ratio(12, 0))
    print("5. for:", sum_with_for(3), sum_with_for(0))
    print("6. Conditions inside loops:", sum_even_numbers(5))
    print("7. while:", sum_with_while(3), sum_with_while(0))
    print("8. continue / break:")
    loop_control_examples()
    print("9. Recursion:", sum_with_recursion(3), sum_with_recursion(0))
