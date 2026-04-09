"""Compile bookmarks from YAML data into HTML templates.

This module loads bookmark data from a YAML file, processes it to add favicon URLs,
and renders HTML templates using Jinja2 to generate static bookmark pages.
"""

import pathlib
from urllib.parse import urlparse

import yaml
from jinja2 import Environment, FileSystemLoader, TemplateError
from rich import print as rprint
from rich.pretty import pprint

# Define file paths
PROJECT_ROOT = pathlib.Path(__file__).parent.resolve()
BOOKMARKS_YAML_FILE_PATH = PROJECT_ROOT / "bookmarks.yaml"
TEMPLATE_ROOT = PROJECT_ROOT / "templates"
OUTPUT_ROOT = PROJECT_ROOT / "output"

# https://stackoverflow.com/a/1774043/5337349
rprint(f"Loading [yellow]{BOOKMARKS_YAML_FILE_PATH}[/yellow]")
with BOOKMARKS_YAML_FILE_PATH.open("r") as bookmarks_yaml_stream:
    file_contents = yaml.safe_load(bookmarks_yaml_stream)
    for group in file_contents["bookmarks"]:
        for bookmark in group["links"]:
            favicon_domain = bookmark.get(
                "favicon_domain",
                urlparse(bookmark["url"]).netloc,
            )
            bookmark["g_favicon_url"] = (
                f"https://www.google.com/s2/favicons?domain={favicon_domain}"
            )
            if not bookmark.get("favicon_url"):
                bookmark["favicon_url"] = bookmark["g_favicon_url"]
    pprint(file_contents)

    # Load all template files
    env = Environment(loader=FileSystemLoader(str(TEMPLATE_ROOT)), autoescape=True)
    for template_file_path in TEMPLATE_ROOT.glob("*.html"):
        template_filename = template_file_path.name
        try:
            rprint(f"Processing [yellow]{template_filename}[/yellow]")
            template = env.get_template(template_filename)
            output = template.render(data=file_contents)
            output_file_path = OUTPUT_ROOT / template_filename
            with output_file_path.open("w", newline="") as f:
                f.write(output)
        except (OSError, TemplateError) as exc:
            rprint(f"[red]Error processing {template_filename}: {exc}[/red]")
