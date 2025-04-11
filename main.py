import markdown
from jinja2 import Environment, FileSystemLoader
n = "test.html"
p = "test.md"


def md_to_html(md_file, html_name):
    """Convert a Markdown file and return a HTML"""
    # Load the markdown file
    with open(md_file, "r", encoding="utf-8") as input_file:
        text = input_file.read()
    # Turn into HTML
    html_contents = markdown.markdown(text)

    # Set-up jinja enviroment
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template("template.html")

    # Render the final html
    rendered_html = template.render(
        title="test.html",
        stylesheet="styles/style.css", # Link the styles
        content=html_contents
    )
    
    # Save to html file
    with open(html_name, "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
        output_file.write(rendered_html)

if __name__ == "__main__":

    md_to_html(p, n)