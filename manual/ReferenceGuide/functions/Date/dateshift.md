# dateshift

The `dateshift` function shifts a source date forward or backward by the specified number of days.

The function is useful when you need to calculate a date relative to another date, for example, to determine a deadline several days later or get a date from a previous period.

## Syntax

```text
dateshift(sourceDate, numberOfDays)
```

**Parameters:**

- `sourceDate` — the date from which the shift is calculated. Required;
- `numberOfDays` — the number of days by which the date should be shifted. Required numeric parameter.

A positive `numberOfDays` value shifts the date forward, while a negative value shifts it backward. A value of `0` returns the source date without shifting it.

You can use:

- field values;
- results of other functions;
- expressions.

## Return value

The function returns a date shifted by the specified number of days.

If the source date contains a time value, the time is preserved.

## Features

The function automatically handles transitions between months and years.

For example:

```text
dateshift("31/12/2025", 1)
```

Result:

```text
01.01.2026 00:00:00
```

---

If the source date contains a time value, the time is preserved after the shift.

For example:

```text
dateshift("31/03/2025 14:30:25", 1)
```

Result:

```text
01.04.2025 14:30:25
```

---

The function accepts fractional numeric values.

For example:

```text
dateshift("31/03/2025", 1.5)
```

Result:

```text
02.04.2025 00:00:00
```

## Examples

**Shifting a date forward**

```text
dateshift("31/03/2025", 20)
```

Result:

```text
20.04.2025 00:00:00
```

---

**Shifting a date backward**

```text
dateshift("31/03/2025", -20)
```

Result:

```text
11.03.2025 00:00:00
```

---

**Using a field value and an expression**

If:

- `sourceDate` = `02/09/2026`;
- `numberOfDays` = `3`;

the expression:

```text
dateshift(sourceDate, numberOfDays + 1)
```

returns:

```text
06.09.2026 00:00:00
```

## Errors

The function returns an error if one of the required parameters is empty.

An error occurs if no value is provided for:

- `sourceDate`;
- `numberOfDays`.

## Related functions

The `dateshift` function can be combined with other date functions.

You can create the source date using the `date` function and then shift it by the required number of days:

```text
dateshift(date(31, 3, 2025), 20)
```

Result:

```text
20.04.2025 00:00:00
```

The result can be passed to a formatting function:

```text
formatDate(dateshift(date(31, 3, 2025), 20),"dddd, d MMMM yyyy","en")
```

Result:

```text
Sunday, 20 April 2025
```