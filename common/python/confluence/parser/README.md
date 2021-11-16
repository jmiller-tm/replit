Confluence Markdown parser
==========================

To convert a Markdown document to a Confluence page, we use the [Python
Markdown library][1], with built-in and custom extensions. This document lists
the Markdown syntax that is supported by the parser, and proven to translate
well in Confluence.

If a feature you are looking for is not listed here, please consider
contributing to the development of the parser!

[1]: https://python-markdown.github.io/


Headers
-------

Page headers are defined by prefixing a string with one or more `#` symbols,
the number of which determine the heading level. For example, one `#` creates
an `<h1>`, two creates `<h2>`, etc.

**Input**

```
# This is an H1 header.

## This is an H2 header.
```

**Output**

# This is an H1 header.

## This is an H2 header.

---

The H1 and H2 headers in particular have an alternative syntax, by underlining
the string with `=` and `-` respectively. The underline does not need to be the
same length as the string, but it is useful to do so to improve readability.

**Input**

```
This is an H1 header
====================

This is an H2 header
--------------------
```

**Output**

This is an H1 header
====================

This is an H2 header
--------------------

---

When parsing a markdown document, **the first H1 is removed and used as the
Confluence page title; therefore there must always be at least one H1 in a
given markdown document**.

Lists
-----

Unordered lists can be defined using either the `-` or `*` symbols as a prefix
to each item; mixing and matching them is fine. Indenting an item below another
will also cause it to be indented within the list.

**Input**

```
  * Item One
      * Sub-item One
  - Item Two
      - Sub-item Two
```

**Output**

  * Item One
      * Sub-item One
  - Item Two
      - Sub-item Two

---

Ordered lists are defined by prefixing each item with a number and `.`; the
specific number does not matter, it will always start at, and increment by,
one.

**Input**

```
 1. Item One
 2. Item Two
 4. Item Three
```

**Output**

 1. Item One
 2. Item Two
 4. Item Three


Hyperlinks
----------

Hyperlinks can be created by enclosing the desired text within `[` and `]`. The
associated link can then follow immediately after, enclosed within `(` and `)`.

**Input**

```
This text contains a [link](https://shorturl.at/nsQTV).
```

**Output**

This text contains a [link](https://shorturl.at/nsQTV).

---

Alternatively, the link text can be followed by a bracketed-number, such as
`[1]`, with the link defined further in document. This is a good way of keeping
the source markdown tidy and easy to read.

**Input**

```
This text contains a [link][2].

[2]: https://shorturl.at/nsQTV
```

**Output**

This text contains a [link][2].

[2]: https://shorturl.at/nsQTV


Tables
------

Simple tables can be defined by delimiting columns with `|` and underlining
the header row with `-`.

**Input**

```
| First Header | Second Header |
| ------------ | ------------- |
| Content Cell | Content Cell  |
| Content Cell | Content Cell  |
```

**Output**

| First Header | Second Header |
| ------------ | ------------- |
| Content Cell | Content Cell  |
| Content Cell | Content Cell  |


Code
----

Inline code is defined by encasing the string within "`".

**Input**

```
This text contains `inline code`.
```

**Output**

This text contains `inline code`.

---

Fenced code is by surrounding the code with triple-"`" or "~" on the lines
above and below the code block.

**Input**

````
```
This text is within fenced code.
```

~~~
This text is also within fenced code.
~~~
````

**Output**

```
This text is within fenced code.
```

~~~
This text is also within fenced code.
~~~
