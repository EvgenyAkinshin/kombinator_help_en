# datediff

The `datediff` function returns the difference between two dates in days.

The function is useful when you need to determine the duration of a period between two dates, for example, the number of days between the start and end of an event or document.

## Syntax

```text
datediff(startDate, endDate)
```

**Parameters:**

- `startDate` — the date from which the difference is calculated. Required;
- `endDate` — the date up to which the difference is calculated. Required.

You can use:

- field values;
- results of other functions;
- expressions.

## Return value

The function returns a numeric value representing the difference between the dates in days.

The sign of the result depends on the order of the dates:

- if `endDate` is later than `startDate`, the result is positive;
- if `endDate` is earlier than `startDate`, the result is negative;
- if the dates are the same, the result is `0`.

## Features

The order of the parameters affects the result.

For example:

```text
datediff("31/03/2025", "04/06/2025")
```

Result:

```text
65
```

If the dates are reversed:

```text
datediff("04/06/2025", "31/03/2025")
```

Result:

```text
-65
```

---

If the dates are the same, the function returns `0`:

```text
datediff("15/04/2025", "15/04/2025")
```

Result:

```text
0
```

---

The function also accepts date and time values.

For example:

```text
datediff("15/04/2025 12:00:00","16/04/2025 00:00:00")
```

Result:

```text
0
```

> In this example, the difference between the values is less than one full day, so the function returns `0`.

## Examples

**Calculating the number of days between dates**

```text
datediff("15/04/2025", "16/04/2025")
```

Result:

```text
1
```

---

**Using results of other functions**

Dates created by other functions can be passed as parameters:

```text
datediff(date(15, 4, 2025), date(20, 4, 2025))
```

Result:

```text
5
```

## Errors

The function returns an error if one of the required parameters is empty.

An error occurs if no value is provided for:

- `startDate`;
- `endDate`.

## Related functions

The `datediff` function can be combined with other date functions.

For example, you can calculate the number of days between today's date and a date shifted by one month:

```text
datediff(today(), edate(today(), 1))
```

In the tested example, the result is:

```text
30
```

The dates can also be created using the `date` function:

```text
datediff(date(15, 4, 2025), date(20, 4, 2025))
```

Result:

```text
5
```

This allows `datediff` to be used as part of a more complex expression when the start or end date is determined by another function.