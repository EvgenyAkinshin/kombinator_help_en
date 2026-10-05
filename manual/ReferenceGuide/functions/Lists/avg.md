# avg

The `avg` function calculates the arithmetic mean of numeric values from list items.

A numeric field or an expression can be used as the value for the calculation.

## Syntax

```text
avg(item in list, expression)
```

**Parameters:**

- `item` — the current list item;
- `list` — the identifier of the list field;
- `expression` — a numeric value or expression whose result is included in the arithmetic mean calculation.

### List with Struct items

If each list item is a Struct field, you can assign any valid name to the current item and use it to access nested fields.

For example:

```text
avg(product in products, product.price)
```

Here:

- `products` — the list field identifier;
- `product` — the name of the current item defined directly in the function;
- `price` — the nested numeric field identifier;
- `product.price` — the value used to calculate the arithmetic mean.

You can choose the name of the current item yourself. For example, instead of `product`, you can use `item`:

```text
avg(item in products, item.price)
```

### List with simple items

If the list contains simple numeric values, the current item itself is used in the expression.

Suppose the `ratings` list contains numeric values.

Expression:

```text
avg(rating in ratings, rating)
```

In this case, each value in the list is used directly in the calculation.

## Return value

The function returns a number — the arithmetic mean of the expression results for all items in the list.

## Examples

### Calculating the average product price

Suppose the template contains a list field with the following identifier:

```text
products
```

Each item is a Struct field containing:

- `name` — product name;
- `price` — product price.

The list contains:

| `name` | `price` |
| --- | ---: |
| Monitor | 15000 |
| Keyboard | 800 |
| Printer | 12000 |
| Mouse | 600 |

To calculate the average product price, use:

```text
avg(product in products, product.price)
```

Here:

- `products` — the list field identifier;
- `product` — the name of the current item defined inside the `avg` function;
- `price` — the numeric field identifier inside the item;
- `product.price` — the value retrieved from each list item.

Result:

```text
7100
```

### Calculating the average of a simple numeric list

Suppose the template contains a list field:

```text
ratings
```

The list contains:

```text
4
5
3
5
```

Expression:

```text
avg(rating in ratings, rating)
```

returns:

```text
4.25
```

### Calculating the average result of an expression

The second parameter can also contain an expression.

Suppose the `products` list contains:

- `name` — product name;
- `price` — unit price;
- `quantity` — product quantity.

Source data:

| `name` | `price` | `quantity` |
| --- | ---: | ---: |
| Monitor | 15000 | 2 |
| Keyboard | 800 | 5 |
| Printer | 12000 | 1 |
| Mouse | 600 | 10 |

You need to calculate the average total cost of a product line based on its quantity.

Expression:

```text
avg(product in products, product.price * product.quantity)
```

For each item, the function first calculates the line total:

| `name` | Calculation | Value |
| --- | --- | ---: |
| Monitor | `15000 × 2` | 30000 |
| Keyboard | `800 × 5` | 4000 |
| Printer | `12000 × 1` | 12000 |
| Mouse | `600 × 10` | 6000 |

The function then calculates the arithmetic mean of these values.

Result:

```text
13000
```