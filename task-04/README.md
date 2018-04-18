# Task 04

(while loops, if statements, functions)

## Stage 1
Develop function that can convert string value to float. In case when input is invalid return `None` value.

## Stage 2

Develop function that can infinitely ask user for input (`while True`) and in case user inputs:

1. string that can be converted to float - returns float;
2. when user inputs `quit` returns `None`
3. in all other case prints message ```Value '{}' can't be converted to float``` and goes to the next iteration;

Also, function should be able to print some string, which notifies user what he should do.

Usage example:

```Python
a = get_safe_float_input("Please input value A")
if a is None:
  exit(0);

print("a = {}".format(a))
```

## Stage 3

Read values for `a`, `b` and `c` (all float values) and solve [Quadratic equation](
https://en.wikipedia.org/wiki/Quadratic_equation)

Print root(s) or message when no roots available.