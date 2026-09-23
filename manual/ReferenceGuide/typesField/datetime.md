# «Date/Time» field

The **«Date/Time»** field is used to store values that contain both a date and a time. The field value can be displayed in different formats and processed using functions.

It is suitable, for example, for meeting dates and times, order dates, document creation dates, and event start or end times.

## Creating and adding a field

For instructions on creating and adding fields, see [Creating a template](../Bitrix/creat.md).

## Field value

The field contains both a date and a time.

When adding the field to the template through **Fields**, you can select the format in which its value should be displayed in the generated document. The same field value can therefore be displayed in different formats.

If needed, you can extract individual parts of the value using the corresponding functions: [year](../functions/Date/year.md), [month](../functions/Date/month.md), [day](../functions/Date/day.md), [hour](../functions/Date/hour.md), [minute](../functions/Date/minute.md), or [second](../functions/Date/second.md).

## Inserting a field through the «Directives» tab

The **«Date/Time»** field value can be inserted into the template using the [«Expression»](../directives/expression.md) directive.

In the **«Expression»** field, specify the field whose value should be inserted.

For example:

```text
deals.meetingDate
```

Where:

- `deals` — the Bitrix24 entity from which the data is retrieved;
- `meetingDate` — the field containing the date and time.

When the document is generated, the directive is replaced with the value of this field.

You can also use functions in the **«Expression»** directive to process or format the date and time.

For example, the [formatDate](../functions/Morph/formatDate.md) function can be used to display only the date in the required format.

## Functions for working with the field

The **«Date/Time»** field supports functions for extracting individual parts of the value, changing the date, and formatting the result.

### Extracting date and time parts

- [year](../functions/Date/year.md) — returns the year;
- [month](../functions/Date/month.md) — returns the month number;
- [day](../functions/Date/day.md) — returns the day of the month;
- [hour](../functions/Date/hour.md) — returns the hour;
- [minute](../functions/Date/minute.md) — returns the minutes;
- [second](../functions/Date/second.md) — returns the seconds;
- [weekday](../functions/Date/weekday.md) — returns the day-of-week number;
- [weeknum](../functions/Date/weeknum.md) — returns the week number.

### Changing the date

- [edate](../functions/Date/edate.md) — shifts the date by the specified number of months;
- [dateshift](../functions/Date/dateshift.md) — shifts the date by the specified number of days;
- [bomonth](../functions/Date/bomonth.md) — returns the first day of the month;
- [eomonth](../functions/Date/eomonth.md) — returns the last day of the month;
- [datediff](../functions/Date/datediff.md) — calculates the difference between dates.

### Formatting functions

- [formatDate](../functions/Morph/formatDate.md) — changes how the date is displayed.