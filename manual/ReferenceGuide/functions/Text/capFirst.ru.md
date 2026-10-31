# capFirst

The `capFirst` function makes the first letter of a string uppercase and converts all remaining letters to lowercase.

## Syntax

```text
capFirst(expression)
```

**Parameters:**

- `expression` — a text value or expression that returns a string. In the function settings, this parameter is **Expression**.

## Return value

The function returns a string value with the letter case changed.

## Examples

### Formatting text

Expression:

```text
capFirst("GENERAL MANAGER")
```

returns:

```text
General manager
```

### Formatting a field value

Suppose the `position` field contains:

```text
HEAD OF LEGAL DEPARTMENT
```

Expression:

```text
capFirst(position)
```

returns:

```text
Head of legal department
```

## Errors

If `expression` returns a value of another type, the function returns an error.