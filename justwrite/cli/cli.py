import click

from justwrite.generator.generator import generate_site

@click.command()
@click.option("--content", default="content", help="Directory with markdown files")
@click.option("--output", default="_site", help="Output directory for website")
@click.option("--title", default="Just Write", help="What is the title your blog")
def cli(content, output, title):
    """Just-Write a simple static site generator."""
    generate_site(content, output, title)
    click.echo(f" a site generated at {output}")

if __name__ == "__main__":
    cli()