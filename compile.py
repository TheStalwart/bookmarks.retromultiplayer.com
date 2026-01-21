import glob
from operator import itemgetter
import os
import pathlib
import yaml
from rich import print
from rich.pretty import pprint
from jinja2 import Environment, FileSystemLoader

# Define file paths
PROJECT_ROOT = pathlib.Path(__file__).parent.resolve()
BOOKMARKS_YAML_FILE_PATH = os.path.join(PROJECT_ROOT, "bookmarks.yaml")
TEMPLATE_ROOT = os.path.join(PROJECT_ROOT, "templates")
OUTPUT_ROOT = os.path.join(PROJECT_ROOT, "output")

# https://stackoverflow.com/a/1774043/5337349
print(f'Loading [yellow]{BOOKMARKS_YAML_FILE_PATH}[/yellow]')
with open(os.path.join(PROJECT_ROOT, BOOKMARKS_YAML_FILE_PATH)) as bookmarks_yaml_stream:
    file_contents = yaml.safe_load(bookmarks_yaml_stream)
    pprint(file_contents)

    # Load all template files
    env = Environment(loader=FileSystemLoader(TEMPLATE_ROOT))
    for template_file_path in glob.glob(os.path.join(TEMPLATE_ROOT, '*.html')):
        template_filename = os.path.basename(template_file_path)
        try:
            print(f'Processing [yellow]{template_filename}[/yellow]')
            template = env.get_template(template_filename)
            output = template.render(data=file_contents)
            output_file_path = os.path.join(OUTPUT_ROOT, template_filename)
            with open(output_file_path, 'w', newline='') as f:
                f.write(output)
        except Exception as exc:
            print(f'[red]Error processing {template_filename}: {exc}[/red]')
