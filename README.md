## fastapi-html

Sample repository demonstrating how to use `FastAPI` to serve HTML web apps. 

>2-min blog post [here](https://eugeneyan.com/writing/how-to-set-up-html-app-with-fastapi-jinja-forms-templates/).

## Quickstart

```
# Clone this repo
git clone https://github.com/eugeneyan/fastapi-html.git

# Install the required dependencies
cd fastapi-html
poetry install

# Start the HTML app
poetry run uvicorn src.html:app --reload
```

Navigate to [127.0.0.1:8000/form](http://127.0.0.1:8000/form).

Viola!

![fastapi-html](https://raw.githubusercontent.com/eugeneyan/fastapi-html/master/fastapi-html-web-app.jpg)

