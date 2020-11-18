from invoke import run, task

from os.path import join, abspath, dirname

ROOT = abspath(join(dirname(__file__)))


def compose(ctx, cmd):
    """Runs a docker-compose command"""
    return ctx.run('docker-compose {0}'.format(cmd), pty=True)


@task
def clean(ctx, docs=False, bytecode=False, extra=''):
    """Cleanups all build artifacts"""
    patterns = ['build', 'dist', 'cover', 'docs/_build', '**/*.pyc', '*.egg-info', '.tox']
    for pattern in patterns:
        print('Removing {0}'.format(pattern))
        with ctx.cd(ROOT):
            ctx.run('rm -rf {0}'.format(pattern))


@task
def start(ctx):
    """Starts the middlewares (docker)"""
    with ctx.cd(ROOT):
        compose(ctx, 'up -d')
        compose(ctx, 'ps')


@task
def stop(ctx, rm=False):
    """Stops the middlewares (docker)"""
    with ctx.cd(ROOT):
        compose(ctx, 'stop')
        if rm:
            compose(ctx, 'rm --force')


@task
def test(ctx):
    """Runs tests suite"""
    with ctx.cd(ROOT):
        ctx.run('pytest', pty=True)


@task
def cover(ctx, html=False):
    """Runs tests suite with coverage"""
    params = '--cov-report term --cov-report html' if html else ''
    with ctx.cd(ROOT):
        ctx.run('pytest --cov flask_file_system {0}'.format(params), pty=True)


@task
def qa(ctx):
    """Runs a quality report"""
    with ctx.cd(ROOT):
        ctx.run('flake8 flask_file_system tests')


@task
def doc(ctx):
    """Builds the documentation"""
    with ctx.cd(ROOT):
        ctx.run('cd docs && make html', pty=True)


@task
def dist(ctx):
    """Package for distribution"""
    with ctx.cd(ROOT):
        ctx.run('python setup.py sdist bdist_wheel', pty=True)


@task(start, doc, qa, dist, default=True)
def all(ctx):
    """Runs tests, reports and packaging"""
    pass
