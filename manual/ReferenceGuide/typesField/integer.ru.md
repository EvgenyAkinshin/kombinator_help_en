# «Integer» field

The **«Integer»** field is used to store numeric values without a fractional part and perform calculations with them.

It is suitable for quantities, numbers of days, numbers of employees, and other whole-number values.

## Creating and adding a field

For instructions on creating and adding fields, see [Creating a template](../Bitrix/creat.md).

## Field value

The field contains an integer without a fractional part.

For example:

- `5`
- `120`
- `15000`

## Inserting a field through the «Directives» tab

The field value can be inserted into the template using the [«Expression»](../directives/expression.md) directive.

1. Place the cursor at the required position in the template.

2. Open the **«Directives»** tab and select **«Expression»**.

3. In the **«Expression»** field, specify the field whose value should be inserted.

4. Click **«OK»**.

For example, if the field identifier is:

```text
deals.numberOfStudents
```

where:

- `deals` — the Bitrix24 entity from which the data is retrieved;
- `numberOfStudents` — the field within that entity.

If the **«Number of students»** field contains `25`, the generated document will display:

```text
25
```

## Functions and operations for working with the field

### Mathematical operations

You can perform arithmetic operations with integer values:

- `+` — addition: `10 + 5` → `15`;
- `-` — subtraction: `10 - 5` → `5`;
- `*` — multiplication: `10 * 5` → `50`;
- `/` — division: `10 / 5` → `2`;
- `^` — exponentiation: `2 ^ 3` → `8`.

### Mathematical functions

The following functions can be used with numeric values:

- [round](../functions/Math/round.md) — rounds a number to the specified number of digits;
- [roundup](../functions/Math/roundup.md) — rounds a number away from zero;
- [rounddown](../functions/Math/rounddown.md) — rounds a number toward zero;
- [exp](../functions/Math/exp.md) — calculates the exponential function;
- [ln](../functions/Math/ln.md) — calculates the natural logarithm;
- [log10](../functions/Math/log10.md) — calculates the base-10 logarithm.

### Formatting functions

- [formatNumber](../functions/Morph/formatNumber.md) — formats a number, for example by adding thousands separators;
- [форматВалюты](../functions/Morph/форматВалюты.md) — formats a numeric value as a monetary amount.

### Number-to-text functions

- [целоеСТекстом](../functions/Morph/целоеСТекстом.md) — displays an integer as digits or words and can use the appropriate word form;
- [числоСТекстом](../functions/Morph/числоСТекстом.md) — displays a number together with a matching word form in the specified format.

