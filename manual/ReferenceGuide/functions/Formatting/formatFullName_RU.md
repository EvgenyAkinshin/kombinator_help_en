# formatFullName_RU

The **`formatFullName_RU`** function formats a person's full name according to the specified format and grammatical case.

## Syntax

```text
formatFullName_RU(Expression for the name, Grammatical case, Format)
```

**Parameters:**

- **`Expression for the name`** — required. The text value containing the person's full name.
- **`Grammatical case`** — required. Specifies the grammatical case in which the full name should be displayed.
- **`Format`** — required. Specifies which parts of the full name should be included and how they should be displayed.

The following values are available for the **`Grammatical case`** parameter:

| Value | Russian case questions |
|---|---|
| `GrammaticalCase_RU.Nominative` | кто? что? |
| `GrammaticalCase_RU.Genitive` | кого? чего? |
| `GrammaticalCase_RU.Dative` | кому? чему? |
| `GrammaticalCase_RU.Accusative` | кого? что? |
| `GrammaticalCase_RU.Instrumental` | кем? чем? |
| `GrammaticalCase_RU.Prepositional` | о ком? о чём? |

The following values are available for the **`Format`** parameter:

| Value | Result |
|---|---|
| `SurnameNamePatronymic` | Иванов Иван Иванович |
| `SurnameName` | Иванов Иван |
| `NamePatronymic` | Иван Иванович |
| `SurnameInitials` | Иванов И.И. |
| `InitialsSurname` | И.И. Иванов |
| `Surname` | Иванов |
| `Name` | Иван |
| `Patronymic` | Иванович |

## Return Value

The function returns a text value containing the person's full name in the selected format and grammatical case.

For example, suppose the `FullName` field contains:

```text
Иванов Иван Иванович
```

The expression:

```text
formatFullName_RU(
    FullName,
    GrammaticalCase_RU.Nominative,
    FullNameFormat_RU.SurnameInitials
)
```

Returns:

```text
Иванов И.И.
```

## Notes

When a grammatical case is specified, the function declines the parts of the full name included in the selected format.

For example, if the **`Surname`** format and **`Dative`** case are selected, the function returns the surname in the dative case.

If a full name is declined incorrectly, you can specify the required form using grammatical exceptions in the template-filling interface.

## Examples

### Initials Before the Surname

Suppose the `FullName` field contains:

```text
Иванов Иван Иванович
```

The expression:

```text
formatFullName_RU(
    FullName,
    GrammaticalCase_RU.Nominative,
    FullNameFormat_RU.InitialsSurname
)
```

Returns:

```text
И.И. Иванов
```

### Surname in the Dative Case

Suppose the `FullName` field contains:

```text
Иванов Иван Иванович
```

The expression:

```text
formatFullName_RU(
    FullName,
    GrammaticalCase_RU.Dative,
    FullNameFormat_RU.Surname
)
```

Returns:

```text
Иванову
```

### Name and Patronymic in the Genitive Case

Suppose the `FullName` field contains:

```text
Иванов Иван Иванович
```

The expression:

```text
formatFullName_RU(
    FullName,
    GrammaticalCase_RU.Genitive,
    FullNameFormat_RU.NamePatronymic
)
```

Returns:

```text
Ивана Ивановича
```

## Errors

All three parameters are required.

For example, the following expression is incomplete:

```text
formatFullName_RU(
    FullName,
    GrammaticalCase_RU.Nominative
)
```

The **`Format`** parameter is missing, so the expression will return an error when evaluated.

You must also use valid values for the **`Grammatical case`** and **`Format`** parameters.

## Using with Other Functions

The result of **`formatFullName_RU`** can be passed to other functions that process text.

For example, the **`upper`** function converts the formatted full name to uppercase:

```text
upper(
    formatFullName_RU(
        FullName,
        GrammaticalCase_RU.Nominative,
        FullNameFormat_RU.SurnameInitials
    )
)
```

Returns:

```text
ИВАНОВ И.И.
```