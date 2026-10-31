# count

The `count` function determines the number of items in a list.

## Syntax

```text
count(item in list)
```

**Parameters:**

- `item` — the name of the current list item. It is defined directly in the function;
- `list` — the identifier of the list field whose items should be counted.

For example:

```text
count(product in products)
```

Here:

- `products` — the list field identifier in the template;
- `product` — the name of the list item defined directly in the function.

You can choose the item name yourself. It is used only inside the function expression.

## Return value

The function returns an integer — the number of items in the list.

## Examples

### Counting list items

Suppose the template contains a list field with the following identifier:

```text
products
```

The list contains:

| Position | Name |
| ---: | --- |
| 1 | Monitor |
| 2 | Keyboard |
| 3 | Printer |
| 4 | Mouse |

Expression:

```text
count(product in products)
```

returns:

```text
4
```

Here:

- `products` — the list field identifier;
- `product` — the name of the list item defined inside the `count` function.

### Counting items that match a condition

The `count` function can be applied to a list returned by `filter`.

Suppose the `products` list contains:

| `name` | `price` |
| --- | ---: |
| Monitor | 15000 |
| Keyboard | 800 |
| Printer | 12000 |
| Mouse | 600 |

You need to determine how many products have a price greater than `5000`.

Expression:

```text
count(
    product in filter(
        item in products,
        item.price > 5000
    )
)
```

Here:

- `products` — the identifier of the source list field;
- `item` — the name of the current item inside the `filter` function;
- `item.price > 5000` — the filtering condition;
- `filter(...)` — returns a new list containing only matching products;
- `product` — the name of an item in the filtered list inside the `count` function.

After filtering, the list contains:

```text
Monitor — 15000
Printer — 12000
```

Therefore, `count` returns:

```text
2
```

### Getting the last item in a list

The result of `count` can be used as an item position in the `index` function.

Suppose the template contains a list field:

```text
payments
```

Each list item contains the following field:

```text
balance
```

You need to get the `balance` value from the last item in the list, while the number of items is not known in advance.

Expression:

```text
index(
    payments,
    count(payment in payments)
).balance
```

Here:

- `payments` — the list field identifier;
- `payment` — the name of the list item inside the `count` function;
- `count(...)` — returns the number of items in the list;
- the returned number is used by `index` as the position of the last item;
- `balance` — the nested field identifier whose value should be returned.

For example, if the list contains four items:

```text
count(payment in payments)
```

returns:

```text
4
```

The expression then effectively becomes:

```text
index(payments, 4).balance
```

and returns the `balance` value from the last item in the list.