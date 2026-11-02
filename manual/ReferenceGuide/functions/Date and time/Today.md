# Today

The `Today` function returns the current date at the time the document is generated.

The function is useful when you need to automatically insert the current date into a document or use it in calculations.

## Syntax

```text
Today()
```

**Parameters:**

The function does not accept any parameters.

## Return value

The function returns the current date with the time set to `00:00:00`.

For example, if the document is generated on September 2, 2026:

```text
Today()
```

Result:

```text
02.09.2026 00:00:00
```

## Features

The function value is determined **at the time the document is generated**.

Therefore, if the same template is generated on different days, `Today()` returns the corresponding generation date.

## Examples

*Using the current date in a calculation**

The current date can be used as the source value for other functions.

For example:

```text
edate(Today(), 1)
```

If the document is generated on September 2, 2026, the result is:

```text
02.10.2026 00:00:00
```

---

**Calculating the difference between dates**

The function can be used to calculate the number of days between the current date and another date:

```text
datediff(Today(), endDate)
```

The result depends on the value of `endDate`.

## Related functions

The result of `Today` can be used with other date functions.

For example, you can immediately display the current date in the required format:

```text
formatDate(Today(),"dddd, d MMMM yyyy","en")
```

If the document is generated on September 22, 2026, the result is:

```text
Tuesday, 22 September 2026
```

The `Today` function can also be combined with date calculation functions such as `edate`, `bomonth`, `eomonth`, and `datediff`.