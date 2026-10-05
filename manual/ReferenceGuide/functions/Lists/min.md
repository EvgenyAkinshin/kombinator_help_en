# min

The `min` function determines the minimum numeric value in a list.

## Syntax

```text
min(item in list, expression)
```

**Parameters:**

- `item` — the name of the current list item. It is defined directly in the function and used in the expression;
- `list` — the identifier of the list field;
- `expression` — a numeric value or expression whose minimum result should be determined.

You can choose the name of the current item yourself. It is used only inside the function.

### List with simple items

If the list contains numeric values, use the current item in the expression.

For example:

```text
min(number in numberList, number)
```

Here:

- `numberList` — the list field identifier;
- `number` — the name of the current list item;
- the second `number` — the value used to determine the minimum.

### List with Struct items

If the list contains Struct items, specify the required numeric field in the expression.

For example:

```text
min(product in products, product.price)
```

Here:

- `products` — the list field identifier;
- `product` — the name of the current item;
- `price` — the nested numeric field identifier;
- `product.price` — the value used to determine the minimum.

## Return value

The function returns the minimum result of the expression across all items in the list.

## Examples

### Finding the minimum product price

Suppose the template contains a list field:

```text
products
```

Each item is a Struct field containing:

- `name` — product name;
- `price` — product price.

Source data:

| `name` | `price` |
| --- | ---: |
| Monitor | 15000 |
| Keyboard | 800 |
| Printer | 12000 |
| Mouse | 600 |

Expression:

```text
min(product in products, product.price)
```

Here:

- `products` — the list field identifier;
- `product` — the name of the current item inside the `min` function;
- `price` — the nested field identifier;
- `product.price` — the value used in the comparison.

The function compares:

```text
15000
800
12000
600
```

and returns:

```text
600
```

The function returns the minimum price value, not the `Mouse` list item itself.

### Finding the minimum result of an expression

The second parameter can also contain an expression.

Suppose the `products` list also contains the following field:

```text
quantity
```

Source data:

| `name` | `price` | `quantity` |
| --- | ---: | ---: |
| Chair | 3500 | 4 |
| Desk | 7500 | 1 |
| Cabinet | 12000 | 2 |

You need to determine the minimum total cost of a product line based on its quantity.

Expression:

```text
min(product in products, product.price * product.quantity)
```

For each item, the function first calculates:

| `name` | Calculation | Result |
| --- | --- | ---: |
| Chair | `3500 × 4` | 14000 |
| Desk | `7500 × 1` | 7500 |
| Cabinet | `12000 × 2` | 24000 |

The function returns:

```text
7500
```