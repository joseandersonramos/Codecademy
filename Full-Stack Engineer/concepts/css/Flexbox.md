### What is Flexbox?

A tool that simplifies how to position elements.

Its components are: _flex containers_ and _flex items_.

A flex container is an element on a page that contains flex items. All direct child elements of a flex container are flex items.

For an element to become a flex container, its `display` property must be set to `flex`.

```css
div.container {
  display: flex;
}
```

A div with the declaration `display: flex;` will remain block level — no other elements will appear on the same line as it. However, it will change the behavior of its child elements. Child elements will not begin on new lines.
