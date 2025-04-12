from setuptools import setup, find_packages

setup(
    name="justwrite",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "markdown",
        "Jinja2",
        "click"
    ],
    entry_points={
        "console_scripts": [
            "justwrite=justwrite.cli:cli",
        ],
    },
    author="Spirit",
    description="A simple Markdown to static HTML generator.",
    url="https://github.com/your-username/justwrite",
    project_urls={
        "Documentation": "https://github.com/your-username/justwrite",
        "Source": "https://github.com/your-username/justwrite",
    },
    license="MIT",
)
