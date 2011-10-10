***********************
Barcamp Bangkok Web App
***********************

Getting Started
===============

Pre-requisites
--------------

Follow the setup instructions on the linked pages here for Windows. See the
Linux/OS X sections below for recommended procedure if you're working on those
platforms.

- `Python`_  (2.6.5+ and 2.7 are both fine)
- Python `setuptools`_
- Python pip (after install setuptools, you should be able to do ``easy_install pip``)
- Python virtualenv (after install pip, you should be able to do ``pip install virtualenv``)
- `Python Imaging Library`_ (PIL)

.. _Python: http://python.org/download/
.. _setuptools: http://pypi.python.org/pypi/setuptools
.. _Python Imaging Library: http://www.pythonware.com/products/pil/

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

In order for PIL to build when installing the rest of the app's Python package
dependencies below, you should install ``libjpeg``. If you're using Homebrew,
for instance::

    $ brew install jpeg

Ubuntu Lucid
~~~~~~~~~~~~

Just run ``sudo aptitude install python-virtualenv`` -- this will take take of
installing Python, setuptools and pip for you as needed. You'll need to
`enable the Universe package repository`_ if you haven't already.

In order for PIL to build when installing the rest of the app's Python package
dependencies below, you should install a couple of prerequisite packages::

    $ sudo aptitude install libjpeg-dev zlib1g-dev libfreetype6-dev

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

2. Create the database for development. From inside the source code folder::

    python manage.py syncdb --all
    python manage.py migrate --fake
    python manage.py loaddata fixtures/dev/*

   When it asks you to create an admin user, please create one. When it runs
   successfully, it will create ``dev.db`` in your source code folder and load
   some stub content from fixtures.

3. Symbolic link cms static files (Windows people, you will have to copy the folder over instead)

    ln -s <virtual environment site-packages folder>/cms/static/cms site_media/static/cms

4. Make sure tests are passing with your setup::

    python manage.py test

5. Run the server::

    python manage.py runserver

6. Check if that works by going to http://localhost:8000/
7. Start hackin'

Note that the Barcamp app builds on `django CMS`_, which uses the `South`_
project for database migration support, as any good modern Django project
probably should. You're advised to browse the `South tutorial`_ if you're
unfamiliar with it -- you should at least be prepared to run::

    python manage.py schemamigration appname --auto
    python manage.py migrate appname

after you make changes to models. You should also be conscious of running the
``migrate`` command when pulling in updates from SCM that contain migrations.

.. _known false failures in Pinax: https://github.com/pinax/pinax/pull/12/files
.. _django CMS: https://www.django-cms.org/
.. _South: http://south.aeracode.org/
.. _South tutorial: http://south.aeracode.org/docs/tutorial/index.html


Internationalization & Localization
===================================

Django CMS allows entering content in multiple languages -- in the CMS Pages
section of the administrative backend, you'll find that each created page has
'English' and 'Thai' tabs at the top.

For developers and tech-savvy translation volunteers, become familiar with
`Django's localization support`_ to translate text strings within the
application (not in the site CMS content). In summary, you generate updated
messages strings to be translated using::

    python manage.py makemessages -l th

if you're going to add/update Thai translations, for instance. Then edit
``locale/th/LC_MESSAGES/django.po`` to change the values (``msgstr``) for each
identifier (``msgid``) found from the application code or templates containing
the string you want to translate. When you've finished, run::

    python manage.py compilemessages

and then commit the changed files into version control.

.. note::
   You'll need to install `GNU gettext`_ in the preferred manner for your
   platform in order to use the ``messages manage.py`` commands.

.. _Django's localization support:
   https://docs.djangoproject.com/en/dev/topics/i18n/localization/
.. _GNU gettext: http://www.gnu.org/software/gettext/

Social Network Authentication
==============================

For development, you'll need to update site domain in the Sites table to the domain you're running at e.g. 127.0.0.1:8000
This will be sent to Twitter for callback.

For production, assuming we're going to deploy at barcampbangkok.org, just make sure that the site domain is barcampbangkok.org

