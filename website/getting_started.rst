.. include:: refs.txt

.. _start:
             
Getting started
===============

We are going to be writing our own programs, which means we need some way to run code that takes in data and produces some kind of output.  To keep things simple, most of our code will be run as text files from a command line.   Being able to create, rename, delete and change files from the command line is the first skill to master.


Installing python
~~~~~~~~~~~~~~~~~

-  All the code used in the tutorial can be run on a Windows, Mac, or
   Linux laptop

-  We will use a python distribution called
   `Anaconda <https://www.anaconda.com/distribution/>`__ to run a series
   of `Jupyter notebooks <http://jupyter.org/>`__ (you are reading a
   jupyter notebook now).

-  You’re definitely encouraged to bring your laptop to the tutorial,
   please do the following:

   -  Download and install Miniconda 3.6 from
      https://conda.io/miniconda.html on your laptop, accepting all the
      defaults for the install (I specified an install into a folder
      named ma36 below):

   -  If you are running on Windows:

      -  Press the ⊞ Win key to open a cmd shell and type: anaconda
         prompt

         This should launch a cmd shell that we can use to install other
         packages

         To test your installation, type

         ::

              conda list

         at the prompt, which should show you a list of installed
         packages starting with:

         ::

              (base) C:\Users\paust>conda list
              # packages in environment at C:\Users\paust\ma36:  

   -  If you are running MacOS or Linux, after the install launch a
         bash terminal. Hopefully when you type:

      ::

              conda list

       you will see output that looks like:

      ::

              % conda list
              # packages in environment at /Users/phil/mb36:
              #
              # Name                    Version                   Build  Channel

Installing extra dependencies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  To install the software required to run the notebooks:

   1. Download
      `install_file.txt <https://gist.githubusercontent.com/phaustin/01818235ca937dc889aa3ddfeae62c5a/raw/77d4fc6491e37765b62b2c12831fdd8861017c93/install_file.txt>`_
      by right-clicking and choosing "save as"  to save it as a txt file.

   2. From your cmd or bash terminal, cd to the folder containing install_file.txt
      and do (note that "--file" has two minus signs):

      ::

          conda install --file install_file.txt

   3. If this succeeds, then typing the command:

      ::

           python -c 'import numpy;print(numpy.__version__)'

      should print:

      ::

           1.14.2

      (or possibly a higher version)

   4. If you have trouble with these steps, send me a bug report at
      paustin@eos.ubc.ca and we can iterate.
