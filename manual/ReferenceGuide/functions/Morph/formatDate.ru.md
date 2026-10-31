# formatDate

The `formatDate` function formats a date, time, or date and time value.

The output format can be selected from the predefined formats or configured manually using **Custom format**.

## Syntax

```text
formatDate(date, format, [locale])
```

**Parameters:**

- `date` — the date, time, or date and time value to format;
- `format` — defines how the resulting value is displayed;
- `locale` — defines the language used for month and day names. This parameter is optional. If no locale is specified, **Template default locale** is used.

In the function settings, the output format can be configured in two ways:

- if **Custom format** is disabled — select one of the predefined values from **Format**;
- if **Custom format** is enabled — specify the format string manually.

### Custom format

When **Custom format** is enabled, the format string can be created using the following symbols:

| Symbol | Description | Example |
| --- | --- | --- |
| `dd` | day of the month | `05` |
| `ddd` | abbreviated day of the week | `Sat` |
| `dddd` | full day of the week | `Saturday` |
| `MM` | month as a number | `09` |
| `MMM` | abbreviated month name | `Sep` |
| `MMMM` | full month name | `September` |
| `yy` | two-digit year | `26` |
| `yyyy` | four-digit year | `2026` |
| `HH` | hours | `14` |
| `mm` | minutes | `30` |
| `ss` | seconds | `25` |

The symbols can be combined and separated with the required characters.

For example:

```text
"MM/dd/yyyy"
```

```text
"yyyy-MM-dd"
```

```text
"MMMM dd, yyyy HH:mm"
```

Symbol case is significant:

- `MM` — month;
- `mm` — minutes.

Text that should be displayed without changes is enclosed in single quotation marks:

```text
"'Generated on' MMMM dd, yyyy 'at' HH:mm"
```

## Return value

The function returns the formatted value as text.

## Locale

The **Locale** setting affects month and day names.

For example, with an English locale:

```text
formatDate(
    contractDate,
    "MMMM dd, yyyy"
)
```

can return:

```text
September 05, 2026
```

The expression:

```text
formatDate(
    contractDate,
    "dddd, MMMM dd, yyyy"
)
```

can return:

```text
Saturday, September 05, 2026
```

If a locale is not selected, **Template default locale** is used.

## Examples

### Formatting date and time

Suppose the `generatedAt` field contains a date and time value corresponding to September 5, 2026 at 14:30:25.

Expression:

```text
formatDate(
    generatedAt,
    "MMMM dd, yyyy HH:mm:ss"
)
```

Result:

```text
September 05, 2026 14:30:25
```

### Adding text to the formatted value

Suppose the `generatedAt` field contains a date and time value corresponding to September 5, 2026 at 14:30.

Expression:

```text
formatDate(
    generatedAt,
    "'Generated on' MMMM dd, yyyy 'at' HH:mm"
)
```

Result:

```text
Generated on September 05, 2026 at 14:30
```

### Displaying the day of the week

Expression:

```text
formatDate(
    contractDate,
    "dddd, MMMM dd, yyyy"
)
```

Result:

```text
Saturday, September 05, 2026
```

### Formatting the result of the `date` function

A value returned by the `date` function can be passed directly to `formatDate`.

For example:

```text
formatDate(
    date(5, 9, 2026),
    "MMMM dd, yyyy"
)
```

Result:

```text
September 05, 2026
```