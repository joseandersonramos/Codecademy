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

Example: [display: inline-flex](inline-flex.html)
