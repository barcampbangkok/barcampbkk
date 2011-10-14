import subprocess
import sys

from os import environ, path

from fabric.api import env, lcd, local
from fabric.colors import red
from fabric.decorators import task

# This ought to be namespaced, but Fabric's loading seems to interfere with
# being able to append the dir containing the fabfile to sys.path here :-/
import settings as app

# Task submodules
import deploy

# -----------------------------------------------------------------------------
# Environments
# -----------------------------------------------------------------------------
@task(alias='prod')
def production():
    """Use production environment"""
    env.hosts = ['2011.barcampbangkok.org']
    env.user = 'barcamp'
    env.environment = 'production'
    env.deploy_to = '/srv/barcampbkk'
    env.current_release = path.join(env.deploy_to, 'current')
    env.virtualenv = path.join(env.deploy_to, 'shared', 'env')
    env.activate = path.join(env.virtualenv, 'bin', 'activate')

    env.roledefs.update({
        'app': ['2011.barcampbangkok.org'],
        'web': ['2011.barcampbangkok.org'],
        'db': ['2011.barcampbangkok.org']
    })


# -----------------------------------------------------------------------------
# Dev Tasks
# -----------------------------------------------------------------------------
@task(default=True)
def test():
    """Simple convenience for `manage.py test`"""
    with lcd(app.PROJECT_ROOT):
        local('python manage.py test')

@task
def startdev():
    """Sets up packages and initial DB for development on a new machine."""
    if 'VIRTUAL_ENV' not in environ:
        print(red('No active VIRTUAL_ENV found -- you should create and activate one!'))
        sys.exit(-1)

    with lcd(app.PROJECT_ROOT):
        subprocess.call(['python', 'manage.py', 'syncb', '--all'])
        subprocess.call(['python', 'manage.py', 'migrate', '--fake'])
        subprocess.call(['python', 'manage.py', 'loaddata', 'fixtures/dev/*'])


