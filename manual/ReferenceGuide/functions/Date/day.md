# day

The `day` function returns the day of the month from a specified date.

The function is useful when you need to extract the day from a full date value and use it separately in a document or expression.

## Syntax

```text
day(date)
```

**Parameters:**

- `date` — the date from which the day of the month should be extracted. Required.

You can use:

- a date field value;
- the result of another function that returns a date;
- an expression whose result is a date.

## Return value

The function returns the day of the month as a number from `1` to `31`.

For example:

```text
day("11/08/2026")
```

Result:

```text
11
```

## Examples

**Getting the day from a field value**

If the `contractDate` field contains:

```text
11/08/2026
```

the expression:

```text
day(contractDate)
```

returns:

```text
11
```

---

**Getting the current day of the month**

You can get the current day from the result of `Today()`:

```text
day(Today())
```

If the document is generated on September 2, 2026, the result is:

```text
2
```

## Errors

The function returns an error if the supplied value is not a valid date.

An error also occurs if the required parameter is empty.

## Related functions

The `day` function can be combined with other date functions.

For example, you can extract the parts of an existing date and create a new date:

```text
date(day(sourceDate), month(sourceDate), year(sourceDate) + 1)
```

This expression keeps the day and month from `sourceDate` and increases the year by `1`.

You can also get the day of the month from a date calculated by another function:

```text
day(dateshift(sourceDate, 10))
```

In this case, `dateshift` first calculates the new date, and `day` returns the day of the month from the resulting value.