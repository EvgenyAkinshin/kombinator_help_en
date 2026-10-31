# log10

The `log10` function calculates the base-10 logarithm of a specified number.

## Syntax

```text
log10(value)
```

**Parameters:**

- `value` — the value for which the base-10 logarithm should be calculated. Required.

You can use:

- a number;
- a numeric field value;
- the result of another function;
- an expression.

## Return value

The function returns the base-10 logarithm of the specified number.

For example:

```text
log10(100)
```

Result:

```text
2
```

## Examples

**Using a field value**

If the `value` field contains:

```text
1000
```

the expression:

```text
log10(value)
```

returns:

```text
3
```

---

**Using an expression**

```text
log10(10 * 10)
```

Result:

```text
2
```

## Related functions

The `log10` function calculates a logarithm with base `10`, while `ln` calculates the natural logarithm.

For example:

```text
log10(100)
```

returns:

```text
2
```

because:

```text
10² = 100
```