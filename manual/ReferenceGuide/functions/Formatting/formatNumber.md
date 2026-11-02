# formatNumber

The `formatNumber` function changes how a numeric value is displayed.

It allows you to specify the number of decimal places, the decimal separator, and, if necessary, the thousands separator.

## Syntax

```text
formatNumber(number, "format", "decimalSeparator")
```

**Parameters:**

- `number` — the numeric value to format;
- `format` — defines how the number is displayed;
- `decimalSeparator` — the character used to separate the fractional part from the integer part.

If necessary, you can also specify a thousands separator:

```text
formatNumber(number, "format", "decimalSeparator", "thousandsSeparator")
```

- `thousandsSeparator` — an optional parameter that defines the character used to separate groups of digits in the integer part.

In the function settings, the number format can be configured in two ways:

- if **Custom format** is disabled — specify the number of **Decimal places**;
- if **Custom format** is enabled — define the format string manually.

You can also specify:

- **Decimal separator** — the character used to separate the fractional part from the integer part;
- **Thousands separator** — the character used to separate groups of digits in the integer part. If no separator is required, select `Empty`.

### Custom format

When **Custom format** is enabled, the format string is created using special characters:

| Symbol | Description |
| :--- | :--- |
| `#` | Digit placeholder. Displays only significant digits. |
| `0` | Digit placeholder with zero padding. If there is no digit in this position, `0` is displayed. |
| `.` | Position of the decimal separator. Can appear only once in the format string. |
| `,` | Position of the thousands separator. |

## Return value

The function returns the formatted numeric value as text.

## Features

The `.` and `,` characters in the format string define the positions of the separators. The actual characters displayed in the result are specified by **Decimal separator** and **Thousands separator**.

If the format contains fewer decimal places than the source value, the displayed value is rounded.

Because the function returns text, calculations with the number should be performed before applying `formatNumber`.

## Examples

### Displaying two decimal places

Suppose the `amount` field contains:

```text
125.6
```

Expression:

```text
formatNumber(
    amount,
    "0.00",
    "."
)
```

returns:

```text
125.60
```

### Adding a thousands separator

Suppose the `amount` field contains:

```text
1234567.865464
```

Expression:

```text
formatNumber(
    amount,
    "#,##0.00",
    ".",
    ","
)
```

returns:

```text
1,234,567.87
```

### Displaying only significant decimal digits

Suppose the `amount` field contains:

```text
125.5
```

Expression:

```text
formatNumber(
    amount,
    "0.##",
    "."
)
```

returns:

```text
125.5
```

If the `amount` field contains:

```text
125
```

the same expression returns:

```text
125
```