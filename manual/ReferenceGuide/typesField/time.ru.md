# «Time» field

The **«Time»** field is used to store time values. The field value can be displayed in different formats and processed using functions.

It is suitable, for example, for meeting times, event start or end times, document sending times, and other scheduled actions.

## Creating and adding a field

For instructions on creating and adding fields, see [Creating a template](../Bitrix/creat.md).

## Field value

The field contains a time value without a calendar date.

When adding the field to the template through **Fields**, you can select the format in which its value should be displayed in the generated document. The same field value can therefore be displayed in different formats.

If needed, you can extract individual parts of the value using the corresponding functions: [hour](../functions/Date/hour.md), [minute](../functions/Date/minute.md), or [second](../functions/Date/second.md).

## Inserting a field through the «Directives» tab

The **«Time»** field value can be inserted into the template using the [«Expression»](../directives/expression.md) directive.

In the **«Expression»** field, specify the field whose value should be inserted.

For example:

```text
deals.meetingTime
```

Where:

- `deals` — the Bitrix24 entity from which the data is retrieved;
- `meetingTime` — the field containing the time.

When the document is generated, the directive is replaced with the value of this field.

You can also use functions in the **«Expression»** directive to process or format the time.

For example, the [formatDate](../functions/Morph/formatDate.md) function can be used to display the time in the required format.

## Functions for working with the field

The **«Time»** field supports functions for extracting individual parts of the value and changing how it is displayed.

### Extracting time parts

- [hour](../functions/Date/hour.md) — returns the hour;
- [minute](../functions/Date/minute.md) — returns the minutes;
- [second](../functions/Date/second.md) — returns the seconds.

### Formatting functions

- [formatDate](../functions/Morph/formatDate.md) — changes how the time is displayed.