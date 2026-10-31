# time

The `time` function creates a time value from separately specified hours, minutes, and seconds.

The function is useful when the parts of a time value are stored in different fields or calculated directly in an expression.

## Syntax

```text
time(hours, minutes, seconds)
```

**Parameters:**

- `hours` — hours. Required. A numeric value from `0` to `23`;
- `minutes` — minutes. Required. A numeric value from `0` to `59`;
- `seconds` — seconds. Required. A numeric value from `0` to `59`.

Parameters must be specified in the following order: **hours, minutes, seconds**.

You can use:

- numbers;
- values from numeric fields;
- results of other functions;
- expressions.

## Return value

The function returns a time value with the specified hours, minutes, and seconds.

In the full representation of the result, the technical date `01.01.0001` is used.

For example:

```text
time(14, 30, 0)
```

Result:

```text
01.01.0001 14:30:00
```

## Examples

**Using field values and an expression**

If:

- `hours` = `13`;
- `minutes` = `30`;
- `seconds` = `0`;

the expression:

```text
time(hours + 1, minutes, seconds)
```

returns:

```text
01.01.0001 14:30:00
```

## Errors

The function returns an error if one of the parameters is outside the allowed range.

For example:

```text
time(24, 0, 0)
```

```text
time(23, 60, 0)
```

```text
time(23, 59, 60)
```

An error also occurs if one of the required parameters is empty.

## Related functions

The `time` function can be combined with other date and time functions.

For example, the `hour`, `minute`, and `second` functions can extract individual parts of the current time and use them to create a new time value:

```text
time(hour(now()), minute(now()), second(now()))
```

To display the time without the technical date `01.01.0001`, use `formatDate`:

```text
formatDate(time(14, 30, 25), "HH:mm:ss")
```

Result:

```text
14:30:25
```