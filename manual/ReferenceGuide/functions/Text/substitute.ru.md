# substitute

The `substitute` function finds a specified text fragment and replaces all of its occurrences with another value.

## Syntax

```text
substitute(sourceString, searchString, replacementString)
```

**Parameters:**

- `sourceString` — the source text in which the replacement should be performed. Required;
- `searchString` — the text or character to find. Required;
- `replacementString` — the text that replaces each occurrence of the specified fragment. Required.

You can use text, field values, results of other functions, and expressions as parameters.

## Return value

The function returns the modified text with all occurrences of `searchString` replaced by `replacementString`.

For example:

```text
substitute("Contract-125-2026", "-", "/")
```

Result:

```text
Contract/125/2026
```

## Examples

**Preparing a value for a path mask**

In a path mask, the `/` character is used to create nested folders. If `/` is part of a field value and should remain within a single folder name, you can replace it with another character.

For example:

```text
substitute(name, "/", ". ")
```

If the `name` field contains:

```text
Sales Department/Amsterdam
```

the result is:

```text
Sales Department. Amsterdam
```