# README Example

This is an example on a README that explains how to make use of a gitignore template generator.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install **git-ignore**.

You might need to to make a new python environment to install it. You can find further [information here on how to make a python environment and activate it](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments). 

```bash
pip install git-ignore
```

## Usage

With the use of `git-ignore` then we can make simple gitignore file using templates from GitHub.

### Adding a python gitignore template 

```bash
git-ignore python 
```

This will then make a gitignore file with the template for python.

### Adding more to the gitignore template

```bash
git-ignore --add /example_folder example_file.txt 
```

This will two new lines at the bottom of the gitignore file.

### Making use of several templates

```bash
git-ignore kotlin swift python java
``` 

This will add everything from all templates into the gitignore file.
