# stringcontext
Simple Python library functions for getting the context around an index location in a string.

This library was designed to handle retrieving a given amount of context around, before, or after
an index location in a string.

 - `context_after`: returns the string of `n` characters after the given index, or until the end of the string.
 - `context_before`: returns the string of `n` characters before the given index, or until the beginning of the string.
 - `context`: returns the full string of the context before, after, and including the character at index.

The code handles out of range issues on both ends of the string.

Based on the grep program's `-C` option switch

#### Usage
```python
import stringcontext

string = "Hello World test"
index = 5 # the space char

c = stringcontext.context(string, index, 5)
# "Hello World"
```
