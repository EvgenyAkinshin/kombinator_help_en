# bomonth

The `bomonth` function returns the first day of a month based on the specified offset from the source date.

The function is useful when you need to determine the beginning of the current, previous, or future month.

## Syntax

```text
bomonth(sourceDate, numberOfMonths)
```

**Parameters:**

- `sourceDate` — the date used as the starting point for calculating the beginning of the month. Required;
- `numberOfMonths` — the number of months to shift. Required numeric parameter.

A positive value shifts the calculation forward, a negative value shifts it backward, and `0` uses the month of the source date.

You can use:

- field values;
- results of other functions;
- expressions.

## Return value

The function returns the date of the first day of the calculated month.

If the source date contains a time value, the time is preserved.

## Features

Regardless of the day in the source date, the function returns the first day of the calculated month.

For example:

```text
bomonth("15/04/2025", 0)
```

Result:

```text
01.04.2025 00:00:00
```

---

With a negative offset, the function returns the first day of a previous month.

For example:

```text
bomonth("15/04/2025", -1)
```

Result:

```text
01.03.2025 00:00:00
```

---

The function accepts fractional numeric values.

For example:

```text
bomonth("15/04/2025", 1.5)
```

Result:

```text
01.06.2025 00:00:00
```

## Examples

**Shifting by several months**

```text
bomonth("15/04/2025", 2)
```

Result:

```text
01.06.2025 00:00:00
```

---

**Using an expression**

If:

- `sourceDate` = `15/04/2025`;
- `numberOfMonths` = `1`;

the expression:

```text
bomonth(sourceDate, numberOfMonths + 1)
```

returns:

```text
01.06.2025 00:00:00
```

## Errors

The function returns an error if one of the required parameters is empty.

An error occurs if no value is provided for:

- `sourceDate`;
- `numberOfMonths`.

## Related functions

The `bomonth` function can be combined with other date functions.

You can create the source date using the `date` function and then determine the beginning of the required month:

```text
bomonth(date(15, 4, 2025), 2)
```

Result:

```text
01.06.2025 00:00:00
```

The result can be passed to a formatting function:

```text
formatDate(bomonth(date(15, 4, 2026), 6),"dddd, d MMMM yyyy","en")
```

Result:

```text
Thursday, 1 October 2026
```