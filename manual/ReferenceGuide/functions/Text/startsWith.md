# startsWith

The **`startsWith`** function checks whether a string begins with a specified substring. It can be used in conditions where document generation depends on the beginning of a text value.

## Syntax

```text
startsWith(String, Substring, Match case)
```

- **`String`** — required. The source string whose beginning is to be checked.
- **`Substring`** — required. The sequence of characters that must match the beginning of the string.
- **`Match case`** — optional Boolean parameter. Determines whether the comparison is case-sensitive.

If **`Match case`** is omitted, the comparison is case-sensitive by default.

To perform a case-insensitive comparison, pass `false` as the third argument.

## Return Value

The function returns a Boolean value:

- `True` — the string begins with the specified substring.
- `False` — the string does not begin with the specified substring.

The returned value can be used in conditions and other expressions.

## Notes

If **`Substring`** is empty, the function returns `true`.

## Example

Suppose the **`ProductName`** field contains the following value:

```text
Equipment mounting kit
```

Check whether the field value begins with `EQUIPMENT`, ignoring case:

```text
startsWith(ProductName, "EQUIPMENT", false)
```

Result:

```text
true
```

Since the third argument is set to `false`, differences in letter case do not affect the result.