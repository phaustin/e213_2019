"""
http://docs.python-guide.org/en/latest/writing/structure
"""
import site
import sys
from pathlib import Path

curr_dir = Path(__file__).parent
root_dir = curr_dir.parents[1]
notebook_dir = root_dir / Path("notebooks")
website_dir = root_dir / Path("website")
json_path = website_dir / Path("notebooks.json")

# can_path = Path(os.environ['HOME']) / Path('repos/canvas_scripting')
# sys.path.insert(0, can_path)
sep = "*" * 30
print(f"{sep}\ncontext imported. Front of path:\n{sys.path[0]}\n{sys.path[1]}\n{sep}\n")
site.removeduppaths()
