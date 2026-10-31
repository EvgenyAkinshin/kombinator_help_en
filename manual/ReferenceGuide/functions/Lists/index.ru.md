# index

The `index` function returns a list item by its position.

List positions start at `1`: the first item has position `1`, the second has position `2`, and so on.

## Syntax

For a list with simple items:

```text
index(list, position)
```

**Parameters:**

- `list` — the identifier of the list field from which the item should be retrieved;
- `position` — the position of the item. You can specify a number or an expression that returns a position.

For example:

```text
index(stages, 2)
```

returns the second item from the `stages` list.

### List with Struct items

If the list contains Struct items, specify the identifier of the required nested field after the function using dot notation:

```text
index(list, position).field
```

For example:

```text
index(products, 2).name
```

Here:

- `products` — the list field identifier;
- `2` — the item position;
- `name` — the nested field identifier.

## Examples

### Getting an item by position

Suppose the template contains a list field with the following identifier:

```text
stages
```

The list contains:

| Position | Value |
| ---: | --- |
| 1 | Preparation |
| 2 | Approval |
| 3 | Signing |

The expression:

```text
index(stages, 2)
```

returns:

```text
Approval
```

Here:

- `stages` — the list field identifier;
- `2` — the item position in the list.

### Getting a field from the first item that matches a condition

Suppose the template contains a list field:

```text
products
```

Each list item is a Struct field containing:

- `name` — the identifier of the product name field;
- `price` — the identifier of the product price field.

The list contains:

| Position | `name` | `price` |
| ---: | --- | ---: |
| 1 | Chair | 3500 |
| 2 | Desk | 7500 |
| 3 | Cabinet | 12000 |

You need to get the name of the first product with a price greater than `5000`.

Expression:

```text
index(
    products,
    match(
        product in products,
        product.price > 5000
    )
).name
```

Here:

- `products` — the list field identifier in the template;
- `product` — the name of the current item defined inside the `match` function;
- `price` — the nested field identifier;
- `match(...)` — returns the position of the first matching item;
- `index(...)` — returns the item at that position;
- `name` — the field of the matching item whose value should be returned.

The `match` function checks the items in order:

```text
3500 > 5000 → false
7500 > 5000 → true
```

The second item is the first one that matches the condition, so the expression effectively becomes:

```text
index(products, 2).name
```

Result:

```text
Desk
```

### Getting a value from the last item in a list

Suppose the template contains a list field:

```text
payments
```

Each list item is a Struct field containing:

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
- `payment` — the name of the current item defined inside the `count` function;
- `count(...)` — returns the number of items in the list;
- the returned value is used as the position of the last item;
- `balance` — the nested field identifier whose value should be returned.

If the list contains four items:

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