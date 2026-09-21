# Condition expression

The **«Condition expression»** directive controls which content is included in the generated document depending on a specified condition.

![28](../img/directives/28.png)

Kombinator evaluates the condition and either includes or excludes the content inside the directive.

For example, you can:

- include a contract clause only when a field has a specific value;
- display additional text when an amount exceeds a specified value;
- display one version of the content when the condition is met and another when it is not.

## Directive structure

The directive consists of an opening and a closing part.

The condition is specified in the opening part:

```text
{if (condition)}

Content to be included.

{/if}
```

Kombinator evaluates the expression specified in the opening part.

If the result is `true`, the content between `If` and `/Endif` is included in the document.

If the result is `false`, the content is not included.

## Condition

The condition must be an expression that returns the Boolean value `true` or `false`.

For example, you can check a numeric field:

```text
amount > 100000
```

If the `amount` field contains a value greater than `100000`, the condition is met.

You can compare field values:

```text
quantity > limit
```

check text values:

```text
status = "Approved"
```

or check whether a value is present:

```text
contractNumber != null
```

Logical operators and functions can also be used according to the general expression syntax.

For more information, see [«Basic rules»](../syntax/syntax.md).

## Boolean field

A **Boolean** field can be used directly as a condition.

For example:

```text
delivery
```

If the `delivery` field contains `true`, the condition is met and the content inside the directive is included in the document.

If the field contains `false`, the content is excluded.

To check the opposite value, use the `not` operator:

```text
not delivery
```

In this case, the content will be included when the `delivery` field contains `false`.

## Multiple conditions

A single expression can contain multiple conditions.

Use the `and` operator when both conditions must be true:

```text
amount > 100000 and approval
```

The content will be included only if the amount is greater than `100000` and the `approval` field returns `true`.

Use the `or` operator when at least one condition must be true:

```text
urgentOrder or importantClient
```

The content will be included if at least one of these conditions is met.

## Else block

Use the **Else** block when you need two content options: one for a true condition and another for a false condition.

The structure is:

```text
{if (condition)}

Content displayed when the condition is true.

{else}

Content displayed when the condition is false.

{/if}
```

For example:

```text
{if (amount > 100000)}

Additional approval is required.

{else}

Additional approval is not required.

{/if}
```

If `amount > 100000`, the first content block is included in the document.

If the condition is not met, the content after `Else` is included.

The **Else** block is optional. If no alternative content is required, use only `If` and `/Endif`.

## Nested conditions

One **«Condition expression»** directive can be placed inside another. This allows you to check several dependent conditions step by step.

For example:

```text
{if (delivery)}

Delivery terms.

    {if (urgentDelivery)}

    Delivery within one business day.

    {/if}

{/if}
```

Kombinator first checks the `delivery` field.

Only if this condition is met does it evaluate the nested `urgentDelivery` condition.