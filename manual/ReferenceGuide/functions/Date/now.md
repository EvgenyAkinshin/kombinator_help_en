# now

The `now` function returns the current date and time at the moment the document is generated.

The function is useful when you need to automatically insert the exact generation date and time or use them in calculations.

## Syntax

```text
now()
```

**Parameters:**

The function does not accept any parameters.

## Return value

The function returns the current date and time.

For example:

```text
now()
```

Result:

```text
02.09.2026 13:45:30
```

## Features

The function value is determined at the time the document is generated.

Unlike `Today()`, which returns the current date with the time set to `00:00:00`, `now()` returns the current date and time.

For example:

```text
Today()
```

Result:

```text
02.09.2026 00:00:00
```

```text
now()
```

Result:

```text
02.09.2026 13:45:30
```

## Examples

**Shifting the date and time**

```text
dateshift(now(), 1)
```

If `now()` returns:

```text
02.09.2026 13:45:30
```

the result is:

```text
03.09.2026 13:45:30
```

---

**Shifting by one month**

```text
edate(now(), 1)
```

If `now()` returns:

```text
02.09.2026 13:45:30
```

the result is:

```text
02.10.2026 13:45:30
```

## Related functions

The result of `now()` can be used with other date and time functions.

For example:

```text
formatDate(now(),"'Generated' dd.MM.yyyy 'at' HH:mm","en")
```

Result:

```text
Generated 02.09.2026 at 13:45
```