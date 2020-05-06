.. _cheatsheet:

+++++++++++++++
E213 Cheatsheet
+++++++++++++++

=======================
 Useful shell commands
=======================

+--------------+----------------+-----------------------+
|command       |Mac/Linux       |Windows                |
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


=====================
 Useful git commands
=====================

* ``git clone https://github.com/phaustin/eosc213_students.git``  (clone the course repo)
* ``git fetch``  (get new updates)
* ``git reset --hard origin/master`` (sync the new updates into your local repo -- note there are two hyphens in front of hard)

========================
Useful debugger commands
========================

To open the debugger anywhere::

  import pdb

Then put this line where you want to stop::

  pdb.set_trace()


