# formatDate_RU

The **`formatDate_RU`** function converts a date or time value into the specified text format.

The function allows you to display a complete date or time, extract individual components, or represent a date in words.

## Syntax

```text
formatDate_RU(Expression, Date format)
```

**Parameters:**

- **`Expression`** — required. The date, time, or date and time value to be formatted.
- **`Date format`** — required. Specifies how the result is displayed.

The following values are available for the **`Date format`** parameter:

| Value | Example Result |
|---|---|
| `DateFormat_RU.Time` | `13:22` |
| `DateFormat_RU.TimeInWords` | `13 часов 22 минуты` |
| `DateFormat_RU.TimeWithSeconds` | `13:22:32` |
| `DateFormat_RU.TimeWithSecondsInWords` | `13 часов 22 минуты 32 секунды` |
| `DateFormat_RU.Year` | `2023` |
| `DateFormat_RU.YearShort` | `23` |
| `DateFormat_RU.YearWord` | `2023 год` |
| `DateFormat_RU.DateAndTime` | `4 декабря 2023 13:22` |
| `DateFormat_RU.DateAndTimeShort` | `04.12.2023 13:25` |
| `DateFormat_RU.DateAndTimeShortWithSeconds` | `04.12.2023 13:25:32` |
| `DateFormat_RU.DateAndTimeWithSeconds` | `4 декабря 2023 13:22:32` |
| `DateFormat_RU.DateShort` | `04.12.2023` |
| `DateFormat_RU.FullDateYearAbbr` | `1 декабря 2023 г.` |
| `DateFormat_RU.FullDateYearWord` | `1 декабря 2023 года` |
| `DateFormat_RU.DateInWords` | `первое декабря две тысячи двадцать третий год` |
| `DateFormat_RU.DateInWordsYearGenitive` | `первое декабря две тысячи двадцать третьего года` |
| `DateFormat_RU.DateInWordsShort` | `1 декабря 2023 (первое декабря две тысячи двадцать третий) год` |
| `DateFormat_RU.DateInWordsShortGenitive` | `1 декабря 2023 (первое декабря две тысячи двадцать третьего) год` |
| `DateFormat_RU.DateInWordsFull` | `01.12.2023 (первое декабря две тысячи двадцать третий) год` |
| `DateFormat_RU.DateInWordsFullGenitive` | `01.12.2023 (первое декабря две тысячи двадцать третьего) год` |
| `DateFormat_RU.DateInWordsGenitive` | `первого декабря две тысячи двадцать третьего года` |
| `DateFormat_RU.DateQuoted` | `"01" декабря 2023 г.` |
| `DateFormat_RU.DateGuillemets` | `«01» декабря 2023 г.` |
| `DateFormat_RU.Day` | `01` |
| `DateFormat_RU.FullDateYearAbbrDay2` | `01 декабря 2023 г.` |
| `DateFormat_RU.FullDateYearWordDay2` | `01 декабря 2023 года` |
| `DateFormat_RU.DayMonth` | `01 декабря` |
| `DateFormat_RU.Weekday` | `Пятница` |
| `DateFormat_RU.WeekdayShort` | `Пт` |
| `DateFormat_RU.Month` | `декабрь` |
| `DateFormat_RU.MonthYear` | `декабрь 2023` |
| `DateFormat_RU.MonthShort` | `дек` |
| `DateFormat_RU.MonthNumber` | `12` |
| `DateFormat_RU.Minutes` | `22` |
| `DateFormat_RU.Seconds` | `32` |
| `DateFormat_RU.Hours` | `13` |

## Return Value

The function returns a text value in the selected format.

For example, suppose the `ContractDate` field contains:

```text
01.12.2023
```

The expression:

```text
formatDate_RU(
    ContractDate,
    DateFormat_RU.DateShort
)
```

Returns:

```text
01.12.2023
```

## Notes

The selected format determines which part of the source value is included in the result.

For example, a field containing a date and time value can be used to extract only the date:

```text
formatDate_RU(
    DateTime,
    DateFormat_RU.DateShort
)
```

Only the time:

```text
formatDate_RU(
    DateTime,
    DateFormat_RU.Time
)
```

Or an individual date component, such as the year:

```text
formatDate_RU(
    DateTime,
    DateFormat_RU.Year
)
```

The function does not change the original date or time value. It only controls how the value is displayed in the document.

Since **`formatDate_RU`** uses Russian date formatting, month names, weekday names, and dates written out in words are returned in Russian.

If the available formats do not meet your requirements, use a custom date-formatting function to define the desired date and time representation using a format mask.

## Examples

### Date with Quotation Marks

Suppose the `ContractDate` field contains:

```text
01.12.2023
```

The expression:

```text
formatDate_RU(
    ContractDate,
    DateFormat_RU.DateGuillemets
)
```

Returns:

```text
«01» декабря 2023 г.
```

### Date Written Out in Words

Suppose the `ContractDate` field contains:

```text
01.12.2023
```

The expression:

```text
formatDate_RU(
    ContractDate,
    DateFormat_RU.DateInWords
)
```

Returns:

```text
первое декабря две тысячи двадцать третий год
```

### Extracting the Day of the Week

Suppose the `ContractDate` field contains:

```text
01.12.2023
```

The expression:

```text
formatDate_RU(
    ContractDate,
    DateFormat_RU.Weekday
)
```

Returns:

```text
Пятница
```

### Extracting the Month

Suppose the `ContractDate` field contains:

```text
01.12.2023
```

The expression:

```text
formatDate_RU(
    ContractDate,
    DateFormat_RU.Month
)
```

Returns:

```text
декабрь
```

### Extracting the Year

Suppose the `ContractDate` field contains:

```text
01.12.2023
```

The expression:

```text
formatDate_RU(
    ContractDate,
    DateFormat_RU.Year
)
```

Returns:

```text
2023
```

### Formatting Date and Time

Suppose the `DateTime` field contains:

```text
04.12.2023 13:22:32
```

The expression:

```text
formatDate_RU(
    DateTime,
    DateFormat_RU.DateAndTimeWithSeconds
)
```

Returns:

```text
4 декабря 2023 13:22:32
```

### Extracting Time Without Seconds

Suppose the `DateTime` field contains:

```text
04.12.2023 13:22:32
```

The expression:

```text
formatDate_RU(
    DateTime,
    DateFormat_RU.Time
)
```

Returns:

```text
13:22
```

## Using with Other Functions

The **`Expression`** parameter can accept the result of another function, provided that it returns a date or time value.

For example, **`formatDate_RU`** can be used together with the **`date`** function:

```text
formatDate_RU(
    date(1, 12, 2023),
    DateFormat_RU.FullDateYearWord
)
```

Returns:

```text
1 декабря 2023 года
```

First, the **`date`** function creates a date value. The **`formatDate_RU`** function then converts it into the selected text format.