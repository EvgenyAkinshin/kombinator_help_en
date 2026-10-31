# group

The `group` function combines list items into groups based on the same value of a specified property or expression.

## Syntax

```text
group(item in list, expression)
```

**Parameters:**

- `item` — the name of the current list item. In the function settings, this parameter is **Item list name**;
- `list` — the identifier of the list field. In the function settings, this parameter is **List**;
- `expression` — the property or expression used to group the items. In the function settings, this parameter is **Grouping property**.

The item name can be chosen freely and is used only inside the function.

For example:

```text
group(product in products, product.category)
```

Here:

- `product` — the current item name specified in **Item list name**;
- `products` — the list field identifier specified in **List**;
- `category` — the nested field identifier;
- `product.category` — the value specified in **Grouping property**.

Items with the same `category` value are placed in the same group.

## Return value

The function returns a list of groups.

Each group automatically provides two properties:

- `.Key` — the value used to create the group;
- `.List` — the list of source items included in the group.

For example, if the current group is named `groupItem`:

```text
groupItem.Key
groupItem.List
```

You can choose the name `groupItem` yourself.

The `.Key` and `.List` properties are created by the `group` function and must be specified exactly as shown. They are not field identifiers from the form.

The resulting `groupItem.List` can be used like any other list. For example, you can iterate through it in a `for` block or pass it to `sum`, `count`, `avg`, `min`, or `max`.

## Example

### Grouping products and calculating a subtotal for each group

Suppose the template contains a list field with the following identifier:

```text
products
```

Each list item contains:

- `name` — product name;
- `category` — product category;
- `price` — unit price;
- `quantity` — product quantity.

Source list:

| `name` | `category` | `price` | `quantity` |
| --- | --- | ---: | ---: |
| Monitor | Electronics | 15000 | 2 |
| Printer | Electronics | 12000 | 1 |
| Desk | Furniture | 20000 | 1 |
| Chair | Furniture | 5000 | 4 |

The products need to be grouped by category. For each category, the products should be displayed and their total cost calculated.

Use an outer `for` block to iterate through the result of `group` and an inner `for` block to iterate through the items in each group:

```text
{for(groupItem in group(product in products, product.category))}
{groupItem.Key}

{for(item in groupItem.List)}
{item.name} — {item.quantity} × {item.price}
{/for}

Total: {sum(totalItem in groupItem.List, totalItem.price * totalItem.quantity)}

{/for}
```

Here:

- `products` — the identifier of the source list field;
- `product` — the current item name specified in **Item list name**;
- `product.category` — the value specified in **Grouping property**;
- `groupItem` — the name of the current group in the outer `for` block;
- `groupItem.Key` — the current category;
- `groupItem.List` — the products included in the current category;
- `item` — the name of the current product in the inner `for` block;
- `totalItem` — the name of the current product inside the `sum` function;
- `totalItem.price * totalItem.quantity` — the product line total used to calculate the subtotal.

For the `Electronics` group, `sum` calculates:

```text
15000 × 2 + 12000 × 1 = 42000
```

For the `Furniture` group:

```text
20000 × 1 + 5000 × 4 = 40000
```

The result is:

```text
Electronics

Monitor — 2 × 15000
Printer — 1 × 12000

Total: 42000


Furniture

Desk — 1 × 20000
Chair — 4 × 5000

Total: 40000
```