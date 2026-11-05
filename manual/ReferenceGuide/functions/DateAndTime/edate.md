# edate

The `edate` function shifts a date forward or backward by the specified number of months.

The function is useful when you need to calculate a date relative to another date, for example, to get a date several months later or determine a date in a previous period.

## Syntax

```text
edate(sourceDate, numberOfMonths)
```

**Parameters:**

- `sourceDate` — the date from which the shift is calculated. Required;
- `numberOfMonths` — the number of months by which the date should be shifted. Required numeric parameter.

A positive `numberOfMonths` value shifts the date forward, while a negative value shifts it backward. A value of `0` returns the original date without shifting it.

You can use:

- field values;
- results of other functions;
- expressions.

## Return value

The function returns a date shifted by the specified number of months.

If the source date contains a time value, the time is preserved.

## Features

If the target month does not contain the corresponding day, the function returns the last valid day of that month.

For example:

```text
edate("31/01/2026", 1)
```

Result:

```text
28.02.2026 00:00:00
```

---

The function accepts fractional numeric values.

For example:

```text
edate(sourceDate, 1.5)
```

shifts the date forward by `2` months.

## Examples

**Shifting a date**

```text
edate("15/03/2025", 6)
```

Result:

```text
15.09.2025 00:00:00
```

---

**Using field values and an expression**

If:

- `sourceDate` = `15/03/2026`;
- `numberOfMonths` = `2`;

the expression:

```text
edate(sourceDate, numberOfMonths + 1)
```

returns:

```text
15.06.2026 00:00:00
```

## Errors

The function returns an error if one of the required parameters is empty.

An error occurs if no value is provided for:

- `sourceDate`;
- `numberOfMonths`.

## Related functions

The `edate` function can be combined with other date functions.

You can create the source date using the `date` function and then shift it by the required number of months:

```text
edate(date(15, 3, 2026), 6)
```

Result:

```text
15.09.2026 00:00:00
```

The result of `edate` can be passed to a formatting function:

```text
formatDate(edate(date(15, 3, 2026), 6),"dddd, d MMMM yyyy","en")
```

Result:

```text
Tuesday, 15 September 2026
```