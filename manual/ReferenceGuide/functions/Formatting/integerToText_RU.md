# integerToText_RU

The **`integerToText_RU`** function displays an integer in digits and/or words and adjusts the grammatical form of a specified word to agree with the number.

For example, the number `3` and the word `документ` can be displayed as:

```text
3 (три) документа
```

## Syntax

```text
integerToText_RU(Number expression, Expression of the word, Custom format, Numeral type, Grammatical case, Thousands separator)
```

**Parameters:**

- **`Number expression`** — required. The integer value to be formatted.
- **`Expression of the word`** — required. The word that must agree with the number.
- **`Custom format`** — required. Specifies how the number and word are displayed.
- **`Numeral type`** — required. Specifies whether a cardinal or ordinal numeral is used.
- **`Grammatical case`** — optional. Specifies the grammatical case in which the numeral and word are displayed.
- **`Thousands separator`** — optional. Specifies the character used to separate digit groups in the numeric representation.

### Custom Format

The custom format string determines the content and order of the result.

The following symbols are supported:

| Symbol | Description |
|---|---|
| `i` | Number in digits |
| `ii` | Number written out in words |
| `W` | Word in the appropriate grammatical form |

For example, if the number is `3` and the word is `"документ"`:

| Format | Result |
|---|---|
| `"i W"` | `3 документа` |
| `"ii W"` | `три документа` |
| `"i (ii) W"` | `3 (три) документа` |

Spaces and punctuation marks in the format string are preserved in the result.

Alphabetic characters other than the supported format symbols are ignored. To include text that must remain unchanged, enclose it in single quotation marks (`'`).

Double quotation marks (`"`) are not allowed inside the custom format itself.

### Numeral Type

The following options are available for the **`Numeral type`** parameter:

- **`Cardinal`** — a cardinal numeral indicating quantity.
- **`Ordinal`** — an ordinal numeral indicating position or order.

### Grammatical Case

The following values are available for the **`Grammatical case`** parameter:

| Value | Russian case questions |
|---|---|
| `GrammaticalCase_RU.Nominative` | кто? что? |
| `GrammaticalCase_RU.Genitive` | кого? чего? |
| `GrammaticalCase_RU.Dative` | кому? чему? |
| `GrammaticalCase_RU.Accusative` | кого? что? |
| `GrammaticalCase_RU.Instrumental` | кем? чем? |
| `GrammaticalCase_RU.Prepositional` | о ком? о чём? |

## Return Value

The function returns a text value formatted according to the specified parameters.

## Notes

The grammatical form of the word is determined automatically based on the number and the specified grammatical case.

For example, the function selects the appropriate form of the word `"документ"`:

- `1 документ`
- `2 документа`
- `5 документов`

The thousands separator applies to the numeric representation of the number (`i`).

## Examples

### Number in Digits and Words

Suppose the `DocumentCount` field contains:

```text
3
```

The expression:

```text
integerToText_RU(
    DocumentCount,
    "документ",
    "i (ii) W",
    NumeralType_RU.Cardinal,
    GrammaticalCase_RU.Nominative
)
```

Returns:

```text
3 (три) документа
```

### Number Written Out in Words

Suppose the `DocumentCount` field contains:

```text
5
```

The expression:

```text
integerToText_RU(
    DocumentCount,
    "документ",
    "ii W",
    NumeralType_RU.Cardinal,
    GrammaticalCase_RU.Nominative
)
```

Returns:

```text
пять документов
```

### Changing the Grammatical Case

Suppose the `DocumentCount` field contains:

```text
3
```

The expression:

```text
integerToText_RU(
    DocumentCount,
    "документ",
    "i (ii) W",
    NumeralType_RU.Cardinal,
    GrammaticalCase_RU.Genitive
)
```

Returns:

```text
3 (трёх) документов
```

### Using a Thousands Separator

Suppose the `DocumentCount` field contains:

```text
1250
```

The expression:

```text
integerToText_RU(
    DocumentCount,
    "документ",
    "i W",
    NumeralType_RU.Cardinal,
    GrammaticalCase_RU.Nominative,
    " "
)
```

Returns:

```text
1 250 документов
```