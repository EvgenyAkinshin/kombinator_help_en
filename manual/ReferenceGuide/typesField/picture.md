# «Picture» field

The **«Picture»** field is used to pass an image from Bitrix24 to a template and insert it into the generated document.

## Creating and adding a field

For instructions on creating and adding fields, see [Creating a template](../Bitrix/creat.md).

## Adding an image to the template

The **«Picture»** field can be added to the template from **Fields** or through the **«Directives»** tab.

### From Fields

When inserting a **«Picture»** field from **Fields** using **«Insert expression»**, a window with image settings opens.

After confirming the settings, an image placeholder with the specified dimensions appears in the template.

### Through the «Directives» tab

An image can also be inserted using the [«Picture»](../directives/picture.md) directive.

In the **«Expression»** field, specify the **Picture** field from which the image should be retrieved.

For example:

```text
deals.logo
```

Only a **Picture** field can be used in **«Expression»**.

### By height

The image height is set to the specified value, while the width is calculated proportionally.

For example, if the following values are set:

```text
Height: 3 cm
Width: 4 cm
```

but the proportional width is `6 cm`, the resulting image size will be:

```text
3 × 6 cm
```

In this mode, the specified width does not limit the image size.

### By width

The image width is set to the specified value, while the height is calculated proportionally.

For example, if the following values are set:

```text
Height: 3 cm
Width: 4 cm
```

but the proportional height is `5 cm`, the resulting image size will be:

```text
5 × 4 cm
```

In this mode, the specified height does not limit the image size.

### By height and width

The image is resized proportionally so that it does not exceed either the specified height or width.

For example, if the following values are set:

```text
Height: 3 cm
Width: 5 cm
```

the image will be fitted within `3 × 5 cm`. One of the sides may be smaller than the specified value.

## Picture in the template

After the image is inserted, a placeholder appears in the template showing its position and size.

You can resize the placeholder manually in the editor. The updated width and height are saved and used when the document is generated.

The image is placed **inline with text**, so its position depends on where it is inserted.

When the document is generated, the placeholder is replaced with the image retrieved from the selected **Picture** field.

## Functions for working with the field

The **«Picture»** field does not have dedicated functions.