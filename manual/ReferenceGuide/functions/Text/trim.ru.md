# trim

The `trim` function removes spaces at the beginning and end of a value. Spaces inside the text are preserved.

## Syntax

```text
trim(value)
```

**Parameters:**

- `value` — the value to process. Required.

You can use text, a field value, the result of another function, or an expression.

## Return value

The function returns the value without leading or trailing spaces.

For example:

```text
trim("  New contract  ")
```

Result:

```text
New contract
```

Spaces between words are preserved.

If you pass an empty string or a field with no value, the function returns an empty value.

## Examples

**Using a field value**

If the `name` field contains:

```text
  Commercial proposal  
```

the expression:

```text
trim(name)
```

returns:

```text
Commercial proposal
```

---

**Using with another function**

You can pass the result directly to another text function:

```text
upper(trim("  New contract  "))
```

Result:

```text
NEW CONTRACT
```