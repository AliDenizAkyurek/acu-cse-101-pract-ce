# Weeks 04–05: Conditions, Loops, and Recursion

One combined beginner module for conditionals/recursion and iteration.
**Think Python:** Chapters 5 and 7 in the course's chapter numbering.
Later weeks keep their existing numbers; there is no separate Week 05 submission.

## Learn one step at a time

[`practice.py`](practice.py) contains **completed, runnable examples**. Read one
part, predict its output, run it with **Play** or the top Python Run button, then
change a value and try again. Unlike Week 03's original workshop, you do not need
to fill in blanks before these examples work.

1. Compare values: `==`, `!=`, `<`, `<=`, `>`, `>=`, and chained comparisons.
2. Choose a branch with `if`, `elif`, and `else`: colons, indentation, order,
   boundaries, and returning from a function.
3. Combine conditions with `and`, `or`, `not`, and parentheses; return a Boolean
   expression directly. Avoid the common `day == "Saturday" or "Sunday"` mistake.
4. See truthiness and short-circuit evaluation, including safe division by zero avoidance.
5. Repeat with `for` and `range`: excluded stop values, steps, empty ranges,
   accumulators, and placing `return` after the loop.
6. Put an `if` inside a loop to select even numbers.
7. Repeat the same sum with `while`: initialization, conditions, updates, and stopping.
8. See how `break` and `continue` change a loop.
9. Write the same sum recursively: a base case and a smaller recursive call.

Suggested pacing: cover parts 1–4 first, then 5–8, and finish with part 9.
There is no user input, import requirement, Newton's method, or advanced math.
For the counting and recursion examples, use small non-negative integers.

## Three short graded challenges

Complete the three functions in [`challenge.py`](challenge.py), replacing `pass`.
Return each answer instead of printing it. Keep names and parameters unchanged.

| Function | Task | Boundary examples |
|---|---|---|
| `describe_temperature(temperature)` | Use `if` / `elif` / `else` to return `"cold"` below 10, `"warm"` from 10 through 25, otherwise `"hot"`. | 10 and 25 are both `"warm"`. |
| `count_evens(n)` | Use a loop and condition to count even positive integers from 1 through n. | 0 → 0; 1 → 0; 6 → 3. |
| `power_of_two(n)` | Use recursion to multiply by 2 once per level, starting from 1. | 0 → 1; 3 → 8. |

Tests check returned values. The TA reviews whether you practiced the requested
branching, loop, and recursion techniques; there are no hidden syntax checks.

## Check and submit

Choose **Run Tests** in **Course Tasks**, then select
`week_04_conditions_loops_recursion`. This checks only the graded challenges.
They intentionally fail until you write your solutions.

```bash
python3 -m pytest exercises/week_04_conditions_loops_recursion/test_challenge.py
```

The worked examples already pass their separate checks. After experimenting,
you can check them with:

```bash
python3 -m pytest exercises/week_04_conditions_loops_recursion/test_practice.py
```

When the challenge tests pass, choose **Submit** and the same week folder.
If the bottom menu is missing, use **Command Palette → Tasks: Run Task**.
