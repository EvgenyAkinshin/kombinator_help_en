# numberToText_RU

The **`numberToText_RU`** function displays a number together with a word in the appropriate grammatical form.

## Syntax

```text
numberToText_RU(Number expression, Expression of the word, Format, Numeral type, Grammatical case)
```

**Parameters:**

- **`Number expression`** — an integer or decimal numeric value.
- **`Expression of the word`** — the word that must agree with the number.
- **`Format`** — specifies how the number is displayed.
- **`Numeral type`** — specifies the type of numeral.
- **`Grammatical case`** — specifies the grammatical case in which the numeral and word are returned.

The following options are available for the **`Format`** parameter:

| Value | Result |
|---|---|
| `Long` | `5 (пять) комнат` |
| `Short` | `5 комнат` |
| `InWords` | `пять комнат` |

The following options are available for the **`Numeral type`** parameter:

- **`Cardinal`** — a cardinal numeral indicating quantity.
- **`Ordinal`** — an ordinal numeral indicating position or order.

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

The function returns a text value in which the number and the specified word agree according to the selected parameters.

## Notes

The function supports both integer and decimal values.

The grammatical form of the word is determined automatically based on the numeric value and the specified grammatical case.

Unlike the **`integerToText_RU`** function, **`numberToText_RU`** allows you to select the output format from predefined options.

## Examples

### Number in Digits and Words

Suppose the `Quantity` field contains:

```text
5
```

The expression:

```text
numberToText_RU(
    Quantity,
    "комната",
    Long,
    Cardinal,
    GrammaticalCase_RU.Nominative
)
```

Returns:

```text
5 (пять) комнат
```

### Short Format

Suppose the `Quantity` field contains:

```text
2
```

The expression:

```text
numberToText_RU(
    Quantity,
    "документ",
    Short,
    Cardinal,
    GrammaticalCase_RU.Nominative
)
```

Returns:

```text
2 документа
```

### Number Written Out in Words

Suppose the `Quantity` field contains:

```text
3
```

The expression:

```text
numberToText_RU(
    Quantity,
    "этаж",
    InWords,
    Cardinal,
    GrammaticalCase_RU.Nominative
)
```

Returns:

```text
три этажа
```