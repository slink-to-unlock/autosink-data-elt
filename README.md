# Data Extract-Load-Transform

[🇬🇧](README.md) | [🇰🇷](README.kr.md) | [🇨🇳](README.zh-CN.md)

Parse the values in the data lake and load them into memory, so that the data labeler can be executed. It puts the labeled data into the feature store. autosink-data-elt contains utility classes for reading and writing json files stored in the data lake, and defines data types. When the data extracted from the Raspberry Pi is stored in the data lake, it is loaded, labeled, and stored in the feature store in transformed form, so it is named ELT.

## Features

- [ ] Parse the values in the data lake and load them into memory, then organize them in a way that the data labeler can easily read.
- [ ] Call the labeler.
- [ ] Put the labeled data into the feature store.

# Environment

The environment is based on MacOS and Linux.

## `Makefile`

The `Makefile` has the following functions.

### `make lint`

- To use the `.vscode` settings, install the `pylint` extension.
- Overrides the options specified in the `pyproject.toml` file to lint the code.

### `make format`

- Uses google's `yapf` formatter.
- Overrides the options specified in the `pyproject.toml` file to format the code.
- To use the `.vscode` settings, install the `yapf` extension.

### `make test`

- Uses `unittest` for testing.
- Supports both `test_*.py` and `*_test.py` patterns.
- The test file must be connected to `__init__.py` up to the location of the test file.

### `make publish`

- Write the `~/.pypirc` file as follows.
    ```
    [pypi]
    username = __token__
    password = pypi-어쩌고저쩌고 # Replace with your personal API token.
    ```
- This command uses `flit` to push the package to the PyPI public registry.
- The previously specified name `myproject` (alias) will be uploaded, and anyone in the world can install the package using `python3 -m pip install myproject`.