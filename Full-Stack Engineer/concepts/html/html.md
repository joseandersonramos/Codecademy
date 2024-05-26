# HTML

## HTML Elements

### Attributes

*Attributes* are name-value pairs used to provide additional information about elements. They are placed in the opening tag of the elements.

```HTML
<div id="intro">
    <h1>Introduction</h1>
</div>
```

### `<span></span>`

`<span>` contains short pieces of text or other HTML. They are used to separate small pieces of content that are on the same line as other content.

```HTML
<p>
    <span>Self-driving cars</span> are anticipated to 
    replace up to 2 million jobs over the next two decades.
</p>
```

### Styling Text

The `<em>` tag emphasizes text, while the `<strong>` tag highlights important text.

```HTML
<p>
    <strong>The Nile River</strong> is the <em>longest</em> river in the world, 
    measuring over 6,850 kilometers long (approximately 4,260 miles).
</p>
```

“The Nile River” is **bolded** and “longest” is in _italics_.

## HTML Structures

### `<!DOCTYPE html>`

Declaration that tells the browser the type of document to expect and the version of HTML. In this case HTML5.

### `<html></html>`

This tag is used to define the root element of an HTML document. It represents the entire HTML document and contains all other HTML elements.

### `<head></head>`

The `<head>` element contains the metadata for a web page. Metadata is information about the page that isn’t displayed directly on the web page like the tab title. It goes above the `<body>` element.

### Opening links in a new tab

For a link to open in a new tab, the `target` attribute requires a value of `_blank`.

```html
<a href="https://en.wikipedia.org/wiki/Brown_bear" target="_blank">The Brown Bear</a>
```

### Linking to relative page

A relative path is a path to another file relative to the current working directory.

If index.html and contact.html are in the same directory, from index.html can be created a link to about.html like so:

```html
<a href="./contact.html">Contact</a>
```

The `./` in `./index.html` tells the browser to look for the file in the current folder.

###  Turn any element into a link by wrapping the html element with an anchor element.

```html
<a href="https://en.wikipedia.org/wiki/Brown_bear" target="_blank">
    <img src="https://content.codecademy.com/courses/web-101/web101-image_brownbear.jpg" alt="A Brown bear"/>
</a>
```

### Linking to same page

1. First, assign an id to the section of the page you want to link to. For example:
    ```html
    <div id="section1">Content of Section 1</div>
    ```
2. Next, create a link pointing to that id by using the # symbol followed by the id value:
    ```html
    <a href="#section1">Go to Section 1</a>
    ```
### Comments

```html
<!-- This is a comment that the browser will not display. -->
```

### `<th>` scope attribute

The scope attribute specifies whether a header cell is a header for a column, row, or group of columns or rows.

>Note: The scope attribute has no visual effect in ordinary web browsers, but can be used by screen readers.

```html
<table>
  <tr>
    <th></th>
    <th scope="col">Month</th>
    <th scope="col">Savings</th>
  </tr>
  <tr>
    <td>1</td>
    <td>January</td>
    <td>$100</td>
  </tr>
</table>
```

### `<td>` colspan attribute

Allows table data to occupy more than one column. It accepts an integer greater than or equal to 1.

```html
<table>
  <tr>
    <th>Monday</th>
    <th>Tuesday</th>
    <th>Wednesday</th>
  </tr>
  <tr>
    <td colspan="2">Out of Town</td>
    <td>Back in Town</td>
  </tr>
</table>
```

