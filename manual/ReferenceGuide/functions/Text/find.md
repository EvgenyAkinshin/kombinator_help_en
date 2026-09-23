# find

The `find` function searches for a specified fragment in a string and returns the position where it begins.

The function is useful when the position of the required text is not known in advance. The returned position can be used in other functions, such as `mid`, to extract a specific part of a string.

## Syntax

```text
find(string, substring, [startPosition], [matchCase])
```

**Parameters:**

- `string` — the value in which to search. Required;
- `substring` — the text or character to find. Required;
- `startPosition` — the position from which to start the search. Optional. By default, the search starts from the first character;
- `matchCase` — determines whether the search is case-sensitive. Optional. By default, the search is case-insensitive.

You can use text, field values, results of other functions, and expressions as parameters.

## Return value

If the specified fragment is found, the function returns the position of its first character. Counting starts from `1`.

For example:

```text
find("Acme Company", "Com", 1, false)
```

Result:

```text
6
```

If the specified text is not found, the function returns `null`.

## Examples

**Finding a character in a field value**

If the `documentNumber` field contains:

```text
Contract No.125/2026
```

the expression:

```text
find(documentNumber, "No.")
```

returns the position where `No.` begins.

---

**Extracting text after a found fragment**

You can pass the result of `find` to `mid` when you need to extract a part of text whose position is not known in advance.

For example:

```text
mid(
    documentNumber,
    find(documentNumber, "No.") + length("No."),
    length(documentNumber)
)
```

If `documentNumber` contains:

```text
Contract No.125/2026
```

the result is:

```text
125/2026
```

Here, `find` determines the position of `No.`, while `length("No.")` moves the starting position to the first character after it. The `length` function allows the remaining text to be extracted through the end of the string.

---

**Searching from a specific position**

If the same fragment appears more than once, you can start the search from a specified position instead of the first character:

```text
find(text, "/", 10)
```

In this case, the function searches for `/` starting from the tenth character of the string.

---

**Case-sensitive search**

Set `matchCase` to `true` when the letter case must match:

```text
find("Contract CONTRACT", "CONTRACT", 1, true)
```

The function searches for the substring using the exact letter case.