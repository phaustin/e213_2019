import json
from pathlib import Path

import context
import nbformat

with open(context.json_path, "r") as json_file:
    notebook_order = json.load(json_file)

for week, notebook_list in notebook_order.items():
    for notebook in notebook_list:
        nb_name = f"{notebook}.ipynb"
        nb_file = list(context.notebook_dir.glob(f"**/{nb_name}"))[0]
        with open(nb_file, "r") as f:
            nb = nbformat.read(f, as_version=nbformat.NO_CONVERT)
nbsphinx = nbformat.from_dict({"execute": "never"})
nb["metadata"]["nbsphinx"] = nbsphinx
outfile = context.notebook_dir / Path("trythis.ipynb")
with open(outfile, "w") as f:
    nbformat.write(nb, f, version=nbformat.NO_CONVERT)
