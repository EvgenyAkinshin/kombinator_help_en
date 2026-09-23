# date

The `date` function creates a date from separately specified day, month, and year values.

The function is useful when the parts of a date are stored in different fields or calculated directly in an expression.

## Syntax

```text
date(day, month, year)
```

**Parameters:**

- `day` — day of the month. Required. A numeric value from `1` to `31`;
- `month` — month number. Required. A numeric value from `1` to `12`;
- `year` — year. Required. Specified as a number, for example `2026`.

Parameters must be specified in the following order: **day, month, year**.

You can use:

- numbers;
- values from numeric fields;
- numeric expressions.

## Return value

The function returns a date value.

Because hours, minutes, and seconds are not specified, the time is set to `00:00:00`.

For example:

```text
date(12, 8, 2026)
```

Result:

```text
12.08.2026 00:00:00
```

## Features

The specified values must form a valid calendar date.

The `day` parameter can contain a value from `1` to `31`, but the maximum valid value depends on the selected month and year.

If a fractional numeric value is passed, the function converts it when creating the date.

For example:

```text
date(1.5, 5, 2026)
```

Result:

```text
02.05.2026 00:00:00
```

## Examples

**Values from fields**

If the fields contain:

- `day` = `5`;
- `month` = `9`;
- `year` = `2026`;

the expression:

```text
date(day, month, year)
```

returns:

```text
05.09.2026 00:00:00
```

---

**Using an expression**

Calculations can be used in function parameters.

If the fields contain:

- `day` = `5`;
- `month` = `9`;
- `year` = `2026`;

the expression:

```text
date(day + 1, month, year)
```

returns:

```text
06.09.2026 00:00:00
```

## Errors

The function returns an error if the specified values cannot form a valid date.

For example:

```text
date(31, 2, 2026)
```

returns an error because February 2026 does not have 31 days.

An error also occurs if:

- `day` is `0`;
- the month number is greater than `12`;
- the specified day does not exist in the selected month and year;
- one of the required parameters is empty.

For example:

```text
date(29, 2, 2025)
```

returns an error because 2025 does not have February 29.

## Related functions

The `date` function can be combined with other date functions.

A date created with `date` can be:

- split into individual parts using `day`, `month`, and `year`;
- used to retrieve calendar information such as the weekday or week number;
- passed to date formatting functions.

The `date` function can also be used to create a new date based on an existing one.

For example:

```text
date(day(sourceDate), month(sourceDate), year(sourceDate) + 1)
```

This expression keeps the day and month from `sourceDate` and increases the year by `1`.

The resulting date can also be passed directly to `formatDate`:

```text
formatDate(date(5, 9, 2026), "yyyy-MM-dd")
```

Result:

```text
2026-09-05
```

This allows `date` to be used as part of a more complex expression: first create or modify a date, then extract the required information or change how the date is displayed.