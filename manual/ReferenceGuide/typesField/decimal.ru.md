# «Decimal» field

The **«Decimal Number»** field is used to store numeric values with a fractional part and perform calculations with them.

It is suitable for prices, weight, area, percentages, coefficients, and other numeric values that may contain a fractional part.

## Creating and adding a field

For instructions on creating and adding fields, see [Creating a template](../Bitrix/creat.md).

## Field value

The field contains a numeric value that may include a fractional part.

For example:

- `12.5`;
- `1500.75`;
- `0.25`.

The field can be used not only to insert a value into a document but also in mathematical expressions and functions.

## Inserting a field through the «Directives» tab

The field value can be inserted into the template using the [«Expression»](../directives/expression.md) directive.

1. Place the cursor at the required position in the template.

2. Open the **«Directives»** tab and select **«Expression»**.

3. In the **«Expression»** field, specify the field whose value should be inserted.

4. Click **«OK»**.

For example, if the field identifier is:

```text
deals.price
```

where:

- `deals` — the Bitrix24 entity from which the data is retrieved;
- `price` — the field within that entity.

If the field contains `1250.50`, this value will be inserted into the generated document.

The **«Expression»** field can contain not only a field identifier but also a mathematical expression using its value.

For example, the total price can be calculated directly in the expression:

```text
deals.price * deals.quantity
```

When the document is generated, Kombinator calculates the expression and inserts the result.

## Functions and operations for working with the field

### Mathematical operations

You can perform arithmetic operations with decimal numbers:

- `+` — addition;
- `-` — subtraction;
- `*` — multiplication;
- `/` — division;
- `^` — exponentiation.

### Mathematical functions

The following functions can be used with decimal values:

- [round](../functions/Math/round.md) — rounds a number to the specified number of digits;
- [roundup](../functions/Math/roundup.md) — rounds a number away from zero;
- [rounddown](../functions/Math/rounddown.md) — rounds a number toward zero;
- [exp](../functions/Math/exp.md) — calculates the exponential function;
- [ln](../functions/Math/ln.md) — calculates the natural logarithm;
- [log10](../functions/Math/log10.md) — calculates the base-10 logarithm.

### Formatting functions

- [formatNumber](../functions/Morph/formatNumber.md) — changes how a numeric value is displayed;
- [форматВалюты](../functions/Morph/форматВалюты.md) — formats a numeric value as a monetary amount;
- [числоСТекстом](../functions/Morph/числоСТекстом.md) — displays a numeric value together with a matching word form in the specified format.