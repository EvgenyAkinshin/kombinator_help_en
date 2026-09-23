# if

The `if` function returns one of two values depending on whether a specified condition is met.

The function is useful when the result should change depending on a field value, comparison, or logical condition.

## Syntax

```text
if(condition, valueIfTrue, valueIfFalse)
```

**Parameters:**

- `condition` — the condition that determines the function result. Required;
- `valueIfTrue` — the value returned if the condition is true. Required;
- `valueIfFalse` — the value returned if the condition is false. Required.

The return values can be:

- text;
- numbers;
- field values;
- results of other functions;
- expressions;
- `null`.

## Return value

If the condition is true, the function returns `valueIfTrue`. If the condition is false, it returns `valueIfFalse`.

For example:

```text
if(quantity > 10, 100, 50)
```

If `quantity` is greater than `10`, the result is:

```text
100
```

Otherwise:

```text
50
```

## Conditions

You can use a **Boolean** field as the condition:

```text
if(delivery, "Delivery required", "Delivery not required")
```

If `delivery` = `true`, the function returns `Delivery required`. If `delivery` = `false`, it returns `Delivery not required`.

---

You can also build a condition using comparisons and logical operations.

For example:

```text
if(
    amount >= 50000 и amount <= 100000,
    "Medium deal",
    "Other range"
)
```

For more information about comparisons, logical operations, and expressions, see [Syntax](/../ReferenceGuide/syntax/syntax/).

---

The numeric value `1` can also be used as a true condition:

```text
if(1, "Yes", "No")
```

Result:

```text
Yes
```

## Examples

**Returning field values**

```text
if(
    delivery,
    priceWithDelivery,
    priceWithoutDelivery
)
```

The function returns one of the two field values depending on the value of `delivery`.

---

**Using another function**

```text
if(
    delivery,
    upper(deliveryMethod),
    "Pickup"
)
```

If delivery is required, the function returns the result of `upper`. Otherwise, it returns `Pickup`.

---

**Returning an empty value**

```text
if(delivery, "Delivery", null)
```

If the condition is false, the function returns `null`.

---

**Nested conditions**

You can use `if` inside another `if` function:

```text
if(
    amount > 100000,
    "Large",
    if(
        amount > 50000,
        "Medium",
        "Standard"
    )
)
```

Depending on the value of `amount`, the function returns `Large`, `Medium`, or `Standard`.

## Errors

All three parameters are required.

For example:

```text
if(delivery, "Yes")
```

returns an error because the third parameter is missing.

An error also occurs if the supplied condition cannot be processed by the function.

For example:

```text
if("text", "Yes", "No")
```

returns an error.