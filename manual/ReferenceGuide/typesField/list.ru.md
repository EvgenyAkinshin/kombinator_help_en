# «List» field

The **«List»** field is used to store multiple items with the same structure.

Each list item can contain a single value or several related fields. For example, a list can be used to store products, employees, services, or other repeating data.

## Creating and adding a field

For instructions on creating and adding fields, see [Creating a template](../Bitrix/creat.md).

## List structure

The structure of a single item determines which data is stored in each list item.

For example, the **«Products»** field in a deal may have the following structure:

```text
deals

└── products

    └── product

        ├── name

        ├── quantity

        └── price
```

Where:

- `deals` — a **Struct** field representing the deal entity;
- `products` — a **List** field;
- `product` — a **Struct** field representing one list item;
- `name`, `quantity`, and `price` — fields of a single product.

The list can contain multiple products with the same structure but different values.

## Using the field through the «Directives» tab

The [«For»](../directives/for.md) and [«Table»](../directives/table.md) directives are used to work with list items.

### Using the «For» directive

The **«For»** directive processes each item in the list and repeats the specified document content for every item.

The current list item is assigned a variable name that can be used to reference its value or nested fields.

For example, for a deal product list:

```text
{t_for(product из deals.products)}

{product.name} — {product.quantity} — {product.price}

{/t_for}
```

Where:

- `deals.products` — the **List** field;
- `product` — the current item variable;
- `product.name`, `product.quantity`, and `product.price` — fields of the current product.

For more information, see [«For»](../directives/for.md).

### Using the «Table» directive

The **«Table»** directive is used when list items need to be displayed as a dynamic table.

For each item in the list, Kombinator repeats the table rows placed between the `t_for` and `/t_for` directives. The repeated block can contain one or multiple rows.

For example, if the template contains two rows for each product:

```text
Name: {product.name}

Quantity: {product.quantity}    Price: {product.price}
```

and the list contains two products, the generated document may contain:

```text
Name: Monitor

Quantity: 2    Price: 15000

Name: Keyboard

Quantity: 5    Price: 3000
```

For more information, see [«Table»](../directives/table.md).

## Functions for working with the field

The **«List»** field supports functions for searching, filtering, sorting, grouping, and processing list items.

### Searching and processing a list

- [index](../functions/Lists/index.md) — returns a list item at the specified position;
- [match](../functions/Lists/match.md) — finds the position of an item in a list;
- [filter](../functions/Lists/filter.md) — selects list items that match a specified condition;
- [sort](../functions/Lists/sort.md) — sorts items in ascending order;
- [sortDescending](../functions/Lists/sortDescending.md) — sorts items in descending order;
- [group](../functions/Lists/group.md) — groups items by a specified value.

The results of `filter`, `sort`, `sortDescending`, and `group` can be used instead of the original list in a **For** or **Table** directive.

`filter` returns a new list containing only the selected items, sorting functions return a new list with a different item order, and `group` returns a list of generated groups.

### Calculations with list items

The following functions can be used with a list and values of its items:

- [count](../functions/Lists/count.md) — returns the number of items;
- [sum](../functions/Lists/sum.md) — calculates the sum of numeric values;
- [avg](../functions/Lists/avg.md) — calculates the arithmetic mean;
- [min](../functions/Lists/min.md) — returns the minimum value;
- [max](../functions/Lists/max.md) — returns the maximum value.