# weekday

The `weekday` function determines the day of the week for a specified date and returns its number.

The function is useful when you need to determine the day of the week and use the result in conditions or other expressions.

## Syntax

```text
weekday(date, [returnType])
```

**Parameters:**

- `date` — the date for which the day of the week should be determined. Required;
- `returnType` — defines the first day of the week and the numbering system. Optional.

For the `date` parameter, you can use:

- a Date field value;
- a Date/Time field value;
- a text value containing a valid date;
- the result of another function that returns a date;
- an expression whose result is a date.

The time component does not affect the day-of-week calculation.

## Return value

The function returns the day-of-week number.

If `returnType` is not specified, the following numbering is used:

```text
Monday — 1
Tuesday — 2
Wednesday — 3
Thursday — 4
Friday — 5
Saturday — 6
Sunday — 7
```

For example:

```text
weekday("03/09/2026")
```

Result:

```text
4
```

because September 3, 2026 is a Thursday.

## Return type

The `returnType` parameter allows you to change the first day of the week and the numbering system.

| Return type | First day of the week | Numbering |
| --- | --- | --- |
| `1` | Monday | `0–6` |
| `2` | Tuesday | `0–6` |
| `3` | Wednesday | `0–6` |
| `4` | Thursday | `0–6` |
| `5` | Friday | `0–6` |
| `6` | Saturday | `0–6` |
| `7` | Sunday | `0–6` |
| `11` | Monday | `1–7` |
| `12` | Tuesday | `1–7` |
| `13` | Wednesday | `1–7` |
| `14` | Thursday | `1–7` |
| `15` | Friday | `1–7` |
| `16` | Saturday | `1–7` |
| `17` | Sunday | `1–7` |

Return type `11` corresponds to the default numbering.

For example:

```text
weekday("03/09/2026", 1)
```

Result:

```text
3
```

With return type `1`, Monday is numbered `0`, so Thursday is numbered `3`.

If return type `12` is used:

```text
weekday("03/09/2026", 12)
```

the result is also:

```text
3
```

In this case, Tuesday is the first day of the week and is numbered `1`.

## Examples

**Checking whether a date falls on a weekend**

If the `date` field contains:

```text
05/09/2026
```

the expression:

```text
weekday(date)
```

returns:

```text
6
```

With the default numbering, `6` and `7` correspond to Saturday and Sunday.

For example, you can check whether a date falls on a weekend using:

```text
weekday(date) >= 6
```

## Errors

The function returns an error if:

- the required parameter is empty;
- the supplied value cannot be processed as a valid date;
- `returnType` contains a value other than `1–7` or `11–17`.

For example, return type values `8`, `10`, and `18` return an error.

## Related functions

You can pass a date returned by another function to `weekday`.

For example:

```text
weekday(now())
```

returns the number of the current day of the week.

The function can also be combined with date-shifting functions.

For example:

```text
weekday(dateshift(sourceDate, 1))
```

First, `dateshift` calculates the date of the next day, and then `weekday` returns its day-of-week number.