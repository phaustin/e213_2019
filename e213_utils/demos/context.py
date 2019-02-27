import site
import sys
from pathlib import Path

root_dir = Path(__file__).parents[2]
demo_dir = root_dir / Path("e213_utils/demos")
sys.path.insert(0, root_dir)
print(f"root_dir is {root_dir}\n and demo_dir is {demo_dir}\n")
sep = "*" * 30
print(f"{sep}\ncontext imported. Front of path:\n{sys.path[0]}\n{sys.path[1]}\n{sep}\n")
site.removeduppaths()
