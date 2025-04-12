import os
import shutil
import markdown
from jinja2 import Environment, FileSystemLoader

def generate_site(content_dir, output_dir):

    template_dir = os.path.join(os.path.dirname(__file__), "templates")
    static_dir = os.path.join(os.path.dirname(__file__), "static")

    # Set-up jinja enviroment
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("template.html")

    make_output_dir(output_dir, static_dir)

    posts = list_posts(content_dir)
    html_files = []

    for i, post_file in enumerate(posts):
        with open(os.path.join(content_dir, post_file), "r") as f:
            md_content = f.read()

        html_content = markdown.markdown(md_content)
        slug = os.path.splitext(post_file)[0]
        output_file = get_slug(post_file)

        prev_post = posts[i - 1] if i > 0 else None
        next_post = posts[i + 1] if i < len(posts) -1 else None

        rendered = template.render(
            title=slug.replace('-', ' ').title(),
            stylesheet="styles/style.css", # Link the styles
            content=html_content,
            home_link="index.html",
            prev_link=get_slug(prev_post) if prev_post else None,
            next_link=get_slug(next_post) if next_post else None,
        )

        with open(os.path.join(output_dir, output_file) ,"w", encoding="utf-8", errors="xmlcharrefreplace") as f:
            f.write(rendered)
        html_files.append((slug, output_file))
        
        # generate index file
        generate_index_html(html_files, template_dir, output_dir)

def generate_index_html(files, template_dir, output_dir):

    # Set-up jinja enviroment
    env = Environment(loader=FileSystemLoader(template_dir))
    template = env.get_template("template.html")

    index_html = "<h1>Just Write Posts</h1><ul>"
    for title, file in files:
        index_html += f'<li> <a href="{file}"> {title.replace("-", " ").title()}</a> </li>'
    index_html += "</ul>"

    rendered = template.render(
        stylesheet="styles/style.css", # Link the styles
        content=index_html,
    )

    with open(os.path.join(output_dir, "index.html"), "w", encoding="utf-8", errors="xmlcharrefreplace") as f:
        f.write(rendered)


def make_output_dir(out, static):
    # make sure output dir is clean
    if os.path.exists(out):
        shutil.rmtree(out)
    os.makedirs(out)

    # Copy static files
    shutil.copytree(static, os.path.join(out), dirs_exist_ok=True)

def list_posts(dir):
    posts = sorted([f for f in os.listdir(dir) if f.endswith(".md")])
    return posts

def get_slug(name): return os.path.splitext(name)[0] + ".html"