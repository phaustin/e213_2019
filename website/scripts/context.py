"""
this module defines useful variables and adds packages if needed
paths are all constructored by moving up or down relative to the
path to this file, which is store din __file__

see
http://docs.python-guide.org/en/latest/writing/structure
"""
import site
import sys
from pathlib import Path


curr_dir = Path(__file__).parent
# /Users/phil/repos/eosc213/website/scripts
root_dir = curr_dir.parents[1]
# /Users/phil/repos/eosc213
notebook_dir = root_dir / Path("notebooks")
# /Users/phil/repos/eosc213/website/notebooks
website_dir = root_dir / Path("website")
# /Users/phil/repos/eosc213/website
json_path = website_dir / Path("notebooks.json")
# /Users/phil/repos/eosc213/website/notebooks.json
home_dir = Path.home()
# /Users/phil
assign_dir = home_dir / Path("Nextcloud/213/graded_assignments")
# /Users/phil/Nextcloud/213/graded_assignments
assign_source = home_dir / assign_dir / Path("source")
# /Users/phil/Nextcloud/213/graded_assignments/source
assign_release = home_dir / assign_dir / Path("release")
# /Users/phil/Nextcloud/213/graded_assignments/source
student_dir = root_dir.parent / Path("eosc213_students")
# /Users/phil/repos/eosc213_students
sep = "*" * 30
print(f"{sep}\ncontext imported. Front of path:\n{sys.path[0]}\n{sys.path[1]}\n{sep}\n")
site.removeduppaths()
