# endsWith

The **`endsWith`** function checks whether a string ends with a specified substring. It can be used in conditions where document generation depends on the ending of a text value.

## Syntax

```text
endsWith(String, Substring, Match case)
```

- **`String`** — required. The source string whose ending is to be checked.
- **`Substring`** — required. The sequence of characters that must match the end of the string.
- **`Match case`** — optional Boolean parameter. Determines whether the comparison is case-sensitive.

If **`Match case`** is omitted, the comparison is case-sensitive by default.

To perform a case-insensitive comparison, pass `false` as the third argument.

## Return Value

The function returns a Boolean value:

- `True` — the string ends with the specified substring.
- `False` — the string does not end with the specified substring.

The returned value can be used in conditions and other expressions.

## Notes

If **`Substring`** is empty, the function returns `true`.

## Example

Check whether the string ends with `AGREEMENT`, ignoring case:

```text
endsWith("Supply agreement", "AGREEMENT", false)
```

Result:

```text
true
```

Since the third argument is set to `false`, differences in letter case do not affect the result.