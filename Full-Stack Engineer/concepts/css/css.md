# Example of the `clear` property in CSS.

Imagine you have a set of floating `<div>` elements and a `<div>` element that you want to appear below them, regardless of how the previous ones float. This is where the `clear` property becomes useful.

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        .floating {
            float: left;
            width: 100px;
            height: 100px;
            margin: 10px;
            background-color: #ffcc00;
        }

        .clear-div {
            clear: left;
            background-color: #99ccff;
            padding: 10px;
        }
    </style>
</head>
<body>

<div class="floating">Floating 1</div>
<div class="floating">Floating 2</div>
<div class="floating" style="height: 150px;">Floating 3 (taller)</div>
<div class="floating">Floating 4</div>
<!-- This div will use clear to avoid floating alongside the previous elements -->
<div class="clear-div">I do not float next to the previous floaters.</div>

</body>
</html>
```

In this example:

- The elements with the class `.floating` are set to float to the left (`float: left;`). This means they will line up side by side from left to right, depending on the available space.
- The element with the class `.clear-div` has the `clear: left;` property. This causes the element to position itself below any previous floating elements on the left side, preventing it from being placed alongside the floating elements, regardless of their height or arrangement.

The `clear` property is especially useful in layouts where you need to ensure that certain elements are displayed below others, instead of beside them, which can be crucial for maintaining structure and readability.