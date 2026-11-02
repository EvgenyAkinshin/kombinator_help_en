# «Date/Time» field

The **«Date/Time»** field is used to store values that contain both a date and a time. The field value can be displayed in different formats and processed using functions.

It is suitable, for example, for meeting dates and times, order dates, document creation dates, and event start or end times.

## Creating and adding a field

For instructions on creating and adding fields, see [Creating a template](../Bitrix/creat.md).

## Field value

The field contains both a date and a time.

When adding the field to the template through **Fields**, you can select the format in which its value should be displayed in the generated document. The same field value can therefore be displayed in different formats.

If needed, you can extract individual parts of the value using the corresponding functions: [year](../functions/Date and time/year.md), [month](../functions/Date and time/month.md), [day](../functions/Date and time/day.md), [hour](../functions/Date and time/hour.md), [minute](../functions/Date and time/minute.md), or [second](../functions/Date and time/second.md).

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

For example, the [formatDate](../functions/Formatting/formatDate.md) function can be used to display only the date in the required format.

## Functions for working with the field

The **«Date/Time»** field supports functions for extracting individual parts of the value, changing the date, and formatting the result.

### Extracting date and time parts

- [year](../functions/Date and time/year.md) — returns the year;
- [month](../functions/Date and time/month.md) — returns the month number;
- [day](../functions/Date and time/day.md) — returns the day of the month;
- [hour](../functions/Date and time/hour.md) — returns the hour;
- [minute](../functions/Date and time/minute.md) — returns the minutes;
- [second](../functions/Date and time/second.md) — returns the seconds;
- [weekday](../functions/Date and time/weekday.md) — returns the day-of-week number;
- [weeknum](../functions/Date and time/weeknum.md) — returns the week number.

### Changing the date

- [edate](../functions/Date and time/edate.md) — shifts the date by the specified number of months;
- [dateshift](../functions/Date and time/dateshift.md) — shifts the date by the specified number of days;
- [bomonth](../functions/Date and time/bomonth.md) — returns the first day of the month;
- [eomonth](../functions/Date and time/eomonth.md) — returns the last day of the month;
- [datediff](../functions/Date and time/datediff.md) — calculates the difference between dates.

### Formatting functions

- [formatDate](../functions/Formatting/formatDate.md) — changes how the date is displayed.