# Basic rules

Kombinator uses **expressions** to work with data. Expressions allow you to retrieve field values, perform calculations, compare data, use functions, and define conditions.

The same expression syntax is used wherever expressions are supported. For more information, see [«Where to use»](syntax-usage.md).

## Writing expressions

An expression can consist of a single element:

- a field — `amount`;

- a value — `"Contract"`;

- a function — `length(name)`.

Elements can be combined using operators:

- `quantity * price`;

- `amount > 100000`.

A single expression can combine values, fields, functions, and operators:

```text
if(amount > 100000, "Approval required", "Approval not required")
```

## Values in expressions

**Integers** are written without quotation marks:

- `10`
- `-5`
- `0`

**Decimal numbers** are also written without quotation marks. Use a period as the decimal separator:

- `10.1`
- `3.14`
- `0.01`

**Text** is enclosed in single or double quotation marks:

- `"Contract"`
- `'Contract'`

**Boolean values**:

- `true`
- `false`

Use `null` to represent an empty value.

## Referencing fields

To retrieve a field value in an expression, enter its identifier:

```text
amount
```

To reference a field inside a composite field, specify the path using a period (`.`):

```text
counterparty.taxId
```

Here, `counterparty` is a composite field and `taxId` is a field inside it.

If a field has multiple nesting levels, specify the full path:

```text
deals.counterparty.taxId
```

## Functions

Functions process the data passed to them and return a result.

**Function syntax**

Enter the function name followed by parentheses containing its arguments:

```text
function(argument1, argument2)
```

Arguments are separated by commas. The number and order of arguments depend on the specific function.

An argument can be a value, a field, or another expression.

For example:

```text
length(name)
```

- `length` — the function;

- `name` — the field whose value is passed to the function.

**Nested functions**

The result of one function can be passed to another function:


```text
upper(mid(text, 1, 1))
```

First, `mid` is evaluated. Its result is then passed to `upper`.

## Operators

Operators perform actions on values within an expression.

**Mathematical operators**

- `+` — addition;
- `-` — subtraction;
- `*` — multiplication;
- `/` — division;
- `mod` — remainder after division;
- `^` — exponentiation.

**Comparison operators**

- `<` — less than;
- `<=` — less than or equal to;
- `>` — greater than;
- `>=` — greater than or equal to;
- `=` — equal to;
- `!=` — not equal to.

**Logical operators**

- `and` — returns true when both conditions are true;
- `or` — returns true when at least one condition is true;
- `not` — reverses the Boolean value.

**Combining values**

The `&` operator combines multiple values into a single string:

```text
"Contract № " & contractNumber
```

If the `contractNumber` field contains `125`, the result will be:

```text
Contract № 125
```

You can combine text, field values, and function results:

```text
"Contract № " & contractNumber & " dated " & formatDate(contractDate,"dd.MM.yyyy")
```

