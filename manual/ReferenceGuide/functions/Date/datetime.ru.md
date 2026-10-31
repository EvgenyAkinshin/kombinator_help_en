# datetime

The `datetime` function creates a single date and time value from separately specified year, month, day, hour, minute, and second values.

The function is useful when the parts of a date and time are stored in different fields or calculated directly in an expression.

## Syntax

```text
datetime(year, month, day, hours, minutes, seconds)
```

**Parameters:**

- `year` — year. Required numeric parameter;
- `month` — month number. Required numeric parameter. A value from `1` to `12`;
- `day` — day of the month. Required numeric parameter. A value from `1` to `31`;
- `hours` — hours. Required numeric parameter. A value from `0` to `23`;
- `minutes` — minutes. Required numeric parameter. A value from `0` to `59`;
- `seconds` — seconds. Required numeric parameter. A value from `0` to `59`.

Parameters must be specified in the following order: **year, month, day, hours, minutes, seconds**.

You can use:

- numbers;
- values from numeric fields;
- results of other functions;
- expressions.

## Return value

The function returns a date and time value.

For example:

```text
datetime(2026, 8, 11, 14, 30, 15)
```

Result:

```text
11.08.2026 14:30:15
```

## Features

The specified values must form a valid date and time.

Fractional numeric values may be converted when the result is created, so it is recommended to use integers for the parameters.

## Examples

**Using field values and an expression**

If the fields contain:

- `year` = `2026`;
- `month` = `8`;
- `day` = `10`;
- `hours` = `14`;
- `minutes` = `30`;
- `seconds` = `15`;

the expression:

```text
datetime(
    year,
    month,
    day + 1,
    hours,
    minutes,
    seconds
)
```

returns:

```text
11.08.2026 14:30:15
```

## Errors

The function returns an error if the specified values cannot form a valid date and time.

For example:

```text
datetime(2026, 2, 31, 14, 30, 15)
```

returns an error because February 2026 does not have 31 days.

An error also occurs if one of the parameter values is outside the allowed range.

## Related functions

The `datetime` function can be combined with functions that extract individual parts of a date and time.

For example, you can extract all components from an existing date and time value and create a new one:

```text
datetime(year(now()), month(now()), day(now()), hour(now()), minute(now()), second(now()))
```

To display the resulting value in a custom format, use `formatDate`:

```text
formatDate(datetime(2026, 8, 11, 14, 30, 15), "dd MMMM yyyy 'at' HH:mm","en")
```

Result:

```text
11 August 2026 at 14:30
```