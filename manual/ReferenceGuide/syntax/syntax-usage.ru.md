# Where to use

Expressions are used in different parts of Kombinator, but the syntax is the same everywhere.

Whether an expression is used in field properties, a directive, a file name mask, or another part of the application, you can use the same fields, functions, operators, and values.

Expression syntax is described in [«Basic rules»](syntax.md).

## Directives

Expressions are used in directive properties to retrieve data and control template content.

For example:

- in the [«Expression»](../directives/expression.md) directive — to specify which value or expression result should be inserted into the document;

- in the [«Condition expression»](../directives/if.md) directive — to define a condition;

- in the [«For»](../directives/for.md) and [«Table»](../directives/table.md) directives — to work with lists.

Other directives can also use expressions depending on their purpose.

## File name mask

Expressions are used in the [file name mask](../../UserInterface/Templates/file-name-mask.md) to generate the name of the final document from text, field values, and function results.

For example:

```text
"Contract № " & contractNumber
```