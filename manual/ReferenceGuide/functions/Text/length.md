# length

The `length` function counts the number of characters in text, a number, or a field value.

## Syntax

```text
length(value)
```

**Parameters:**

- `value` — the value for which the number of characters should be determined. Required.

You can use text, a field value, the result of another function, or an expression.

## Return value

The function returns the number of characters as a number. Letters, digits, spaces, and other characters are all included in the count.

For example:

```text
length("New contract")
```

Result:

```text
12
```

If you pass an empty string or a field with no value, the function returns `0`.

## Examples

**Using a field value**

If the `name` field contains:

```text
Kombinator
```

the expression:

```text
length(name)
```

returns:

```text
10
```

---

**Using with another function**

`length` is often used together with `mid` when you need to extract part of a text value through the end of the string:

```text
mid(documentNumber, 5, length(documentNumber))
```

If `documentNumber` contains:

```text
DOC-125/2026
```

the result is:

```text
125/2026
```