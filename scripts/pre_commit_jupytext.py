"""
this script is used by
https://github.com/pre-commit/pre-commit
to convert notebooks to python/*py files and add them
to the index pre-commit
"""
import sys
import jupytext
import subprocess
from pathlib import Path

nbfile = Path(sys.argv[1])
pyfile = nbfile.with_suffix(".py")
nb = jupytext.readf(nbfile)
pydir = pyfile.parent / Path("python")
pydir.mkdir(parents=True, exist_ok=True)
pypath = pydir / pyfile.name
jupytext.writef(nb, pypath, format="percent")
cmd = f"git add {str(pypath)}"
status1, output1 = subprocess.getstatusoutput(cmd)
with open("jupytext_logfile.txt", "w") as f:
    f.write(
        f"""
         notebook: {sys.argv[1]}
         writing out to {pypath}
        """
    )
sys.exit(0)
