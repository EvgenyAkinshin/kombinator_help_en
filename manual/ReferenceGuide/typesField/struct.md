# «Struct» field

The **«Struct»** field contains other fields and is used to store a set of related data about a single object.

For example, a **«Counterparty»** Struct field may contain the **name**, **tax ID**, **registration code**, and **address**.

## Creating and adding a field

For instructions on creating and adding fields, see [Creating a template](../Bitrix/creat.md).

## Field value

When working with a Struct field, you use the values of its nested fields.

In Bitrix24, a Struct field can contain fields of the entity from which the document is generated.

For example, when working with a deal, the structure may look like this:

```text
deals

├── name

└── id
```

Here, `deals` is a Struct field containing the deal fields.

Struct fields can also be nested inside other field types. For example, a **List** field may contain a Struct field that represents each item in the list:

```text
deals

└── products

    └── product

        ├── name

        ├── quantity

        └── price
```

Where:

- `deals` — the Struct field representing the deal entity;
- `products` — a **List** field containing multiple products;
- `product` — a Struct field representing one item in the list;
- `name`, `quantity`, and `price` — the fields that make up each product.

## Working with nested fields

To reference a nested field, specify its full path using a period (`.`).

For example:

```text
deals.name
```

Where:

- `deals` — the Struct field containing the deal fields;
- `name` — the nested field.

If a field is located deeper in the structure, specify the full path to it in the expression.

Nested fields can be used in the same way as regular fields of the corresponding type:

- insert their values into the document;
- use them in conditions;
- pass them to functions;
- use them in expressions.

## Inserting fields through the «Directives» tab

A Struct field itself is not inserted into the document as a separate value. Instead, you use the fields nested inside it.

The directive you use depends on the nested field type and how the field should be used in the template.

For example:

- a **Text**, **Integer**, **Decimal Number**, or **Date** field can be inserted using the [«Expression»](../directives/expression.md) directive;
- a **Boolean** field can be used with the [«Condition expression»](../directives/if.md) directive;
- a **List** field can be used with the [«For»](../directives/for.md) or [«Table»](../directives/table.md) directive.

## Functions for working with the field

The **«Struct»** field itself does not have dedicated functions.

Functions are applied to its nested fields depending on their type.

For example:

- **Text** fields support text functions;
- **Integer** and **Decimal Number** fields support mathematical functions;
- **Date** fields support date functions.

## Features

A Struct field can contain multiple levels of nesting. To reference a specific value, specify the full path to the corresponding field.