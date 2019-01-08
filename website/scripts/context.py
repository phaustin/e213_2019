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
home_dir = Path.home()
assign_dir = home_dir / Path("oNextcloud/213/graded_assignments")
assign_source = home_dir / assign_dir / Path("source")
assign_release = home_dir / assign_dir / Path("release")
student_dir = root_dir.parent / Path("eosc213_students")

# can_path = Path(os.environ['HOME']) / Path('repos/canvas_scripting')
# sys.path.insert(0, can_path)
sep = "*" * 30
print(f"{sep}\ncontext imported. Front of path:\n{sys.path[0]}\n{sys.path[1]}\n{sep}\n")
site.removeduppaths()
