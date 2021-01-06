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
