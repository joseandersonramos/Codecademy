### Example of the `clear` property in CSS.

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


### Example of a breadcrumb navigation

Shopping > Fashion > Shoes > Flats > Brown

```css
.breadcrumb > li {
  display: inline;
}

.breadcrumb li+li::before {
  content: ">";
	padding: 10px;
}
```

The `>` symbol in `.breadcrumb > li` is known as the child combinator. It selects elements that are direct children of a specified element. So, when you see .breadcrumb > li, it means “select all li elements that are directly inside an element with the breadcrumb class,” but it does not select li elements that are further nested inside other elements.

The syntax `.breadcrumb li+li::before` in CSS is broken down as follows:

- **`.breadcrumb`**: This targets any element with the class `breadcrumb`.
- **`li + li`**: The `+` is the adjacent sibling combinator. It selects an `li` element that directly follows another `li` element, both being children of the same parent element. This means it targets every `li` element that follows another `li` within `.breadcrumb`, but not the first `li` element.
- **`::before`**: This is a pseudo-element selector. It targets a virtual element that is considered to be the first child of the selected element. In this case, it creates a virtual element before each `li` element selected by `.breadcrumb li+li`.

So, putting it all together, `.breadcrumb li+li::before` targets a virtual element placed just before every `li` element that directly follows another `li` within a parent element with the class `breadcrumb`, except for the very first `li` in the list. This is commonly used to insert content (like a separator symbol) between list items in a navigation breadcrumb.

The content property sets the > symbol, and padding adds space around it to improve readability.

[Understand '+', '>' and '~' symbols in CSS Selector](https://techbrij.com/css-selector-adjacent-child-sibling)
