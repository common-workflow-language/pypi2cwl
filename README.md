`pypi2cwl` forms CWL tool descriptions from PyPi packages using [argparse2cwl](https://github.com/common-workflow-language/gxargparse). It installs the package if it hasn't been installed before, downloads the source code to a new directory, parses command-line scripts from package's `setup.py` and runs `argparse2cwl` against those scripts.

## Installing ##

	$ pip install pypi2cwl


## Usage ##

	$ pypi2cwl <package_name> [options]

Options (some of them are inherited from `argparse2cwl`):

* `-go`, `--generate_outputs`: flag for generating outputs not only from arguments that are instances of `argparse.FileType('w')`, but also from every argument which contains `output` keyword in its name. For instance, argument `--output-file` with no type will also be placed to output section. However, `--output-directory` argument will also be treated like file, so generated tools must be checked carefully when this option is selected.

* `-d`, `--directory`: directory for storing tool descriptions.

* `-v`, `--venv`: this flag must be used if `pypi2cwl` is run inside a virtual environment. Then a package, if it wasn't installed before, will be installed locally.

* `--no-clean`: the source package won't be deleted after running, so `setup.py` inside the package can be edited

## Troubleshooting ##

Sometimes `setup()` function cannot be parsed directly from package's `setup.py`. If `pypi2cwl` has exited with warning `could not import setup function` and a path to `setup.py` file, follow the path provided in the message, edit `setup.py` so `setup` function is available in the main body of the program and is executed during importing `setup.py`, and run `pypi2cwl` again with `--no-clean` option. The edits don't affect the program's behavior, because only the downloaded copy of the package is edited.

## Limitations ##

`pypi2cwl` cannot process packages where:

a) tools are not defined as command-line scripts in `setup.py`

b) argument parsers other than `argparse` (for instance, `sys.argv`) are used.

<br>
In these cases you should manually generate tool descriptions using `argparse2cwl`.