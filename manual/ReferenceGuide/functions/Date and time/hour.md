# hour

The `hour` function returns the hour from a date and time value or a time value.

The function is useful when you need to extract the hour and use it separately in a document or expression.

## Syntax

```text
hour(value)
```

**Parameters:**

- `value` — the date and time or time value from which the hour should be extracted. Required.

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

The function returns the hour as a number from `0` to `23`.

For example:

```text
hour("03/09/2026 15:53:21")
```

Result:

```text
15
```

## Examples

**Getting the hour from a time value**

```text
hour("15:53:21")
```

Result:

```text
15
```

---

**Getting the hour from a field value**

If the `signingTime` field contains:

```text
15:53:21
```

the expression:

```text
hour(signingTime)
```

returns:

```text
15
```

---

**Getting the current hour**

```text
hour(now())
```

For example, if the current time is `15:53:21`, the function returns:

```text
15
```

## Errors

The function returns an error if the supplied value cannot be processed as a date or time.

An error also occurs if:

- the required parameter is empty;
- a plain numeric value is passed.

## Related functions

The `hour` function can be combined with `minute` and `second` to extract individual parts of a time value.

For example:

```text
time(hour(sourceTime), minute(sourceTime), second(sourceTime))
```

If `sourceTime` contains:

```text
15:53:21
```

the expression creates a time value with the same hours, minutes, and seconds.