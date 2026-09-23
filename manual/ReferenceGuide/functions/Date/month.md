# month

The `month` function returns the month number from a specified date.

The function is useful when you need to extract the month from a full date value and use it separately in a document or expression.

## Syntax

```text
month(date)
```

**Parameters:**

- `date` — the date from which the month number should be extracted. Required.

You can use:

- a date field value;
- the result of another function that returns a date;
- an expression whose result is a date.

## Return value

The function returns the month number as a value from `1` to `12`.

For example:

```text
month("11/08/2026")
```

Result:

```text
8
```

## Examples

**Getting the month from a field value**

If the `contractDate` field contains:

```text
11/08/2026
```

the expression:

```text
month(contractDate)
```

returns:

```text
8
```

---

**Getting the current month**

You can get the current month from the result of `Today()`:

```text
month(Today())
```

If the document is generated in September, the result is:

```text
9
```

## Errors

The function returns an error if the supplied value is not a valid date.

An error also occurs if the required parameter is empty.

## Related functions

The `month` function can be combined with other date functions.

For example, you can extract the parts of an existing date and create a new date:

```text
date(day(sourceDate), month(sourceDate), year(sourceDate) + 1)
```

This expression keeps the day and month from `sourceDate` and increases the year by `1`.

You can also get the month number from a date calculated by another function:

```text
month(edate(sourceDate, 6))
```

In this case, `edate` first calculates the new date, and `month` returns the month number from the resulting value.