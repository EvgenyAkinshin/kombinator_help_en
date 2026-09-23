# year

The `year` function returns the year from a specified date.

The function is useful when you need to extract the year from a full date value and use it separately in a document or expression.

## Syntax

```text
year(date)
```

**Parameters:**

- `date` — the date from which the year should be extracted. Required.

You can use:

- a date field value;
- the result of another function that returns a date;
- an expression whose result is a date.

## Return value

The function returns the year as a number.

For example:

```text
year("11/08/2026")
```

Result:

```text
2026
```

## Examples

**Getting the year from a field value**

If the `contractDate` field contains:

```text
11/08/2026
```

the expression:

```text
year(contractDate)
```

returns:

```text
2026
```

---

**Getting the current year**

You can get the current year from the result of `Today()`:

```text
year(Today())
```

If the document is generated in 2026, the result is:

```text
2026
```

## Errors

The function returns an error if the supplied value is not a valid date.

An error also occurs if the required parameter is empty.

For example, if the field contains regular text instead of a date value, the function cannot extract the year from it.

## Related functions

The `year` function can be combined with other date functions.

For example, you can extract the parts of an existing date, change the year, and create a new date:

```text
date(day(sourceDate), month(sourceDate), year(sourceDate) + 1)
```

This expression keeps the day and month from `sourceDate` and increases the year by `1`.

You can also extract the year from a date returned by another function:

```text
year(edate(sourceDate, 6))
```

In this case, `edate` first calculates the new date, and `year` returns the year from the resulting value.