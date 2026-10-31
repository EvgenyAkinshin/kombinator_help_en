# eomonth

The `eomonth` function returns the last day of a month based on the specified offset from the source date.

The function is useful when you need to determine the end of the current, previous, or future month.

## Syntax

```text
eomonth(sourceDate, numberOfMonths)
```

**Parameters:**

- `sourceDate` — the date used as the starting point for calculating the end of the month. Required;
- `numberOfMonths` — the number of months to shift. Required numeric parameter.

A positive value shifts the calculation forward, a negative value shifts it backward, and `0` uses the month of the source date.

You can use:

- field values;
- results of other functions;
- expressions.

## Return value

The function returns the date of the last day of the calculated month.

If the source date contains a time value, the time is preserved.

## Features

The function automatically takes into account the number of days in each month.

For example:

```text
eomonth("15/02/2025", 0)
```

Result:

```text
28.02.2025 00:00:00
```

---

For a leap year:

```text
eomonth("15/02/2024", 0)
```

Result:

```text
29.02.2024 00:00:00
```

---

The function accepts fractional numeric values.

For example:

```text
eomonth("15/04/2025", 1.5)
```

Result:

```text
30.06.2025 00:00:00
```

## Examples

**Shifting by several months**

```text
eomonth("15/04/2025", 2)
```

Result:

```text
30.06.2025 00:00:00
```

---

**Using an expression**

If:

- `sourceDate` = `15/04/2025`;
- `numberOfMonths` = `1`;

the expression:

```text
eomonth(sourceDate, numberOfMonths + 1)
```

returns:

```text
30.06.2025 00:00:00
```

## Errors

The function returns an error if one of the required parameters is empty.

An error occurs if no value is provided for:

- `sourceDate`;
- `numberOfMonths`.

## Related functions

The `eomonth` function can be combined with other date functions.

You can create the source date using the `date` function and then determine the end of the required month:

```text
eomonth(date(15, 4, 2025), 2)
```

Result:

```text
30.06.2025 00:00:00
```

The result can be passed to a formatting function:

```text
formatDate(eomonth(date(15, 4, 2026), 6),"dddd, d MMMM yyyy","en")
```

Result:

```text
Saturday, 31 October 2026
```