# contains

The **`contains`** function checks whether a string contains a specified substring. It can be used in conditions where document generation depends on the presence of certain text in a value.

## Syntax

```text
contains(String, Substring, Match case)
```

- **`String`** — required. The source string in which the search is performed.
- **`Substring`** — required. The sequence of characters to search for within the string.
- **`Match case`** — optional Boolean parameter. Determines whether the comparison is case-sensitive.

If **`Match case`** is omitted, the comparison is case-sensitive by default.

To perform a case-insensitive search, pass `false` as the third argument.

## Return Value

The function returns a Boolean value:

- `True` — the specified substring is found in the string.
- `False` — the specified substring is not found in the string.

The returned value can be used in conditions and other expressions.

## Notes

If **`Substring`** is empty, the function returns `true`.

## Example

Suppose the `PaymentTerms` field contains the following value:

```text
Payment is due within 10 business days after delivery of the goods
```

Check whether the field value contains `DELIVERY`, ignoring case:

```text
contains(PaymentTerms, "DELIVERY", false)
```

Result:

```text
true
```

Since the third argument is set to `false`, differences in letter case do not affect the result.