# Markdown MacTutor

This plugin adds support for the custom markdown syntax used by the MacTutor
website.

## Current syntax

The syntax added is as below:

- **m_link** - support for `[m]` biography links
- **gl_link** - support for `[gl]` glossary links
- **math_inline** - support for inline MathJax using `$math$`
- **text_inline** - modification of the regular expression for matching against
text to allow for MathJax

## Adding additional syntax

Adding additional syntax for new commands is easy, simply create a new file in
the `commands` directory and import and add it to the `plugins` list in
`lektor_markdown_mactutor.py`. The new file added must have the following global
variables:

- **name** - the name of the new syntax, must be unique
- **type** - either `inline` or `block`
- **position** - the numerical position of the command, 0 is run first
- **regex** - the compiled regular expression to find this new syntax
- **render(match)** - function that takes in the match and returns the rendered
result

## Enabling the plugin

To install/enable the plugin, run the command:

``lektor plugins add markdown-mactutor``
