# ✍️ Just Write

**Just Write** is a simple, no-fuss static site generator that turns your Markdown files into clean, navigable HTML posts — ready to publish anywhere.

Perfect for blogging, journaling, publishing essays, or building a minimal knowledge base.

{{ This is still work in progress}}

---

## 🚀 Features

- 📄 Converts Markdown `.md` files into styled `.html` pages
- 🔗 Auto-generates navigation (Home, Previous, Next)
- 🎨 Includes support for custom CSS and JS
- 🗂️ Output can be deployed to any static web host (Netlify, GitHub Pages, etc.)
- 💻 Simple CLI tool — just run and go!

---

## 📦 Installation

1. Clone this repo

```bash
git clone https://github.com/your-username/justwrite.git
cd justwrite
```
2. Create a virtual env

```bash
python -m venv .venv 
```

3. Install dependencies
```
pip install requirements.txt
```

4. run 
```bash
python main.py
```

## 🛠️ Usage
By default, it looks for .md files in the content/ folder and generates HTML files into site/.

You can also specify folders:
```bash
python main.py --content=path/to/your/posts --output=path/to/output/site --title=yourtitle
```

Also you can put your own styles in a path  `static/styles` so that will be used instead of the default.

For javascript files you can do the same but in this path `static/scripts`

You also need to make a directory named templates and puth a `html` file named `tamplate.html`
`templates/template.html`

Markdown post should have this format 
- `2024-10-01-my-first-post.md`
- `2024-11-20-second-post.md`

## 🌐 Deploying Your Site
The site/ folder is self-contained. You can upload it to:

- Netlify

- GitHub Pages

- Any static file server