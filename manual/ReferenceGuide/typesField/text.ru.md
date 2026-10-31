# «Text» field

The **«Text»** field is used to store text values such as full names, job titles, addresses, phone numbers, company details, contract numbers, and other information.

The field can contain letters, numbers, spaces, punctuation marks, and other characters.

## Creating and adding a field

For instructions on creating and adding fields, see [Creating a template](../Bitrix/creat.md).

## Field value

The field contains a text value.

For example:

```text
John Smith
```

```text
10 Main Street, New York, NY
```

```text
Contract No. 125/2026
```

The field can also be used for values consisting of numbers if they are not intended for mathematical calculations.

For example:

- tax identification number;
- bank identification code;
- registration number;
- bank account number;
- phone number;
- contract number;
- serial number.

## Inserting a field through the «Directives» tab

A text field value can be inserted into the template using the [«Expression»](../directives/expression.md) directive.

1. Place the cursor at the required position in the template.

2. Open the **«Directives»** tab and select **«Expression»**.

3. In the **«Expression»** field, enter the identifier of the text field.

4. Click **«OK»**.

> When the document is generated, the directive is replaced with the value of the specified field.

## Functions for working with the field

A text field value can be used in functions to modify, search, and process text.

### Text functions

- [length](../functions/Text/length.md) — returns the number of characters in a string;
- [trim](../functions/Text/trim.md) — removes spaces at the beginning and end of a string;
- [upper](../functions/Text/upper.md) — converts text to uppercase;
- [lower](../functions/Text/lower.md) — converts text to lowercase;
- [proper](../functions/Text/proper.md) — capitalizes the first letter of each word;
- [mid](../functions/Text/mid.md) — returns part of a string;
- [find](../functions/Text/find.md) — finds a specified fragment in a string;
- [substitute](../functions/Text/substitute.md) — replaces specified text or characters;
- [repeat](../functions/Text/repeat.md) — repeats a string a specified number of times.

### Formatting functions

Some text values can also be processed using formatting functions:

- [инициалы](../functions/Morph/инициалы.md) — changes the format and grammatical case of a full name;
- [окончание](../functions/Morph/окончание.md) — selects an ending depending on gender and number;
- [склонение](../functions/Morph/склонение.md) — changes the grammatical form of a word or phrase by case and number;
- [транслит](../functions/Morph/транслит.md) — converts Cyrillic text to Latin characters.

> Some formatting functions are intended for specific types of text. For example, `инициалы` is used for text containing a person's full name.