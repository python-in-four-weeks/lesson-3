# Lesson 3 Independent Challenges

## Challenge 1: `flip_coin` (4 points)

| Function parameter(s) | Function return(s)          |
|-----------------------|-----------------------------|
| None                  | The result of the coin flip |

Write a function that uses `random.choice` to simulate the flip of a coin and return the result. (The result should be either the exact text `heads` or the exact text `tails`.)

## Challenge 2: `roll_n_sided_dice` (8 points)

| Function parameter(s)                 | Function return(s) |
|---------------------------------------|--------------------|
| `n`, the number of sides the dice has | The number rolled  |

Write a function that uses `random.randint` to simulate the roll of an `n`-sided dice and return the result. (Each whole number from 1 to `n` is written on its own face of the dice.)

If `n` is less than 1, a `ValueError` should be raised with the following exact message, replacing the `___` with the value of `n`:

```
It isn't possible to have a ___-sided dice
```

## Challenge 3: `get_renewed_return_date` (4 points)

| Function parameter(s) | Function return(s)            |
|-----------------------|-------------------------------|
| None                  | The date two weeks from today |

Write a function that gets the new return date for a library book that is being renewed. This should be a `datetime.date` object (not a `datetime.datetime` object) that is always two weeks from today.

## Challenge 4: `calculate_age` (14 points)

| Function parameter(s)            | Function return(s)                                |
|----------------------------------|---------------------------------------------------|
| `date_of_birth`, a date of birth | The corresponding age in the form of a dictionary |

Write a function that takes a date object representing a date of birth and returns the corresponding age in the form of a dictionary: `{"years": ___, "months": ___}`, replacing the `___`s with the number of years and months since the given date of birth.

Note that the months value should not exceed 12: for example, rather than returning 4 years and 14 months, the function should return 5 years and 2 months. Also, as is generally the case with ages, you should round down if fractions are involved.

If the date of birth provided is in the future, a `ValueError` should be raised with the following exact message:

```
It isn't possible to have a date of birth in the future
```

## Challenge 5: `calculate_sphere_volume` (8 points)

| Function parameter(s)              | Function return(s)       |
|------------------------------------|--------------------------|
| `radius`, the radius of the sphere | The volume of the sphere |

Write a function that takes a value representing the radius of a sphere and returns the volume of that sphere.

For reference, the formula for finding the volume of a sphere based on its radius $r$ is as follows:

$$V=\frac{4}{3}\pi r^3$$

If the radius provided is less than zero, a `ValueError` should be raised with the following exact message:

```
It isn't possible for a sphere to have a negative radius
```

## Challenge 6: `calculate_quadratic_equation_solutions` (20 points)

| Function parameter(s)                       | Function return(s)                               |
|---------------------------------------------|--------------------------------------------------|
| `a`, `b` and `c`, the equation coefficients | A frozenset containing solutions to the equation |

Write a function that takes three values representing the coefficients of a quadratic equation and returns a frozenset containing all the unique solutions to the equation. More specifically, for $a$, $b$ and $c$ such that $ax^2+bx+c=0$, return as many unique values of $x$ as there are existing are that make the equation true.

For reference, when $a \neq 0$, the quadratic formula for solving quadratic equations is as follows:

$$x=\frac{-b\pm \sqrt{b^2-4ac}}{2a}$$

For the case where $a = 0$, you should find another suitable formula online and implement it carefully.

For the case where $a = b = c = 0$, a `ValueError` should be raised with the following exact message:

```
Infinite number of solutions found
```

Your function should not result in an uncaught exception if there are no solutions: an empty frozenset should be returned instead. (If you've come across complex numbers before, note that we are only interested in real solutions here.)

## Challenge 7: `get_guest_count` (14 points)

| Function parameter(s) | Function return(s)   |
|-----------------------|----------------------|
| None                  | The number of guests |

Write a function that asks the user for a single response: the number of guests for a restaurant booking. If the user types a positive integer, return this integer. Otherwise, raise a `ValueError` with one of the following exact messages:

```
Bookings cannot be for a negative number of guests
Bookings cannot be for zero guests
Bookings must be for a valid whole number of guests
```

For negative non-whole numbers of guests, choose the third error message rather than the first.

## Challenge 8: `split_bill_evenly` (14 points)

| Function parameter(s) | Function return(s) |
|-----------------------|--------------------|
| None                  | None               |

A restaurant bill totals 100.00 currency. Write a function that asks the user for a single response: the number of guests to split the bill evenly between. If the user types a positive integer, print the following exact text, replacing the `___` with the size of each share, formatted to exactly two decimal places:

```
That will be ___ each, thank you!
```

Otherwise, print one of the following exact messages:

```
The bill cannot be split between a negative number of guests.
The bill cannot be split between zero guests.
That isn't a valid whole number of guests.
```

For negative non-whole numbers of guests, choose the third error message rather than the first.

The function should not use any `if`-`else` blocks except to handle the case where the number of guests is negative (notably, you will need to find another solution in the case where the number of guests is zero). Rather, it should use at least one `try`-`except`-`else` block. Your function should not result in an uncaught exception under any circumstances.

## Challenge 9: `greet_customer` (8 points)

| Function parameter(s) | Function return(s) |
|-----------------------|--------------------|
| None                  | None               |

A function has been written for you that asks a user for a single response upon entering a shop: which action out of three possible options they would like to take. At the moment, the function sometimes results in an uncaught `IndexError` or `ValueError`. We would like to change this.

If possible, the function should still print the following exact text, replacing the `___` with the selected option:

```
You selected: ___.
```

Otherwise, the function should print the following exact text:

```
That wasn't one of the options.
```

You should achieve this change by wrapping one line of the function in a `try`-`except` block.

## Challenge 10: `serve_customer` (6 points)

| Function parameter(s) | Function return(s) |
|-----------------------|--------------------|
| None                  | None               |

A function has been written for you that asks a user for a single response: which of the available fruits they would like to purchase. At the moment, the function sometimes results in an uncaught `KeyError`. We would like to change this.

If possible, the function should still print the following exact text, replacing the `___` with the price of the fruit chosen:

```
That will be ___, please!
```

Otherwise, the function should print the following exact text:

```
That wasn't one of the options.
```

You should achieve this change by wrapping one line of the function in a `try`-`except` block.
