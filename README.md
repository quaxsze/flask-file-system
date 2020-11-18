[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<br />
<p align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Flask-File-System</h3>

  <p align="center">
    File storages for Flask.
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
  </p>
</p>

## Table of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Documentation](#documentation)
* [Contributing](#contributing)
* [License](#license)

## About The Project

Flask-File-System provide a simple and flexible file storage interface for Flask.
This is a independently maintained version of Flask-FS based on the 0.6.1 version of the [Original]() project, unmaintains.

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

Flask-File-System requires Python 3.4+ and Flask 0.10+.

Amazon S3 support requires Boto3.

GridFS support requires PyMongo 3+.

OpenStack Swift support requires python-swift-client.

### Installation

You can install Flask-File-System with pip:

```sh
$ pip install flask-fs
# or
$ pip install flask-fs[s3]  # For Amazon S3 backend support
$ pip install flask-fs[swift]  # For OpenStack swift backend support
$ pip install flask-fs[gridfs]  # For GridFS backend support
$ pip install flask-fs[all]  # To include all dependencies for all backends
```

## Usage

```python
    from flask import Flask
    import flask_fs as fs

    app = Flask(__name__)
    fs.init_app(app)

    images = fs.Storage('images')


    if __name__ == '__main__':
        app.run(debug=True)
```

## Documentation

The full documentation is hosted [on Read the Docs](http://flask-fs.readthedocs.org/en/latest/)

## Contributing

Flask-File-System is open-source and open to contributions.

#### Submitting issues

Issues can be submitted [here](https://github.com/noirbizarre/flask-fs/issues).

Please provide as much information as possible when submitting the issue:

- Flask-file-system version used
- Stacktrace
- Code sample to reproduce the issue
- ...

#### Submitting patches (bugfix, features, ...)

1. Fork the [Flask-File-System repository]()
2. Create a branch with an explicit name (`issue-XX` for example)
3. Work in it
4. Rebase it on the master branch from the official repository (cleanup your history by performing an interactive rebase)
5. Submit your pull-request

Some rules to follow:

* Your contribution should be documented (if needed)
* your contribution should be tested and the test suite should pass successfully
* Your code should mostly be PEP8 compatible with a 120 characters line length

You need to install some dependencies to work on Flask-File-System:

```sh
$ pip install -e .[dev]
```

An Invoke `tasks.py` is provided to simplify the common tasks:

```sh
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
```

You can launch invoke without any parameters, it will:

* start `docker` middlewares containers (ensure docker and docker-compose are installed)
* run tests
* build the documentation
* execute flake8 quality report
* build a distributable wheel

Or you can execute any task on demand.
By example, to only run tests in the current Python environment and a quality report:

```sh
$ inv test qa
```

## License

Distributed under the MIT License. See `LICENSE` for more information.

Project Link: [https://github.com/your_username/repo_name](https://github.com/your_username/repo_name)

<!-- MARKDOWN LINKS & IMAGES -->
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=flat-square
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=flat-square
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
