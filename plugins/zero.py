from rich.console import Console
from rich.markdown import Markdown

def sub_zero():
  console = Console()
  with open("zero.md", "r") as file:
    md_content = file.read()
  markdown = Markdown(md_content)
  console.print(markdown)


