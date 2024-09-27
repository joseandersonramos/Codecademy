### What is Flexbox?

A tool that simplifies how to position elements.

Its components are: _flex containers_ and _flex items_.

Flex containers are helpful tools for creating websites that respond to changes in screen sizes. Child elements (flex items) of flex containers will change size and location in response to the size and position of their parent container.

## display: flex

For an element to become a flex container, its `display` property must be set to `flex`.

```css
div.container {
  display: flex;
}
```

Example: [display: flex](display-flex.html)

## display: inline-flex

Allows us to create flex containers that are also inline elements.

```css
.container {
  width: 200px;
  height: 200px;
  display: inline-flex;
}
```

Example: [display: inline-flex](inline-flex.html)

## justify-content

To position the items from left to right, we use a property called `justify-content`.

Common values for `justify-content` include:

- `flex-start`: Aligns items at the start of the container.
- `flex-end`: Aligns items at the end of the container.
- `center`: Centers items in the container.
- `space-around`: Distributes items with equal space before and after each item.
- `space-between`: Distributes items with equal space between them, with no extra space at the start or end.

These values help control how items are distributed along the main axis of the flex container.

Example: [justify-content](justify-content.html)

## align-items

Align elements vertically within a container.

Common values for `align-items` are:

- `flex-start`: Aligns items at the top.
- `flex-end`: Aligns items at the bottom.
- `center`: Centers items vertically.
- `baseline`: Aligns items based on the baseline of the content.
- `stretch`: Stretches items to fill the container (default value).

These values affect the cross axis of the container.

Example: [align-items](align-items.html)

## flex-grow

Allows flex items to grow to fill the container if there is extra space. Items with a higher flex-grow value will grow
proportionally more than those with a lower value. For example, if a container has three items and there is extra space,
items with flex-grow: 2 will grow twice as much as items with flex-grow: 1.

> Note: `flex-grow` is declared on flex items.

Example: [flex-grow](flex-grow.html)

## flex-shrink

The `flex-shrink` property can be used to specify which elements will shrink and in what proportions. The default value of flex-shrink is 1.

> Note: `flex-shrink` is declared on flex items.

Example: [flex-shrink](flex-shrink.html)
