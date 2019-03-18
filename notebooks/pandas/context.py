import site
import sys
from pathlib import Path

curr_dir = Path(__file__).parent
root_dir = curr_dir
processed_dir = root_dir / "data/processed"
raw_dir = root_dir / "data/raw"
sys.path.insert(0, root_dir)
sep = "*" * 30
site.removeduppaths()
print(
    (
        f"{sep}\ncontext imported. Front of path:\n"
        f"{sys.path[0]}\n{sys.path[1]}\n{sep}\n"
    )
)
