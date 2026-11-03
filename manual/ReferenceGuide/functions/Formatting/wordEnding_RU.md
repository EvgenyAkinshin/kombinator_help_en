# wordEnding_RU

The **`wordEnding_RU`** function inserts the appropriate word ending depending on the gender and number of the value in a text field.

## Syntax

```text
wordEnding_RU(Expression of the word, Masculine gender, Feminine gender, Neuter gender, Plural)
```

**Parameters:**

- **`Expression of the word`** — the identifier of the text field whose value is used to determine gender and number.
- **`Masculine gender`** — the ending for the masculine gender.
- **`Feminine gender`** — the ending for the feminine gender.
- **`Neuter gender`** — the ending for the neuter gender.
- **`Plural`** — the ending for the plural form.

Endings must be specified in double quotation marks.

For example:

```text
wordEnding_RU(FullName, "ый", "ая", "ое", "ые")
```

| Field value | Returned ending |
|---|---|
| Masculine gender | `ый` |
| Feminine gender | `ая` |
| Neuter gender | `ое` |
| Plural | `ые` |

## Return Value

The function returns one of the specified text endings.

For example, if the `FullName` field contains the full name of a man:

```text
Иванов Иван Иванович
```

The expression:

```text
wordEnding_RU(FullName, "ый", "ая", "ое", "ые")
```

Returns:

```text
ый
```

## Examples

### Salutation by Full Name

Expression:

```text
"Уважаем" & wordEnding_RU(FullName, "ый", "ая", "ое", "ые")
```

If the `FullName` field contains:

```text
Иванов Иван Иванович
```

The result is:

```text
Уважаемый
```

If the `FullName` field contains:

```text
Иванова Анна Сергеевна
```

The result is:

```text
Уважаемая
```

## Errors

The value used to determine gender and number must contain text suitable for morphological analysis.

If it contains digits, quotation marks, or punctuation marks, the function may fail to determine the correct form or may return an error.