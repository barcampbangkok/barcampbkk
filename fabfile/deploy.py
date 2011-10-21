from fabric.api import cd, env, prefix, run, sudo
from fabric.decorators import roles, task
from fabric.operations import open_shell, require

# -----------------------------------------------------------------------------
# Deployment Tasks
# -----------------------------------------------------------------------------

# This is a quick and dirty cheat, because Chef *mostly* does a pretty good job
# of managing the deployment in a Capistrano-style manner which is a lot of
# work to re-implement with Fabric (somebody should have done it by now =]).
#
# So, it may change in the future to improve some things (easier rollbacks, for
# instance), but it works for now. If you want to know more about how Chef
# handles the deployment, see here:
#
#    http://wiki.opscode.com/display/chef/Deploy+Resource
#
@task(default=True)
def deploy():
    """Deploy the application to servers"""
    require('environment', provided_by=('production'))
    sudo('chef-client')

# Identical to deploy currently, yes, but it shouldn't be forever!
@task
def runchef():
    """Invoke a chef run on all servers for selected environment"""
    require('environment', provided_by=('production'))
    sudo('chef-client')

@task
@roles('app')
def restart():
    """Restart app servers (GUnicorn) and nginx"""
    require('environment', provided_by=('production'))
    sudo('service barcampbkk restart')
    sudo('service nginx restart')

@task
def uptime():
    """Uptime, mainly just a silly task to test connectivity"""
    require('environment', provided_by=('production'))
    run('uptime')

@task
@roles('app')
def shell():
    """Open django-admin.py shell remotely."""
    require('environment', provided_by=('production'))
    open_shell(app_env_shell() + 'django-admin.py shell')

@task
@roles('db')
def dbshell():
    """Open django-admin.py dbshell remotely."""
    require('environment', provided_by=('production'))
    open_shell(app_env_shell() + "django-admin.py dbshell")

# Migrations should be run automatically when deploying, but it isn't
# working properly currently. Until that's fixed, this task can be run
# manually after a deployment that includes migrations.
@task
@roles('db')
def migrate():
    """Run django-admin.py migrate for South migrations."""
    require('environment', provided_by=('production'))
    open_shell(app_env_shell() + "django-admin.py migrate")


# -----------------------------------------------------------------------------
# Utility Helpers
# -----------------------------------------------------------------------------
from contextlib import contextmanager

@contextmanager
def app_env():
    """Enter current release dir, activate virtualenv and set prod settings envvars"""
    with cd(env.current_release):
        # Fabric might have an environment variable context manager soon,
        # which would be sweet
        with prefix('export PYTHONPATH=/srv/barcampbkk && '
                    'export DJANGO_SETTINGS_MODULE=current.settings.production && '
                    'source %(activate)s' % env):
            yield

# Unfortunately the Fabric context managers only work for run/sudo, not
# open_shell, so this is a stand-in for the above.
def app_env_shell():
    return ("cd %(current_release)s && "
            "export PYTHONPATH=/srv/barcampbkk && "
            "export DJANGO_SETTINGS_MODULE=current.settings.production && "
            "source %(activate)s && " % env)

