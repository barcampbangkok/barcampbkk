***********************
Barcamp Bangkok Web App
***********************

Getting Started
===============

.. Note::
   If you're viewing this on GitHub, be aware that *this is currently a
   git-svn mirror only* -- do **not** clone this git repository and push
   changes to it! If you want to use git-svn, you should clone from the SVN
   repository.  Contact the web team if you need SVN access.

Pre-requisites
--------------

Follow the setup instructions on the linked pages here for Windows. See the
Linux/OS X sections below for recommended procedure if you're working on those
platforms.

- `Python`_  (2.6.5+ and 2.7 are both fine)
- Python `setuptools`_
- Python pip (after install setuptools, you should be able to do ``easy_install pip``)
- Python virtualenv (after install pip, you should be able to do ``pip install virtualenv``)

.. _Python: http://python.org/download/
.. _setuptools: http://pypi.python.org/pypi/setuptools

We assume recent Ubuntu (Lucid) or OS X Snow Leopard here. Hopefully you can
work things out on your own if you're not on these versions :-)

Mac OS X
~~~~~~~~

Snow Leopard has Python 2.6.1 pre-installed. This will probably be fine.
setuptools is also pre-installed, so you can jump right to::

    $ sudo easy_install pip
    $ sudo pip install virtualenv

Once you're working with virtualenvs you don't need to (and shouldn't) use
``sudo`` any longer for installing libraries with pip.

Ubuntu Lucid
~~~~~~~~~~~~

Just run ``sudo aptitude-install python-virtualenv`` -- this will take take of
installing Python, setuptools and pip for you as needed. You'll need to
`enable the Universe package repository`_ if you haven't already.

.. _enable the Universe package repository:
   https://help.ubuntu.com/community/Repositories/Ubuntu

Both of the above
~~~~~~~~~~~~~~~~~

virtualenvwrapper__  makes life much nicer when working with virtualenvs::

    $ sudo pip install virtualenvwrapper
    $ mkdir ~/.virtualenvs

Edit your ``~/.bashrc`` and add the following lines::

    # virtualenvs & wrapper
    export WORKON_HOME=$HOME/.virtualenvs
    export PIP_VIRTUALENV_BASE=$WORKON_HOME
    export PIP_RESPECT_VIRTUALENV=true
    export VIRTUALENV_USE_DISTRIBUTE=true
    source /usr/local/bin/virtualenvwrapper.sh

You should restart your shell for these to be set.

__ http://www.doughellmann.com/projects/virtualenvwrapper/


Working Environment
-------------------

You will create an virtual Python environment, and activate it so that you
will be working within it. This isolates packages you install from others on
the system to avoid conflicts.

Windows
~~~~~~~
::

    > virtualenv --no-site-packages barcamp_env
    > barcamp_env\Scripts\activate.bat

This creates the environment in a directory, ``barcamp_env`` (you can name it
whatever you like).

virtualenvwrapper (Linux/OS X)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

    $ mkvirtualenv --no-site-packages barcampbkk
    $ workon barcampbkk

This hides the environment tidily away in the ``$WORKON_HOME`` we set.

Install App Dependencies
------------------------

1. Install libraries required for the project:

   1. Go inside the source code folder
   2. ``pip install -r requirements/project.txt``
   3. See that all libraries are installed successfully (it should say so at
      the end), if not, you may want to open project.txt and install
      one-by-one for your machine).

2. Create the database file for development. From inside the source code folder::

    python manage.py syncdb

When it asks you to create an admin user, please create one. When it runs
successfully, it will create ``dev.db`` in your source code folder.

3. Run the server::

    python manage.py runserver

4. Check if that works by going to http://localhost:8000/

