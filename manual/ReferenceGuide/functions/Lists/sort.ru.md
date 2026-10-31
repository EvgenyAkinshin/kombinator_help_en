# sort

The `sort` function returns a copy of a list with its items arranged in ascending order.

## Syntax

```text
sort(item in list, expression)
```

**Parameters:**

- `item` — the name of the current list item. It is defined directly in the function and used in the sorting expression;
- `list` — the identifier of the list field whose items should be sorted;
- `expression` — the value used to determine the order of the items.

You can choose the name of the current item yourself. It is used only inside the function.

### List with simple items

If the list contains simple values, sorting can be performed by the value of the current item.

For example:

```text
sort(number in numberList, number)
```

Here:

- `numberList` — the list field identifier;
- `number` — the name of the current list item;
- the second `number` — the value used for sorting.

### List with Struct items

If the list contains Struct items, specify the nested field to sort by.

For example:

```text
sort(product in products, product.price)
```

Here:

- `products` — the list field identifier;
- `product` — the name of the current list item;
- `price` — the nested field identifier;
- `product.price` — the value used for sorting.

## Return value

The function returns a sorted copy of the original list.

The original list is not changed.

To output the sorted items in a document, use the result of `sort` inside a `for` block.

## Examples

### Sorting a list of numbers

Suppose the template contains a list field with the following identifier:

```text
numberList
```

It contains:

| Position | Value |
| ---: | ---: |
| 1 | 8 |
| 2 | 3 |
| 3 | 12 |
| 4 | 5 |

To output the values in ascending order, use `sort` inside a `for` block:

```text
{for(number in sort(item in numberList, item))}
{number}
{/for}
```

Here:

- `numberList` — the identifier of the source list field;
- `item` — the name of the current item inside the `sort` function;
- the second `item` — the value used for sorting;
- `sort(...)` — returns a sorted copy of the list;
- `number` — the name of the current item in the sorted list inside the `for` block.

Result:

```text
3
5
8
12
```

The original `numberList` remains unchanged.

### Sorting products by price

Suppose the template contains a list field with the following identifier:

```text
products
```

Each item is a Struct field containing:

- `name` — the product name field identifier;
- `price` — the product price field identifier.

Source list:

| Position | `name` | `price` |
| ---: | --- | ---: |
| 1 | Monitor | 15000 |
| 2 | Keyboard | 800 |
| 3 | Printer | 12000 |
| 4 | Mouse | 600 |

To output the products in ascending order by price:

```text
{for(item in sort(product in products, product.price))}
{item.name} — {item.price}
{/for}
```

Here:

- `products` — the identifier of the source list field;
- `product` — the name of the current item inside the `sort` function;
- `product.price` — the value used for sorting;
- `sort(...)` — returns a copy of `products` with the items in a different order;
- `item` — the name of the current item in the sorted list inside the `for` block;
- `item.name` and `item.price` — the fields of the current item.

Result:

```text
Mouse — 600
Keyboard — 800
Printer — 12000
Monitor — 15000
```

### Sorting by the result of an expression

An expression can also be used as the sorting criterion.

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

The products need to be sorted by the total cost of each line — `price × quantity`.

Expression:

```text
{for(item in sort(product in products, product.price * product.quantity))}
{item.name}
{/for}
```

For each item, the function calculates the expression value:

| `name` | Calculation | Sorting value |
| --- | --- | ---: |
| Chair | `3500 × 4` | 14000 |
| Desk | `7500 × 1` | 7500 |
| Cabinet | `12000 × 2` | 24000 |

Result:

```text
Desk
Chair
Cabinet
```

The calculated value is used only to determine the item order and is not added to the original list.