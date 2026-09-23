# «Boolean» field

The **«Boolean»** field is used to store a logical value: `true` or `false`.

This field is useful for controlling document content depending on whether a condition is true or false.

## Creating and adding a field

For instructions on creating and adding fields, see [Creating a template](../Bitrix/creat.md).

## Field value

The field can contain one of two values:

- `true`;
- `false`.

The field value can be used in logical expressions, for example to show or hide specific parts of a document.

## Inserting a field through the «Directives» tab

The **«Boolean»** field is most commonly used with the [«Condition expression»](../directives/if.md) directive. It allows you to include or exclude part of the document depending on the field value.

Specify the **Boolean** field whose value should be checked as the condition.

The field can also be used with the [«Expression»](../directives/expression.md) directive. In this case, inserting only the field itself is not correct — use the `if(...)` function:

```text
if(fieldValue, expression_if_true, expression_if_false)
```

All three arguments are required:

- `fieldValue` — the **Boolean** field whose value is checked;
- `expression_if_true` — the value returned if the field contains `true`;
- `expression_if_false` — the value returned if the field contains `false`.

The returned expressions can contain text, field values, or nested functions.

For example:

```text
if(delivery, "Delivery required", "Delivery not required")
```

If the field contains `true`, the result will be:

```text
Delivery required
```

If the field contains `false`, the result will be:

```text
Delivery not required
```

This method is used less often than the **«Condition expression»** directive.

## Functions and logical operations

The **«Boolean»** field does not have dedicated functions. Its value can be used directly in logical expressions.