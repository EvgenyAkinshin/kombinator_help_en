# sum

The `sum` function calculates the sum of numeric values from list items.

## Syntax

```text
sum(item in list, expression)
```

**Parameters:**

- `item` — the name of the current list item. It is defined directly in the function and used in the expression;
- `list` — the identifier of the list field;
- `expression` — a numeric value or expression whose results should be added together.

You can choose the name of the current item yourself. It is used only inside the function.

### List with simple items

If the list contains numeric values, use the current item in the expression.

For example:

```text
sum(number in numberList, number)
```

Here:

- `numberList` — the list field identifier;
- `number` — the name of the current list item;
- the second `number` — the value included in the sum.

### List with Struct items

If the list contains Struct items, specify the required numeric field in the expression.

For example:

```text
sum(product in products, product.quantity)
```

Here:

- `products` — the list field identifier;
- `product` — the name of the current item;
- `quantity` — the nested numeric field identifier;
- `product.quantity` — the value included in the sum.

## Return value

The function returns the sum of the expression results for all items in the list.

## Examples

### Calculating the total quantity of products

Suppose the template contains a list field:

```text
products
```

Each item is a Struct field containing:

- `name` — product name;
- `quantity` — product quantity.

Source data:

| `name` | `quantity` |
| --- | ---: |
| Monitor | 2 |
| Keyboard | 5 |
| Printer | 1 |
| Mouse | 10 |

To calculate the total quantity of products, use:

```text
sum(product in products, product.quantity)
```

Here:

- `products` — the list field identifier;
- `product` — the name of the current item inside the `sum` function;
- `quantity` — the nested field identifier;
- `product.quantity` — the value added to the total.

The function adds:

```text
2 + 5 + 1 + 10
```

and returns:

```text
18
```

### Calculating the total cost of products

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

To calculate the total cost of all products:

```text
sum(product in products, product.price * product.quantity)
```

For each item, the function first calculates the line total:

| `name` | Calculation | Result |
| --- | --- | ---: |
| Monitor | `15000 × 2` | 30000 |
| Keyboard | `800 × 5` | 4000 |
| Printer | `12000 × 1` | 12000 |
| Mouse | `600 × 10` | 6000 |

The function then adds the calculated values:

```text
30000 + 4000 + 12000 + 6000
```

Result:

```text
52000
```