# filter

The `filter` function selects list items that match a specified condition.

## Syntax

```text
filter(item in list, condition)
```

**Parameters:**

- `item` — the name of the current list item. It is defined directly in the function and used in the condition;
- `list` — the identifier of the list field;
- `condition` — a Boolean expression that determines whether the current item should be included in the result.

You can choose the name of the current item yourself. It is used only inside the function.

For example:

```text
filter(product in products, product.price > 5000)
```

Here:

- `products` — the list field identifier;
- `product` — the name of the current item defined inside the function;
- `price` — the nested field identifier;
- `product.price > 5000` — the filtering condition.

Only products with a price greater than `5000` are included in the result.

## Return value

The function returns a new list containing only the items for which the condition returns `true`.

The original list is not changed.

The result of `filter(...)` can be used instead of the original list:

- in a `for` or `t_for` block;
- in other list functions;
- in aggregate functions such as `count`, `sum`, `avg`, `min`, and `max`.

This allows you to filter the required items first and then perform calculations only on those items.

## Examples

### Outputting only matching list items

Suppose the template contains a list field:

```text
products
```

Each item contains:

- `name` — product name;
- `price` — product price.

Source list:

| `name` | `price` |
| --- | ---: |
| Monitor | 15000 |
| Keyboard | 800 |
| Printer | 12000 |
| Mouse | 600 |

You need to output only products with a price greater than `5000`.

```text
{for(item in filter(product in products, product.price > 5000))}
{item.name} — {item.price}
{/for}
```

Here:

- `products` — the identifier of the source list field;
- `product` — the name of the current item inside the `filter` function;
- `product.price > 5000` — the filtering condition;
- `filter(...)` — returns a new list containing only matching products;
- `item` — the name of the current item in the filtered list inside the `for` block.

Result:

```text
Monitor — 15000
Printer — 12000
```

The original `products` list remains unchanged.

### Calculating a sum for a filtered list

The result of `filter` can be passed directly to an aggregate function.

Suppose the `products` list contains:

| `name` | `price` | `quantity` |
| --- | ---: | ---: |
| Monitor | 15000 | 2 |
| Keyboard | 800 | 5 |
| Printer | 12000 | 1 |
| Mouse | 600 | 10 |

You need to calculate the total cost only for products whose unit price is greater than `5000`.

First, `filter` selects the matching items:

```text
filter(product in products, product.price > 5000)
```

The resulting list contains:

| `name` | `price` | `quantity` |
| --- | ---: | ---: |
| Monitor | 15000 | 2 |
| Printer | 12000 | 1 |

The filtered list can then be passed directly to `sum`:

```text
sum(
    item in filter(
        product in products,
        product.price > 5000
    ),
    item.price * item.quantity
)
```

Here:

- `product` — the name of the source list item inside `filter`;
- `filter(...)` — returns a list of products with a price greater than `5000`;
- `item` — the name of the filtered list item inside `sum`;
- `item.price * item.quantity` — the value calculated for each item and included in the sum.

The calculation uses:

```text
15000 × 2 = 30000
12000 × 1 = 12000
```

The function returns:

```text
42000
```

In the same way, a filtered list can be passed to `count`, `avg`, `min`, or `max` when a calculation needs to be performed only for items that match a specified condition.