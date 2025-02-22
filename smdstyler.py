from rich.console import Console
from rich.markdown import Markdown

# Create a Console object
console = Console()

# Read the Markdown file
with open("README.md", "r") as file:
    md_content = file.read()

# Parse the Markdown and render it
markdown = Markdown(md_content)
console.print(markdown)
