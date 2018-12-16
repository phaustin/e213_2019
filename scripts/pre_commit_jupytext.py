# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 0.8.6
# ---

# %%
import sys
import subprocess
from pathlib import Path
import shutil


cmd = f"jupytext --to py:percent {sys.argv[1]}"
notebook = Path(sys.argv[1])
status1, output1 = subprocess.getstatusoutput(cmd)
pyfile = notebook.with_suffix(".py")
pydir = pyfile.parent / Path("python")
pydir.mkdir(parents=True, exist_ok=True)
newfile = pydir / pyfile.name
shutil.move(str(pyfile.resolve()), str(newfile.resolve()))
cmd = f"git add {newfile}"
# print(f"working with {newfile}")
status2, output2 = subprocess.getstatusoutput(cmd)
with open("jupytext_logfile.txt", "w") as f:
    f.write(
        f"""
         {sys.argv}
         {status1}
         {output1}
         {status2}
         {output2}
         writing out {newfile}
        """
    )
sys.exit(0)
