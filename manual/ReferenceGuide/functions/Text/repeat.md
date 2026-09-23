# repeat

The `repeat` function repeats a specified value a given number of times.

## Syntax

```text
repeat(value, count)
```

**Parameters:**

- `value` — the value to repeat. Required;
- `count` — the number of repetitions. Required.

The number of repetitions must be a non-negative integer.

You can use field values, results of other functions, and expressions as parameters.

## Return value

The function returns a string containing the specified number of repetitions of the source value.

For example:

```text
repeat("A", 4)
```

Result:

```text
AAAA
```

The function does not add spaces or other separators between repetitions. If you need a separator, include it in the value itself:

```text
repeat("A ", 4)
```

Result:

```text
A A A A 
```

If `count` is `0`, the function returns an empty value.

## Examples

**Using a field value**

If the `name` field contains:

```text
Kombinator
```

the expression:

```text
repeat(name, 2)
```

returns:

```text
KombinatorKombinator
```

---

**Getting the number of repetitions from a field**

The number of repetitions can come from another field or expression:

```text
repeat("-", count)
```

If `count` = `5`, the result is:

```text
-----
```