# proper

The `proper` function capitalizes the first letter of each word and converts the remaining letters to lowercase.

## Syntax

```text
proper(value)
```

**Parameters:**

- `value` — the value in which the letter case should be changed. Required.

You can use text, a field value, the result of another function, or an expression.

## Return value

The function returns a value in which each word begins with an uppercase letter.

For example:

```text
proper("john SMITH")
```

Result:

```text
John Smith
```

Numbers and other characters are not changed.

## Examples

**Using a field value**

If the `fullName` field contains:

```text
john smith
```

the expression:

```text
proper(fullName)
```

returns:

```text
John Smith
```

---

**Using with another function**

You can remove leading and trailing spaces before changing the letter case:

```text
proper(trim("  john smith  "))
```

Result:

```text
John Smith
```