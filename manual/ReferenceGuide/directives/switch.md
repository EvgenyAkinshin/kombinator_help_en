# Switch

The **«Switch»** directive is used when the document should display one of several content options depending on a field value.

![29](../img/directives/29.png)

Kombinator retrieves the specified field value, compares it with the configured **Case** values, and inserts the content of the matching block.

For example, depending on the `counterpartyType` field, you can display different text for an LLC, a sole proprietor, or an individual.

## Directive structure

The directive consists of:

- an opening **«Switch»** directive — specifies the field or expression whose value should be checked;
- one or more **«Case»** blocks — define content for specific values;
- an optional **«Default»** block — defines content to use when no Case value matches;
- a closing **«/Switch»** directive.

Общая структура:

```text
{switch(field)}

{case("Value 1")}

Content for the first value.

{case("Value 2")}

Content for the second value.

{default}

Content displayed if no value matches.

{/switch}
```

## Value to check

In the opening **«Switch»** directive, specify the field whose value Kombinator should compare with the **Case** values.

For example:

```text
counterpartyType
```

To reference a nested field, specify the full path using a period (`.`):

```text
counterparty.type
```

Field reference rules are described in [«Basic rules»](../syntax/syntax.md).

## «Case» block

dd a separate **«Case»** block for each value that should display its own content.

For example:

```text
{switch(counterpartyType)}

{case("LLC")}

Text for a legal entity.

{case("Sole proprietor")}

Text for a sole proprietor.

{case("Individual")}

Text for an individual.

{/switch}
```

If the `counterpartyType` field contains `"Sole proprietor"`, only the content of the corresponding **Case** block will be included in the document:

```text
Text for a sole proprietor.
```

The value specified in **«Case»** must exactly match the value of the field being checked.

For text values, letter case is taken into account. For example, `"LLC"` and `"llc"` are treated as different values.

## «Default» block

Use **«Default»** when you need to display content if none of the **Case** values match the field value.

For example:

```text
{switch(counterpartyType)}

{case("LLC")}

Legal entity.

{case("Sole proprietor")}

Sole proprietor.

{default}

Other counterparty type.

{/switch}
```

If the field value does not match either `"LLC"` or `"Sole proprietor"`, the document will contain:

```text
Other counterparty type.
```

The **«Default»** block is optional. If it is not added and no matching **Case** is found, nothing is inserted at the position of the directive.

## «Switch» and «Condition expression»

The **«Switch»** and [«Condition expression»](if.md) directives both control which content is included in the document, but they are used for different tasks.

Use **«Switch»** when one field can contain several possible values and each value should display different content.

For example:

```text
LLC
Sole proprietor
Individual
```

Use **«Condition expression»** when you need to evaluate a logical expression:

```text
amount > 100000
```

or combine several conditions:

```text
amount > 100000 и approval
```

If you need to select one of several content options based on the value of a single field, use **«Switch»**.