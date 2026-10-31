# round

The `round` function rounds a number to the specified number of decimal places.

## Syntax

```text
round(value, decimalPlaces)
```

**Parameters:**

- `value` — the numeric value to round. Required;
- `decimalPlaces` — the number of decimal places to round to. Required.

You can use:

- numbers;
- values from numeric fields;
- results of other functions;
- expressions.

The function does not process text values or values from text fields as numbers.

## Return value

The function returns a rounded numeric value.

For example:

```text
round(125.678, 2)
```

Result:

```text
125.68
```

## Decimal places

The `decimalPlaces` parameter determines the position to which the value is rounded:

- a positive value — rounds to the specified number of decimal places;
- `0` — rounds to the nearest integer;
- a negative value — rounds to tens, hundreds, thousands, and other positions.

For example:

```text
round(125.678, 0)
```

Result:

```text
126
```

---

```text
round(1896, -2)
```

Result:

```text
1900
```

It is recommended to use integers for `decimalPlaces`. A fractional value may be converted when the result is calculated.

## Examples

**Using a field value and an expression**

If the `value` field contains `2`, the expression:

```text
round(value + 10, 2)
```

returns:

```text
12
```

## Errors

Both parameters are required.

For example:

```text
round(125.678)
```

returns an error.

An error also occurs if one of the parameters is empty:

```text
round(emptyField, 2)
```

A text value cannot be used instead of a numeric value, even if the text contains a number:

```text
round("125.678", 2)
```

also returns an error.

## Related functions

Use `roundup` or `rounddown` when you need to round a value up or down.

- `round` — rounds a number to the nearest value;
- `roundup` — rounds a value up;
- `rounddown` — rounds a value down.