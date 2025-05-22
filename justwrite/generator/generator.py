import os
import math
from datetime import datetime
import shutil
import markdown

from justwrite.user_util.user_style import get_user_static_dir, get_template_env
from .detectors import detect_style_files, detect_script_files

def generate_site(content_dir, output_dir, user_title):
    static_dir = get_user_static_dir()
    env = get_template_env()
    template = env.get_template("template.html")

    make_output_dir(output_dir, static_dir)

    raw_posts = list_posts(content_dir)
    html_files = []

    for i, (post_file, title_part, date) in enumerate(raw_posts):
        with open(os.path.join(content_dir, post_file), "r", encoding="utf-8") as f:
            md_content = f.read()

        html_content = markdown.markdown(md_content)
        slug = os.path.splitext(post_file)[0]
        output_file = get_slug(post_file)

        prev_post = raw_posts[i - 1] if i > 0 else None
        next_post = raw_posts[i + 1] if i < len(raw_posts) - 1 else None

        styles = detect_style_files(static_dir=static_dir)
        scripts = detect_script_files(static_dir=static_dir)

        rendered = template.render(
            title=title_part.replace('-', ' ').title(),
            stylesheets=styles,
            content=html_content,
            date=date.strftime("%B %d, %Y") if date else "Unknown Date",
            scripts=scripts,
            home_link="index.html",
            prev_link=get_slug(prev_post[0]) if prev_post else None,
            next_link=get_slug(next_post[0]) if next_post else None,
        )

        with open(os.path.join(output_dir, output_file), "w", encoding="utf-8") as f:
            f.write(rendered)

        html_files.append((title_part, output_file, date))

    generate_index_html(html_files, env, output_dir, user_title)

def generate_index_html(files, env, output_dir, user_title, posts_per_page=5):
    total_pages = math.ceil(len(files) / posts_per_page)
    static_dir = get_user_static_dir()
    styles = detect_style_files(static_dir=static_dir)
    scripts = detect_script_files(static_dir=static_dir)

    for page in range(total_pages):
        template = env.get_template("template.html")
        start = page * posts_per_page
        end = start + posts_per_page
        current_files = files[start:end]

        index_html = f"<h1>{user_title}</h1>\n\t<ul>"
        for title, file, date in current_files:
            formatted_date = date.strftime("%B %d, %Y") if date else "Unknown Date"
            index_html += f'\n\t<li>\n\t<a href="{file}">{title.replace("-", " ").title()}</a> <span class="date">{formatted_date}</span>\n\t</li>\n'

        index_html += "\t</ul>"

        # Build numbered pagination
        pagination = '\n\t\t\t<div class="pagination">'
        if page > 0:
            prev_page = "index.html" if page == 1 else f"page{page}.html"
            pagination += f'<a href="{prev_page}" class="page-link">⟵ Previous</a> '
        
        for p in range(total_pages):
            link = "index.html" if p == 0 else f"page{p + 1}.html"
            active_class = "active" if p == page else ""
            pagination += f'<a href="{link}" class="page-number {active_class}">{p + 1}</a> '

        if page < total_pages - 1:
            next_page = f"page{page + 2}.html"
            pagination += f'<a href="{next_page}" class="page-link">Next ⟶</a>'
        pagination += "</div>"

        index_html += pagination

        rendered = template.render(
            title=f"{user_title}",
            content=index_html,
            stylesheets=styles,  
            scripts=scripts,
            home_link="index.html",
            prev_link=None,
            next_link=None,
        )

        output_file = "index.html" if page == 0 else f"page{page + 1}.html"
        with open(os.path.join(output_dir, output_file), "w", encoding="utf-8") as f:
            f.write(rendered)

def make_output_dir(out, static):
    if os.path.exists(out):
        shutil.rmtree(out)
    os.makedirs(out)
    shutil.copytree(static, out, dirs_exist_ok=True)

def list_posts(content_dir):
    posts = []
    for f in sorted(os.listdir(content_dir)):
        if f.endswith(".md"):
            try:
                date_str, title_part = parse_filename(f)
                date = datetime.strptime(date_str, "%Y-%m-%d")
                # print(f"date string: {date_str}, date: {date}")
                posts.append((f, title_part, date))
            except ValueError:
                # fallback for old files
                posts.append((f, os.path.splitext(f)[0], None))
    return posts

def parse_filename(f):
    parts = f.split("-")
    if len(parts) < 4:
        raise ValueError(f"Filename {f} does not match expected format YYYY-MM-DD-title.md")

    date_str = "-".join(parts[:3])  # "2024-11-20"
    title_slug = "-".join(parts[3:])  # "second test.md"
    title = os.path.splitext(title_slug)[0]  # "second test"

    return  date_str, title

def get_slug(name):
    return os.path.splitext(name)[0] + ".html"
