# exp

The `exp` function raises the number `e` to the specified power.

The function is useful for calculations that use exponential values.

## Syntax

```text
exp(value)
```

**Parameters:**

- `value` — the exponent. Required.

You can use:

- a number;
- a numeric field value;
- a text value containing a number;
- the result of another function;
- an expression.

## Return value

The function returns the result of raising `e` to the specified power.

For example:

```text
exp(2)
```

Result:

```text
7.38905609893065
```

If the value is `0`:

```text
exp(0)
```

Result:

```text
1
```

## Examples

**Using a negative value**

```text
exp(-1)
```

Result:

```text
0.36787944117144233
```

---

**Using a decimal value**

```text
exp(1.5)
```

Result:

```text
4.4816890703380645
```

---

**Using a field value and an expression**

If the `value` field contains:

```text
2
```

the expression:

```text
exp(value + 1)
```

returns:

```text
20.085536923187668
```

---

**Using the result of another function**

```text
exp(round(1.6, 0))
```

Result:

```text
7.38905609893065
```

---

**Using a text representation of a number**

```text
exp("2")
```

Result:

```text
7.38905609893065
```

The text value must contain a number that the function can use in the calculation.

## Errors

The `value` parameter is required.

For example:

```text
exp()
```

returns an error.

An error also occurs if a field passed to the function is empty.