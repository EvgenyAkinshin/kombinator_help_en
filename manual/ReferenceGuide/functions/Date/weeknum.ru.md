# weeknum

The `weeknum` function determines the week number for a specified date.

The function is useful when you need to use the week number in a document, condition, or other expression.

## Syntax

```text
weeknum(date, [returnType])
```

**Parameters:**

- `date` — the date for which the week number should be determined. Required;
- `returnType` — a code that defines how weeks are calculated. Optional.

For the `date` parameter, you can use:

- a Date field value;
- a Date/Time field value;
- a text value containing a valid date;
- the result of another function that returns a date;
- an expression whose result is a date.

For `returnType`, values from `11` to `17` and from `21` to `27` are supported.

If `returnType` is not specified, `11` is used.

## Return value

The function returns the week number as a number.

For example:

```text
weeknum("12/08/2026")
```

Result:

```text
33
```

The same result is returned when `11` is specified explicitly:

```text
weeknum("12/08/2026", 11)
```

Result:

```text
33
```

## Week numbering rules

Return types `11–17` and `21–27` use different rules for determining the first week of the year.

**Return types `11–17`**

The week containing January 1 is considered the first week of the year.

The code defines the first day of the week:

- `11` — Monday;
- `12` — Tuesday;
- `13` — Wednesday;
- `14` — Thursday;
- `15` — Friday;
- `16` — Saturday;
- `17` — Sunday.

For example:

```text
weeknum("01/01/2022", 11)
```

Result:

```text
1
```

---

**Return types `21–27`**

With this numbering system, the first days of January may belong to the last week of the previous year.

The code also defines the first day of the week:

- `21` — Monday;
- `22` — Tuesday;
- `23` — Wednesday;
- `24` — Thursday;
- `25` — Friday;
- `26` — Saturday;
- `27` — Sunday.

For example:

```text
weeknum("01/01/2022", 21)
```

Result:

```text
52
```

For the same date, return type `27` also returns:

```text
52
```

## Examples

**Getting the week number from a field value**

If the `documentDate` field contains:

```text
03/09/2026
```

the expression:

```text
weeknum(documentDate)
```

returns:

```text
36
```

---

**Using a date and time value**

The function can also process a value containing both a date and time:

```text
weeknum("03/09/2026 15:53:21")
```

Result:

```text
36
```

The time component does not affect the week number, which is determined by the date.

## Errors

The function returns an error if:

- the required parameter is empty;
- the supplied value cannot be processed as a valid date;
- `returnType` contains a value outside the supported ranges `11–17` and `21–27`.

For example, return type values `10`, `18`, `20`, and `28` return an error.

## Related functions

The `weeknum` function can be used with functions that return or modify dates.

For example, you can get the current week number using `Today()`:

```text
weeknum(Today())
```

You can also determine the week number after shifting a date:

```text
weeknum(dateshift(sourceDate, 7))
```

First, `dateshift` calculates the new date, and then `weeknum` returns the week number for the resulting value.