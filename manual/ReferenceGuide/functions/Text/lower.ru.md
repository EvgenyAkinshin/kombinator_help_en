# lower

The `lower` function converts all letters to lowercase.

## Syntax

```text
lower(value)
```

**Parameters:**

- `value` — the value in which the letter case should be changed. Required.

You can use text, a field value, the result of another function, or an expression.

## Return value

The function returns text with all letters converted to lowercase. Numbers, spaces, and other characters are not changed.

For example:

```text
lower("NEW CONTRACT NO. 15")
```

Result:

```text
new contract no. 15
```

## Examples

**Using a field value**

If the `name` field contains:

```text
COMMERCIAL PROPOSAL
```

the expression:

```text
lower(name)
```

returns:

```text
commercial proposal
```

---

**Changing the case of part of a text value**

You can use `lower` together with `mid` when only part of a value should be converted to lowercase.

For example:

```text
lower(mid(text, 2, length(text)))
```

If the `text` field contains:

```text
KOMBINATOR
```

the result is:

```text
ombinator
```

Together with `upper`, you can process the first letter and the remaining part of the text separately:

```text
upper(mid(text, 1, 1)) & lower(mid(text, 2, length(text)))
```

If `text` contains:

```text
kOMBINATOR
```

the result is:

```text
Kombinator
```