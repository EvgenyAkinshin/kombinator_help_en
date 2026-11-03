# decline_RU

The **`decline_RU`** function changes the grammatical case and number of a word or phrase.

## Syntax

```text
decline_RU(Expression of the word, Grammatical case, Number)
```

**Parameters:**

- **`Expression of the word`** — required. The text value to be declined.
- **`Grammatical case`** — required. Specifies the grammatical case in which the text should be returned.
- **`Number`** — required. Specifies whether the text should be returned in singular or plural form.

The following values are available for the **`Grammatical case`** parameter:

| Value | Russian case questions |
|---|---|
| `GrammaticalCase_RU.Nominative` | кто? что? |
| `GrammaticalCase_RU.Genitive` | кого? чего? |
| `GrammaticalCase_RU.Dative` | кому? чему? |
| `GrammaticalCase_RU.Accusative` | кого? что? |
| `GrammaticalCase_RU.Instrumental` | кем? чем? |
| `GrammaticalCase_RU.Prepositional` | о ком? о чём? |

The following values are available for the **`Number`** parameter:

- `GrammaticalNumber_RU.Singular` — singular form.
- `GrammaticalNumber_RU.Plural` — plural form.

## Return Value

The function returns a text value in the specified grammatical case and number.

## Notes

The **`decline_RU`** function is not intended for declining full names. To decline full names, use the dedicated function for processing personal names.

## Examples

### Declining a Job Title

Suppose the `Position` field contains:

```text
Генеральный директор
```

The expression:

```text
decline_RU(
    Position,
    GrammaticalCase_RU.Genitive,
    GrammaticalNumber_RU.Singular
)
```

Returns:

```text
Генерального директора
```

### Declining a Phrase

Suppose the `Name` field contains:

```text
договор поставки
```

The expression:

```text
decline_RU(
    Name,
    GrammaticalCase_RU.Instrumental,
    GrammaticalNumber_RU.Singular
)
```

Returns:

```text
договором поставки
```

### Changing the Grammatical Number

Suppose the `Name` field contains:

```text
ответственное лицо
```

The expression:

```text
decline_RU(
    Name,
    GrammaticalCase_RU.Nominative,
    GrammaticalNumber_RU.Plural
)
```

Returns:

```text
ответственные лица
```

## Errors

If the source text contains numbers, special characters, or punctuation marks, the function may fail to process the value and return an error.

For example:

```text
2 юриста, 1 бухгалтер
```

It is recommended to store numeric quantities and the text to be declined in separate fields.