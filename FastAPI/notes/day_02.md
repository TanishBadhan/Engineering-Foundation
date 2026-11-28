
# Day 02 — HTML Templates and Static Files

## Objective

Understand how FastAPI serves dynamic HTML pages using Jinja2
templates and how static files such as CSS, JavaScript, and
images are served by the application.

## Concepts Covered

### 1. Jinja2 Templates

Jinja2 is a template engine used to generate dynamic HTML
pages by combining HTML with data passed from Python.

FastAPI supports Jinja2 through `Jinja2Templates`.

```python
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
```

The `directory` parameter specifies where the HTML template
files are stored.

### 2. Template Responses

`TemplateResponse` is used to render an HTML template and
return it as an HTTP response.

```python
return templates.TemplateResponse(
    request,
    "home.html",
    {"posts": posts, "title": "Home"},
)
```

The context dictionary passes data from the Python
application to the HTML template.

The template can access this data using Jinja2 expressions.

```html
{{ post.title }}
{{ post.author }}
{{ post.content }}
```

### 3. Template Inheritance

Jinja2 supports template inheritance, allowing multiple
HTML pages to share a common layout.

A child template can extend a parent template:

```html
{% extends "layout.html" %}

{% block content %}
    <!-- Page content -->
{% endblock content %}
```

The parent template defines the corresponding block:

```html
{% block content %}
{% endblock content %}
```

This avoids repeating common HTML elements across pages.

### 4. Dynamic Content

Jinja2 supports loops for displaying collections of data
inside HTML templates.

```html
{% for post in posts %}
    <h2>{{ post.title }}</h2>
    <p>{{ post.content }}</p>
{% endfor %}
```

The loop iterates through the posts collection and generates
HTML for each post.

### 5. Static Files

Static files include CSS stylesheets, JavaScript files,
images, and icons.

FastAPI serves static files using `StaticFiles`.

```python
from fastapi.staticfiles import StaticFiles

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static",
)
```

The application makes the contents of the `static` directory
accessible through the `/static` URL path.

Static files can be referenced inside templates using
`url_for()`.

```html
{{ url_for('static', path='css/main.css') }}
```

The `path` parameter specifies the file location inside
the static directory.

## Implementation

The application was extended with:

- A `templates/` directory containing HTML templates.
- A `layout.html` file containing the common page structure.
- A `home.html` file extending the parent layout.
- A `static/` directory containing CSS, JavaScript, icons,
  and profile pictures.
- Dynamic rendering of posts using Jinja2.
- A navigation bar linking to the home route.
- Static asset loading through FastAPI.

## Important Limitation

The posts collection is still stored in memory.

Consequently:

- Data is not persisted in a database.
- Changes to the collection are lost when the process restarts.
- Templates handle presentation, not permanent data storage.

## Development and Debugging

The application was extended using Jinja2 templates and
static files.

An error occurred while generating static file URLs because
`url_for()` was provided with an incorrect positional argument.

Incorrect:

```html
{{ url_for('static', 'icons/favicon.ico') }}
```

Correct:

```html
{{ url_for('static', path='icons/favicon.ico') }}
```

The issue was resolved by passing the file path using
the `path` keyword argument.

The application was subsequently started and the rendered
home page was verified in the browser.

## Key Takeaways

- Jinja2 generates dynamic HTML using Python data.
- `Jinja2Templates` configures the template directory.
- `TemplateResponse` renders HTML templates.
- Template inheritance avoids repeated HTML structures.
- Jinja2 loops display collections of data dynamically.
- `StaticFiles` serves CSS, JavaScript, images, and icons.
- `url_for()` generates URLs for named routes and static files.

## Next Steps

- Continue the tutorial and extend the existing application.
- Understand how forms and user input are handled.
- Explore additional FastAPI request handling concepts.
- Continue improving the application's structure.

## Reflection

The goal is to understand how FastAPI connects Python
application logic with HTML templates and static resources.

The focus should be on understanding how data is passed
to templates, how reusable layouts work, and how static
files are made accessible to the browser.
