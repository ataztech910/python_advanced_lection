---

- структура проекта
- setup.py для инсталляции пакета

---

Organize your code based on features, not on types.

It is also a bad idea to create a module directory that contains only an __init__.py file, because it’s unnecessary nesting. For example, you shouldn’t create a directory named hooks with a single file named hooks/__init__.py
in it, where hooks.py would have been enough

---

You should also be very careful about the code that you put in the __init__.py file. This file will be called and executed the first time that a module contained in the directory is loaded. Placing the wrong things in your __init__.py can have unwanted side effects.

In fact, __init__.py files should be empty most of the time, unless you know what you’re doing. Don’t try to remove __init__.py files altogether though, or you won’t be able to import your Python module at all: Python requires an __init__.py file to be present for the directory to be considered a submodule

---

### Version Numbering

- Стандарт PEP 440
- Version 1.2 is equivalent to 1.2.0, 1.3.4 is equivalent to 1.3.4.0, and so forth.
- хорошо если разделить выпуск на 2 приложения
---

### Coding Style and Automated Checks

That was one of the first questions raised in the community, so the Python folks, in their vast wisdom, came up with the PEP 8: Style Guide for Python Code

- Use four spaces per indentation level.
- Limit all lines to a maximum of 79 characters.
- Separate top-level function and class definitions with two blank lines.
- Encode files using ASCII or UTF-8.
- Use one module import per import statement and per line. Place import statements at the top of the file, after comments and docstrings, grouped first by standard, then by third party, and finally by local library imports.
- Do not use extraneous whitespaces between parentheses, square brackets, or braces or before commas.
- Write class names in camel case (e.g., CamelCase), suffix exceptions with Error (if applicable), and name functions in lowercase with words and underscores (e.g., separated_by_underscores). Use a leading underscore for _private attributes or methods.

- https://pypi.org/project/pep8/ use this tool to check code style
- https://pypi.org/project/pylint/

---

## Жизненный цикл объекта.

## Работа с ресурсами.
https://www.geeksforgeeks.org/design-a-keylogger-in-python/

## Работа с объектом.

## Итератор и генератор.