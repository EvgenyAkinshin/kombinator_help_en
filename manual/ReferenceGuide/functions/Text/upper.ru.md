# upper

The `upper` function converts all letters to uppercase.

## Syntax

```text
upper(value)
```

**Parameters:**

- `value` — the value in which the letter case should be changed. Required.

You can use text, a field value, the result of another function, or an expression.

## Return value

The function returns the value with all letters converted to uppercase.

For example:

```text
upper("New contract No. 15")
```

Result:

```text
NEW CONTRACT NO. 15
```

Numbers and other characters are not changed.

If you pass an empty string or a field with no value, the function returns an empty value.

## Examples

**Using a field value**

If the `name` field contains:

```text
Commercial proposal
```

the expression:

```text
upper(name)
```

returns:

```text
COMMERCIAL PROPOSAL
```

---

**Changing the case of part of a text value**

You can use `upper` together with `mid` when only part of a value should be converted to uppercase:

```text
upper(mid(text, 1, 1))
```

If the `text` field contains:

```text
kombinator
```

the result is:

```text
K
```