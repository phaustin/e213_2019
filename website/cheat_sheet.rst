.. _cheatsheet:

+++++++++++++++++
 A301 Cheatsheet
+++++++++++++++++

=======================
 Useful shell commands
=======================

+--------------+----------------+-----------------------+
|command       |Mac             |Windows                |
+--------------+----------------+-----------------------+
| create a     |mkdir dirname   |mkdir dirname          |
| directory    |                |                       |  
+--------------+----------------+-----------------------+
| change to a  |cd dirname      |cd dirname             |
|  directory   |                |                       |
+--------------+----------------+-----------------------+
|list contents |ls *            |dir                    |
|of a directory|                |                       |
|              |                |                       |
+--------------+----------------+-----------------------+
|current folder|. (i.e. period) |. (i.e. period)        |
|              |                |                       |
|              |                |                       |
+--------------+----------------+-----------------------+
|cd up one     |cd ..           |cd ..                  |
|folder        |                |                       |
|              |                |                       |
+--------------+----------------+-----------------------+
|launch a      |jupyter notebook|jupyter notebook       |
|notebook      |                |                       |
|              |                |                       |
+--------------+----------------+-----------------------+


==============================
 Useful conda and pip commands
==============================

* conda install -c conda-forge pyhdf  (install pyhdf from the conda-forge channel)
* conda list   (list all installed packages)
* pip install -e . --upgrade (do an editable install of a git repository, upgrading if necessary)

=====================
 Useful git commands
=====================

* git clone https://github.com/phaustin/a301_code.git  (clone the course repo)
* git fetch  (get new updates)
* git reset --hard origin/master (sync the new updates into your local repo)

========================
Useful debugger commands
========================

To open the debugger anywhere::

  import pdb

Then put this line where you want to stop::

  pdb.set_trace()

=================
Folders and files
=================

+-----------------------+-----+
|                       |     |
|                       |     |
+-----------------------+-----+
|                       |     |
+-----------------------+-----+
|                       |     |
+-----------------------+-----+



======================
 Useful pyhdf commands
======================
  
* `List all datasets <https://github.com/phaustin/a301_code/blob/38c895e98e429410f3e07f66d26dc30829ae2287/notebooks/python/modis_level1b_read.py#L138>`_

* `Select one dataset <https://github.com/phaustin/a301_code/blob/38c895e98e429410f3e07f66d26dc30829ae2287/notebooks/python/modis_level1b_read.py#L149>`_

* `Print all attributes <https://github.com/phaustin/a301_code/blob/38c895e98e429410f3e07f66d2futurize -1 -w -n planck.py6dc30829ae2287/notebooks/python/modis_level1b_read.py#L178>`_

* `Get all data as a numpy array <https://github.com/phaustin/a301_code/blob/38c895e98e429410f3e07f66d26dc30829ae2287/notebooks/python/modis_level1b_read.py#L214>`_

* `Get one channel of a Modis Level1b image <https://github.com/phaustin/a301_code/blob/38c895e98e429410f3e07f66d26dc30829ae2287/notebooks/python/modis_level1b_read.py#L239>`_

  
=================
Modis information
=================

* `Modis channel listing <https://modis.gsfc.nasa.gov/about/specifications.php>`_

==============
A301 utilities
==============
  
* see `hdf4ls, killprocs modisheader,  pytree, a301version <https://clouds.eos.ubc.ca/~phil/courses/atsc301/codedoc/codedoc.html>`_

