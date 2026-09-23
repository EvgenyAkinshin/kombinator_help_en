# mid

The `mid` function extracts part of a text value starting from a specified position.

The function is useful when a single value contains several parts and you need to extract a specific fragment, such as a document number, code, detail, or text that follows a particular word.

## Syntax

```text
mid(text, position, length)
```

**Parameters:**

- `text` — the source value from which part of the text should be extracted. Required;
- `position` — the character position where the required fragment starts. Required. Counting starts from `1`;
- `length` — the number of characters to extract. Required.

You can use text, a field value, the result of another function, or an expression.

The position and length do not have to be specified as fixed numbers. You can calculate them using other functions, such as `find` and `length`.

## Return value

The function returns the specified part of the source text.

For example:

```text
mid("AGR-2026-125", 5, 4)
```

Result:

```text
2026
```

In this expression, `5` specifies the starting character, and `4` specifies how many characters to extract.

## Examples

**Extracting text from a known position to the end of the string**

If you know where the required part starts but its length may vary, you can use `length` as the last parameter.

For example, the `documentNumber` field contains:

```text
AGR-125/2026
```

The expression:

```text
mid(documentNumber, 5, length(documentNumber))
```

returns:

```text
125/2026
```

This approach also works with values of different lengths:

```text
AGR-15/2026
AGR-125/2026
AGR-12548/2026
```

The starting position remains the same — the fifth character — while `length` allows the function to extract the remaining part of the value through the end of the string.

---

**Extracting text after a specific fragment**

If the required part may appear at different positions in the string, you can determine its starting position using `find`.

For example, the `details` field contains:

```text
Tax ID: 7701234567; Reg. No.: 770101001
```

To extract only the registration number:

```text
mid(
    details,
    find(details, "Reg. No.: ") + length("Reg. No.: "),
    length(details)
)
```

Result:

```text
770101001
```

Here:

- `find` determines where `Reg. No.: ` begins;
- `length("Reg. No.: ")` skips the label and the space after it;
- `length(details)` allows the remaining text to be extracted through the end of the string;
- `mid` returns the required part of the value.

This approach is useful when the text before the required fragment may vary and its exact position cannot be known in advance.

> If `find` does not find the specified fragment, it returns `null`. In this case, `mid` cannot evaluate the expression and returns an error because all of its parameters are required.

---

**Extracting text between two fragments**

You can use `find` to calculate both the starting position and the length of the required part.

For example, the `basis` field contains:

```text
Supply Agreement No.125/2026 dated 14/09/2026
```

To extract only the agreement number:

```text
125/2026
```

use:

```text
mid(
    basis,
    find(basis, "No.") + length("No."),
    find(basis, " dated ") - find(basis, "No.") - length("No.")
)
```

Result:

```text
125/2026
```

In this case:

- the start is determined by `No.`;
- the end is determined by ` dated `;
- the number of characters between them is calculated directly in the expression.

The expression therefore also works with document numbers of different lengths, for example:

```text
No.15/2026
No.125/2026
No.12548/2026
```