# Python Wheels for `pclpy`
This repository consists of two parts:

- Script for exporting the Anaconda package 
   [pclpy](https://github.com/davidcaron/pclpy) to a Python Wheel.
- A Python package for packaging dependencies.

## Build process
The main script is an [AppVeyor](https://www.appveyor.com/) build script (`appveyor.yml`).

### Preparation phase
The script sets up an Anaconda environment and installs `pclpy`.
It then prepares the build of the dependencies package
by copying required DLL files to `pclpy_dependencies/bin`.
Finally, it patches the `pclpy` package by including an `import pclpy_dependencies` statement during initialization.

### Packaging phase
Two packages are created.
The `pclpy` package is created
by simply zipping two directories in the Anaconda environment.
The dependencies package is created by running the `setup.py` script,
which is based on
[the original pclpy-dependencies project](https://github.com/davidcaron/pclpy-dependencies).

## Installation
Download the two `.whl` files from the [Releases](https://github.com/kad-vliegr/pclpy-conda2whl/releases) page
and install them with `pip`.
For example, for `pclpy` 0.12.0 for Python 3.7.x, you'd run something like the following commands:

```cmd
C:\Users\Alice> cd Downloads
C:\Users\Alice\Downloads> py -m pip install pclpy-0.12.0-cp37-cp37m-win_amd64.whl pclpy_dependencies-0.12.0-py3-none-any.whl
```
