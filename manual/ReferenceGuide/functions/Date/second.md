# second

The `second` function returns the seconds from a date and time value or a time value.

The function is useful when you need to extract the seconds and use them separately in a document or expression.

## Syntax

```text
second(value)
```

**Parameters:**

- `value` — the date and time or time value from which the seconds should be extracted. Required.

You can use:

- a Date/Time or Time field value;
- a text value containing a valid date and time or time;
- the result of another function;
- an expression whose result can be processed as a date or time.

For example, the function can process:

```text
03/09/2026 15:53:21
```

or:

```text
15:53:21
```

## Return value

The function returns the seconds as a number from `0` to `59`.

For example:

```text
second("03/09/2026 15:53:21")
```

Result:

```text
21
```

## Examples

**Getting the seconds from a time value**

```text
second("15:53:21")
```

Result:

```text
21
```

---

**Getting the seconds from a field value**

If the `signingTime` field contains:

```text
15:53:21
```

the expression:

```text
second(signingTime)
```

returns:

```text
21
```

---

**Getting the current second**

```text
second(now())
```

For example, if the current time is `15:53:21`, the function returns:

```text
21
```

## Errors

The function returns an error if the supplied value cannot be processed as a date or time.

An error also occurs if:

- the required parameter is empty;
- a plain numeric value is passed.

## Related functions

The `second` function can be combined with `hour` and `minute` to extract individual parts of a time value.

For example:

```text
time(hour(sourceTime), minute(sourceTime), second(sourceTime))
```

If `sourceTime` contains:

```text
15:53:21
```

the expression creates a time value with the same hours, minutes, and seconds.