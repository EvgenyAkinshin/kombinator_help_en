# ln

The `ln` function calculates the natural logarithm of a specified number.

## Syntax

```text
ln(value)
```

**Parameters:**

- `value` — the value for which the natural logarithm should be calculated. Required.

You can use:

- a number;
- a numeric field value;
- a text value containing a number;
- the result of another function;
- an expression.

## Return value

The function returns the natural logarithm of the specified number.

For example:

```text
ln(2)
```

Result:

```text
0.6931471805599453
```

## Examples

**Using a text representation of a number**

```text
ln("2")
```

Result:

```text
0.6931471805599453
```

The text value must contain a number that the function can use in the calculation.

## Errors

The `value` parameter is required.

For example:

```text
ln()
```

returns an error.

An error also occurs if a field passed to the function is empty.

## Related functions

The `ln` function is the inverse of `exp`.

For example:

```text
ln(exp(2))
```

Result:

```text
2
```