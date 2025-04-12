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
python main.py --content path/to/your/posts --output path/to/output/site
```

## 🌐 Deploying Your Site
The site/ folder is self-contained. You can upload it to:

- Netlify

- GitHub Pages

- Any static file server