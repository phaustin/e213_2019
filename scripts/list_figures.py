"""
This script scans all files below the current directory, looking
for img or markdown figure tags of the

<img src="figures/2d_flux.png" alt="pic05" width="20%" >

or

![pic06](figures/2d_flux.png){width="20%"}

It creates a list of files used in the notebooks, compares it with
all the image files in the folders and creates a list of extra_figs, which
are note used in any notebook.  If dryrun is True, it prints extra_figs,
if dryrun is false, it deletes all files in extra_figs.
"""
import os
import pprint
import re
import shutil
from pathlib import Path

from bs4 import BeautifulSoup

img_re = re.compile(r".*(\<img\s+src.*\>).*")
md_re = re.compile(r"^\#\s+\!\[.*\]\((?P<filename>.*)\).*")
template = '# ![{alt:}]({src:}){{width="{width:}"}}\n'

curr_dir = Path()
file_list = curr_dir.glob("**/*py")
good_files = [
    item
    for item in file_list
    if (str(item).find(".ipynb_checkpoints") == -1 and item.is_file())
]
file_list = curr_dir.glob("**/*ipynb")
ipynb_files = [
    item
    for item in file_list
    if (str(item).find(".ipynb_checkpoints") == -1 and item.is_file())
]
good_files.extend(ipynb_files)

doc_figs = []
exclude_list = [
    "feedback",
    "zipfiles",
    "submitted",
    "autograded",
    "downloaded",
    "autograded",
    "exchange",
    "completed",
]

debug = False
for item in good_files:
    if item.parts[0] in exclude_list:
        continue
    # if item.name.find("7_finite") > -1:
    #     print(f'found: {item} -- seting debug')
    #     debug=False
    # else:
    #     debug=False
    try:
        file_content = item.read_text()
    except UnicodeDecodeError:
        print(f"unicode error for {item}")
        continue
    for the_line in file_content.split(os.linesep):
        if debug:
            print(f"{the_line}")
        md_match = md_re.match(the_line)
        if md_match:
            figname = md_match.group("filename")
            full_path = item.parent / figname
            the_fig = Path(full_path).resolve()
            doc_figs.append(the_fig)
        else:
            img_match = img_re.match(the_line)
            if img_match:
                soup = BeautifulSoup(the_line, "html.parser")
                out = soup()
                figname = out[0]["src"].replace(r"\"", "")
                full_path = item.parent / figname
                the_fig = Path(full_path).resolve()
                doc_figs.append(the_fig)

doc_figs = set(doc_figs)

fig_dirs = curr_dir.glob("**/figures*")
dir_list = [item for item in fig_dirs if item.is_dir()]
dir_figs = []
for the_dir in dir_list:
    print(f"scanning {the_dir}")
    fig_files = list(the_dir.glob("**/*"))
    fig_files = [item.resolve() for item in fig_files]
    dir_figs.extend(fig_files)

dir_figs = set(dir_figs)
extra_figs = dir_figs - doc_figs
print(f"\n\nfound {len(doc_figs)} figures in notebooks")
print(f"found {len(dir_figs)} figures in in folders")

dryrun = True
if dryrun:
    if len(extra_figs) > 0:
        print(f"\n\ngoing to delete {pprint.pformat(extra_figs)}")
        print("set dryrun=False to delete")
    else:
        print("\n\nno files to delete")
else:
    for item in extra_figs:
        print(f"\n\ndeleting {item}")
        if item.is_dir():
            shutil.rmtree(item)
        else:
            try:
                item.unlink()
            except FileNotFoundError:
                pass
