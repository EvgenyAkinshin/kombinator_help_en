# Table

The **«Table»** directive is used to control table rows when generating a document.

It allows you to repeat rows for list items, display rows only when a condition is met, and vertically merge adjacent cells.

![«Table» directive](../img/directives/31.png)

## Table for

**«Table for»** is used to display data from a **List** field in a table.

![Table for](../img/directives/66.png)

### Table for structure

The opening directive has the following structure:

```text
{t_for(employee in employeeList)}
```

Где:

Where:

- `employeeList` — the **List** field whose items should be processed;
- `employee` — the name used to reference the current list item.

If a list item is a composite field, its nested fields are referenced using a period (`.`):

```text
employee.fullName
employee.position
employee.workExperience
```

The current item variable can be changed.

For example:

```text
{t_for(data in employeeList)}
```

In this case, the nested fields must also be referenced using the new variable:

```text
data.fullName
data.position
data.workExperience
```

The **Table for** block must be closed with:

```text
{/t_for}
```

The opening `t_for` and closing `/t_for` directives must each be placed in a separate table row.

Do not add text, values, or other directives to the rows containing `t_for` and `/t_for`. These rows are used only to define the beginning and end of the repeating table block.

### Which rows are repeated

**Table for** repeats the entire table block located between `t_for` and `/t_for`.

For one list item, the repeating block may contain a single row:

![One row inside Table for](../img/directives/88.png)

or multiple rows:

![Multiple rows inside Table for](../img/directives/89.png)

The repeating block can also contain other directives and additional logic:

![Additional logic inside Table for](../img/directives/90.png)

For example, if the block contains three rows, all three rows will be generated for each item in the list.

Therefore, the number of rows in the generated table depends not only on the number of list items but also on the structure placed inside **Table for**.

## Table if

**«Table if»** controls whether specific table rows are included in the generated document.

Rows placed between `t_if` and `/t_if` are included only when the specified condition is met.

![Table if](../img/directives/59.png)

### Table if structure

**Table if** consists of an opening `t_if` directive containing a condition and a closing `/t_if` directive.

For example:

```text
{t_if(data.workExperience > 3)}

...

{/t_if}
```

If the expression `data.workExperience > 3` returns `истина`, the rows inside the block are included in the document.

If it returns `ложь`, the rows are not included.

A **Boolean** field or a logical expression can be used as the condition.

The opening `t_if` and closing `/t_if` directives must each be placed in a separate table row.

Do not add text, values, or other directives to the rows containing `t_if` and `/t_if`. These rows are used only to define the beginning and end of the conditional block.

### Table if inside Table for

**Table if** can be placed inside **Table for** to evaluate a condition separately for each list item.

The structure may look like this:

![Table for with Table if](../img/directives/22.png)

**Table for** processes all employees in the list, while **Table if** checks the condition for each employee individually.

Rows containing employee data will be generated only for employees for whom the condition `data.workExperience > 3` is met.

## V_Merge

**«V_Merge»** is used to merge adjacent table cells vertically.

Place the directive inside a cell in the column where the cells should be merged.

![V_Merge](../img/directives/70.png)

### How V_Merge works

The directive contains an expression:

```text
v_merge(expression)
```

When the document is generated, Kombinator compares the result of this expression in adjacent rows.

If the results are the same, the corresponding cells are merged vertically. When the result changes, a new group begins.

For example:

```text
v_merge(data.type)
```

If `data.type` contains the following values:

```text
Installation
Installation
Installation
Delivery
Delivery
```

the cells containing `Installation` will be merged into one group, while the cells containing `Delivery` will be merged into another group.