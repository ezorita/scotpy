# scot.py - Smart Coding Template for Python

## Setting up the project

First, make sure you are running `python` from your system install (not a virtualenv!). Use `which python` to figure out where the python binary resides.

Install `poetry`:

```
pip3 install poetry virtualenv
```

Then install the dependencies:

```
poetry install
```

In general we prefer to use `virtualenvs.in-project=false` setting, to avoid collission between docker and local venvs. This setting can be changed in `poetry.toml`.
Running the install command will create a virtual environment inside `~/.cache/pypoetry/virtualenvs/`. If you use `virtualenvs.in-project=true`, the virtual environment will be created in a `.venv/` directory in this repo, make sure you don't include it in any commit!

## Running commands

Use `poethepoet` to run commands defined in `pyproject.toml`:

```
poetry run poe format
poetry run poe lint
poetry run poe test
...
```

## Add dependencies

To add dependencies to your project, you can use the add command followed by the package name and version. For example, to add the requests package as a dependency, run the following command:

```
poetry add requests
```

Poetry will automatically resolve the dependency, update the `pyproject.toml` file, and install the package in your project's virtual environment.

You can also specify version constraints when adding dependencies. For example:

```
poetry add "requests>=2.0.0,<3.0.0"
```

or equivalently:

```
poetry add "requests@^2.0.0"
```

This adds a version constraint to ensure that the installed package is within the specified range.
