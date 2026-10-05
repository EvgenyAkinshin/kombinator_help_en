# match

The `match` function finds the first list item that satisfies a specified condition and returns its position.

## Syntax

```text
match(item in list, condition)
```

**Parameters:**

- `item` — the current list item used in the condition;
- `list` — the list in which the search is performed;
- `condition` — a Boolean expression that determines whether the current item matches. The condition must return `true` or `false`.

### List with a Struct item

If the list contains Struct items, you can assign any valid name to the current item and use it to access nested fields.

For example:

```text
match(
    product in products,
    product.price > 5000
)
```

Here:

- `product` — the name of the current list item;
- `products` — the list field identifier;
- `product.price` — the `price` field of the current Struct item.

The current item name is used only inside the function expression. For example, instead of `product`, you can use `item`, `position`, `_1`, or another valid name:

```text
match(
    position in products,
    position.price > 5000
)
```

### List with a simple item

If the list contains simple values, such as text or numbers, the condition is applied directly to the current item.

For example, for a list of numbers:

```text
match(
    number in numbers,
    number >= 5
)
```

The function finds the position of the first value greater than or equal to `5`.

## Return value

The function returns an integer — the position of the first list item for which the condition returns `true`.

List positions start at `1`.

If no item matches the condition, the function does not return a position.

## Features

The search starts from the beginning of the list. If several items match the condition, only the position of the first matching item is returned.

The function returns the item position, not the item itself or the value of one of its fields.

## Examples

### Finding the first product with a price greater than 5,000

Suppose the template contains a list field with the following identifier:

```text
products
```

Each item in `products` is a Struct field containing:

- `name` — product name;
- `price` — product price.

For example:

| Position | `name` | `price` |
| ---: | --- | ---: |
| 1 | Chair | 3500 |
| 2 | Desk | 7500 |
| 3 | Cabinet | 12000 |

To find the position of the first product with a price greater than `5000`, use:

```text
match(
    product in products,
    product.price > 5000
)
```

Here:

- `products` — the list field identifier in the template;
- `product` — the name assigned to the current list item;
- `price` — the nested field identifier;
- `product.price` — the `price` value of the current item.

The function checks the items in order:

```text
3500 > 5000 → false
7500 > 5000 → true
```

The second item is the first one that matches the condition, so the function returns:

```text
2
```

### Finding a value in a list of numbers

Suppose the template contains a list field with the following identifier:

```text
numbers
```

The list contains:

```text
2
4
7
9
```

To find the position of the first value greater than or equal to `5`, use:

```text
match(
    number in numbers,
    number >= 5
)
```

Here:

- `number` — the name assigned to the current list item;
- `numbers` — the list field identifier;
- `number >= 5` — the condition checked for each item.

The function checks the values in order:

```text
2 >= 5 → false
4 >= 5 → false
7 >= 5 → true
```

The first matching value is in the third position, so the function returns:

```text
3
```

## Using with other functions

The result of `match` can be passed to the `index` function to retrieve the matching list item or one of its fields.

For example, to get the name of the first product with a price greater than `5000`:

```text
index(
    products,
    match(
        product in products,
        product.price > 5000
    )
).name
```

For the following list:

| Position | `name` | `price` |
| ---: | --- | ---: |
| 1 | Chair | 3500 |
| 2 | Desk | 7500 |
| 3 | Cabinet | 12000 |

the expression returns:

```text
Desk
```

First, `match` finds the position of the first matching item. Then `index` retrieves the `name` field from that item.