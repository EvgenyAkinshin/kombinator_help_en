# integerToText

The `integerToText` function converts a number to its text representation.

The function supports both cardinal and ordinal numbers.

## Syntax

```text
integerToText(expression, format)
```

**Parameters:**

- `expression` — a numeric value or expression to convert to text;
- `format` — determines whether the number is converted to a cardinal or ordinal form.

The following values are available for `format`:

| Value | Number type | Example |
| --- | --- | --- |
| `NumberType.Cardinal` | Cardinal | `twenty-one` |
| `NumberType.Ordinal` | Ordinal | `twenty-first` |

In the function settings:

- **Expression** — specifies the number, field reference, or expression to convert;
- **Format** — selects `Cardinal` or `Ordinal`.

If a decimal number is passed to the function, only its integer part is used. The fractional part is discarded without rounding.

## Return value

The function returns the text representation of the number.

For example:

```text
integerToText(
    21,
    NumberType.Cardinal
)
```

returns:

```text
twenty-one
```

## Features

The function converts only the numeric value. It does not add units of measurement, currency names, or other text.

If a decimal value needs to be converted in full, its integer and fractional parts should be processed separately.

## Examples

### Cardinal number

Expression:

```text
integerToText(
    1234,
    NumberType.Cardinal
)
```

returns:

```text
one thousand two hundred thirty-four
```

### Ordinal number

Expression:

```text
integerToText(
    21,
    NumberType.Ordinal
)
```

returns:

```text
twenty-first
```

### Decimal number

Suppose the `amount` field contains:

```text
1234.56
```

Expression:

```text
integerToText(
    amount,
    NumberType.Cardinal
)
```

returns:

```text
one thousand two hundred thirty-four
```

The fractional part `.56` is not included in the result.

### Amount in US dollars and cents

Suppose the `amount` field contains:

```text
1234.56
```

To display the integer and fractional parts separately as US dollars and cents, use:

```text
integerToText(
    amount,
    NumberType.Cardinal
) & " " &
if(
    amount - (amount mod 1) = 1,
    "US dollar",
    "US dollars"
) & " " &
integerToText(
    round((amount mod 1) * 100, 0),
    NumberType.Cardinal
) & " " &
if(
    round((amount mod 1) * 100, 0) = 1,
    "cent",
    "cents"
)
```

Result:

```text
one thousand two hundred thirty-four US dollars fifty-six cents
```

Here:

- `amount mod 1` — returns the fractional part of the number;
- `(amount mod 1) * 100` — converts the fractional part to cents;
- `round(..., 0)` — rounds the number of cents to an integer;
- `amount - (amount mod 1)` — returns the integer part used to select `US dollar` or `US dollars`;
- `if(...)` — selects the singular or plural currency name.