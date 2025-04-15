import click

from justwrite.generator.generator import generate_site

@click.command()
@click.option("--content", default="content", help="Directory with markdown files")
@click.option("--output", default="_site", help="Output directory for website")
def cli(content, output):
    """Just-Write a simple static site generator."""
    generate_site(content, output)
    click.echo(f" a site generated at {output}")

if __name__ == "__main__":
    cli()