# Template for Python projects

## Introduction

This is the boiler for any of my Python projects. This includes most of the good practices I use for having a clean, well-maintained and sharable code. Feel free to use this template for any of your future or existing projects! 🚀

## Use
When creating the package, run 
```bash
pre-commit install   // to install the pre-commit hooks
```

The main entry point for your code is `main.py` . Feel free to add any other entry points as you wish.
You can run it with
```bash
uv run python main.py
```

## Tooling

Here below is provided the list of tools used in this repo. 

### uv

This repo uses `uv` for dependency management and packaging. 

#### Install the repo as a package
You can install the repo with 
```bash
uv pip install -e .  // for editable mode 
uv pip install .     // not editable, a copy of the package is saved in the .venv
```

#### Add a package

To add a package, use

```bash
uv add <package-name>
```

for example `uv add numpy==2.5.2`. By default, `uv` uses PyPI as the library for downloading packages. 

#### Run executable
`uv` also allows you to run the specific version of python with 

```bash
uv run python
```

or any other executable you have in your `.venv/bin` 
Learn more about `uv` [here](https://docs.astral.sh/uv/).

### hydra
All the config related code is handle by `hydra`. The config is located in `config/config.yaml`. You can add different arguments there, they will be read by `hydra` and directly be accessible in the `config` object (see `main.py`). 

You can also override the different arguments when running the script from the CLI with for example 
```bash  
uv run python main.py argument1=value1 +argument2=value2
```
here `argument1` value is overwritten with `value1` and a new argument `argument2` is added to the config. 

Learn more about `hydra` [here](https://hydra.cc/docs/intro/).

### pre-commit
`pre-commit` is a tool that allows to correct the code based on some hooks before they get commited. This allows to have the same exact rules for the code: number of trailing spaces, checking missing semi colons, line spacing etc. 
The different hooks are defined in the `.pre-commit-config.yaml`. 

pre-commit has two capacities, a linter and a formatter. Some changes like trailing spaces are easy for the formatter to change. However, some other ones are more tricky (synthax changes). This means that sometimes that hooks will fail, sometimes just recommiting the changed files is enough, ONLY after adding them again first. Otherwise, you would have to change them manually, readd and recommit them for `pre-commit` to be happy.  

Learn more about `pre-commit` [here](https://pre-commit.com).

## Debugging (VSCode or Cursor)
This is some basic debugging with VSCode or Cursor. When running in debug mode, you can edit the config in the `.vscode/launch.json`. 
You can add different entry points or change the arguments. 
