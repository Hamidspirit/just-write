import os 
from jinja2 import Environment, FileSystemLoader

def get_user_static_dir():
    # Look in current working directory first (i.e. project root)
    user_static_dir = os.path.join(os.getcwd(), "static")

    # Fallback: go one level up from user_util/
    fallback_static_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")

    if os.path.isdir(user_static_dir):
        print(f"✅ Using static files from: {user_static_dir}")
        return user_static_dir
    elif os.path.isdir(fallback_static_dir):
        print(f"⚠️  Static not found in user dir. Using fallback: {fallback_static_dir}")
        return fallback_static_dir
    else:
        raise FileNotFoundError("❌ No static directory found in expected locations.")


def get_template_env():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    root_dir = os.path.abspath(os.path.join(base_dir, '..', '..'))  # <- project root

    # Check for user-defined template directory
    user_template_dir = os.path.join(root_dir, 'templates')
    default_template_dir = os.path.join(base_dir, 'templates')  # your built-in

    template_path = os.path.join(user_template_dir, 'template.html')
    if not os.path.isfile(template_path):
        print("⚠️  template.html not found in user template folder. Using default.")

    if os.path.isdir(user_template_dir):
        print(f"✅ Using user templates from: {user_template_dir}")
        loader = FileSystemLoader(user_template_dir)
    else:
        print(f"⚠️  No user templates found, using default: {default_template_dir}")
        loader = FileSystemLoader(default_template_dir)

    return Environment(loader=loader)