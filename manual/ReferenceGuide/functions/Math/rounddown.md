# rounddown

The `rounddown` function rounds a number to the specified number of decimal places without increasing the last retained digit.

## Syntax

```text
rounddown(value, decimalPlaces)
```

**Parameters:**

- `value` — the numeric value to round. Required;
- `decimalPlaces` — the number of decimal places to round to. Required.

You can use:

- numbers;
- values from numeric fields;
- results of other functions;
- expressions.

## Return value

The function returns a rounded numeric value.

For example:

```text
rounddown(125.678, 2)
```

Result:

```text
125.67
```

When rounding to two decimal places, the retained digits `67` remain unchanged.

## Decimal places

The `decimalPlaces` parameter determines the position to which the value is rounded:

- a positive value — rounds to the specified number of decimal places;
- `0` — rounds to an integer;
- a negative value — rounds to tens, hundreds, thousands, and other positions.

For example:

```text
rounddown(1896, -2)
```

Result:

```text
1800
```

## Examples

**Using a field value and an expression**

If the `value` field contains `125.678`, the expression:

```text
rounddown(value + 10, 2)
```

returns:

```text
135.67
```

## Related functions

Different rounding methods are available:

- `round` — rounds a number to the nearest value;
- `roundup` — increases the last retained digit when rounding;
- `rounddown` — keeps the last retained digit unchanged.