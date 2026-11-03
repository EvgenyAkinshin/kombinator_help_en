# transliterate_RU

The **`transliterate_RU`** function converts Cyrillic text into Latin characters.

## Syntax

```text
transliterate_RU(Value)
```

**Parameters:**

- **`Value`** — required. The text value to be transliterated into Latin characters.

## Return Value

The function returns a text value in which Cyrillic letters are replaced with their corresponding Latin characters.

## Notes

Transliteration is performed character by character. The capitalization of the original text is preserved.

For example:

| Cyrillic | Latin |
|---|---|
| `Ж` | `Zh` |
| `Ю` | `Iu` |
| `Я` | `Ia` |
| `Й` | `I` |

## Examples

### Transliterating a Full Name

Suppose the `FullName` field contains:

```text
Петрова Ирина Сергеевна
```

The expression:

```text
transliterate_RU(FullName)
```

Returns:

```text
Petrova Irina Sergeevna
```

## Using with Other Functions

The **`transliterate_RU`** function can be used as an argument in other functions that process text.

For example, to transliterate a value and convert the result to lowercase:

```text
lower(transliterate_RU(FullName))
```

Suppose the `FullName` field contains:

```text
Петрова Ирина Сергеевна
```

The result is:

```text
petrova irina sergeevna
```