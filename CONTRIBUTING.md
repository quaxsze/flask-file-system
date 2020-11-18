# Contributing guide

Flask-File-System is open-source and open to contributions.

## Submitting issues

Issues can be submitted [here](https://github.com/noirbizarre/flask-fs/issues).

Please provide as much information as possible when submitting the issue:

- Flask-file-system version used
- Stacktrace
- Code sample to reproduce the issue
- ...

## Submitting patches (bugfix, features, ...)

1. Fork the [Flask-File-System repository]()
2. Create a branch with an explicit name (``issue-XX`` for example)
3. Work in it
4. Rebase it on the master branch from the official repository (cleanup your history by performing an interactive rebase)
5. Submit your pull-request

Some rules to follow:

- Your contribution should be documented (if needed)
- your contribution should be tested and the test suite should pass successfully
- Your code should mostly be PEP8 compatible with a 120 characters line length

You need to install some dependencies to work on Flask-File-System:

.. code-block:: console

    $ pip install -e .[dev]

An Invoke ``tasks.py`` is provided to simplify the common tasks:

.. code-block:: console

    $ inv -l
    Available tasks:

      all      Run tests, reports and packaging
      clean    Cleanup all build artifacts
      cover    Run tests suite with coverage
      dist     Package for distribution
      doc      Build the documentation
      qa       Run a quality report
      start    Start the middlewares (docker)
      stop     Stop the middlewares (docker)
      test     Run tests suite

You can launch invoke without any parameters, it will:

- start ``docker`` middlewares containers (ensure docker and docker-compose are installed)
- run tests
- build the documentation
- execute flake8 quality report
- build a distributable wheel

Or you can execute any task on demand.
By example, to only run tests in the current Python environment and a quality report:

.. code-block:: console

    $ inv test qa
