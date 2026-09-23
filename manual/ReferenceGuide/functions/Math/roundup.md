# roundup

The `roundup` function rounds a number to the specified number of decimal places, increasing the last digit of the result.

## Syntax

```text
roundup(value, decimalPlaces)
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

The function returns a number rounded away from zero.

For example:

```text
roundup(125.671, 2)
```

Result:

```text
125.68
```

## Decimal places

The `decimalPlaces` parameter determines the position to which the value is rounded:

- a positive value — rounds to the specified number of decimal places;
- `0` — rounds to an integer;
- a negative value — rounds to tens, hundreds, thousands, and other positions.

For example:

```text
roundup(1891, -2)
```

Result:

```text
1900
```

## Features

For positive numbers, the result is rounded up to the nearest value with the specified number of decimal places.

For negative numbers, rounding is also performed away from zero:

```text
roundup(-125.671, 2)
```

Result:

```text
-125.68
```

## Examples

**Using a field value and an expression**

If the `value` field contains `125.671`, the expression:

```text
roundup(value + 10, 2)
```

returns the result rounded away from zero to two decimal places.

## Related functions

Different rounding methods are available:

- `round` — rounds a number to the nearest value;
- `roundup` — rounds a number away from zero;
- `rounddown` — rounds a number toward zero.