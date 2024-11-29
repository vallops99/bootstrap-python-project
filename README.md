# Bootstrap Python Project #
Bootstrap your Python project with [devbox](https://github.com/jetify-com/devbox), [uv](https://github.com/astral-sh/uv), [ruff](https://github.com/astral-sh/ruff), [mypy](https://github.com/python/mypy), and [pre-commit](https://github.com/pre-commit/pre-commit).

## Overview ##
This repository is intendend to give developers a way to improve their life.   
These are the most advanced tools of the moment that a Python developer can use.   
Next will be described the main reasons of such choices.

### What is devbox? What is used for? ###
Devbox is an environment manager, it is based on [Nix](https://nixos.org/) and it is perfect to create a custom, completely isolated, easy to handle, and easy to replicate environment with whatever techonology you are in need.    
In this case we create our environment with Python 3.13, uv 0.4.30, ruff 0.7.4, mypy 1.11.2, and pre-commit 4.0.1    
By just typing `devbox shell` in your terminal you start a new Nix shell configured through a devbox.json file (that describes the environment you are in need).

<p><b>Downside:</b></p>

It relies on nix-packages that are uploaded on an archive that requires a custom configuration for each project.   
This usually leads to delays between actual new release of a project and nix-package availabilty in the archive.  
Nice to know, it is completely open source, so you can open a PR that brings the new release you are in need into the archive.


### What is UV? What is used for? ###
UV is a Python package manager written in Rust by [Astral](https://astral.sh/) that helps managing the project too.   
Chosen for its lightness and speed compared to Pip (even Poetry), furthermore its lock system is cross platform compatible.   
It "inherits" Rust's workspace package managing that brings dependencies organization to another level.

<picture align="left">
    <source media="(prefers-color-scheme: dark)" srcset="https://github.com/astral-sh/uv/assets/1309177/03aa9163-1c79-4a87-a31d-7a9311ed9310">
    <source media="(prefers-color-scheme: light)" srcset="https://github.com/astral-sh/uv/assets/1309177/629e59c0-9c6e-4013-9ad4-adb2bcf5080d">
    <img alt="Shows a bar chart with benchmark results." src="https://github.com/astral-sh/uv/assets/1309177/629e59c0-9c6e-4013-9ad4-adb2bcf5080d">
</picture>

<p align="left">
    <i>
        Installing <a href="https://trio.readthedocs.io/">Trio</a>'s dependencies with a warm cache.
        <p>Thanks to Astral for the benchmark.</p>    
    </i>
</p>

<p><b>Why not other package managers?</b></p>

The picture above describes the situation, this is the fastest package manager at the moment.   
On top of that, in my opinion, it is the most clean and technologically advanced project of its type.


### What is Ruff? What is used for? ###
Ruff is a Python linter and formatter written in Rust by [Astral](https://astral.sh/) (it is the brother of UV).   
It is been choosen for its lightness and speed compared to others (Autoflake, Flake8, etc...).

<picture align="left">
    <source media="(prefers-color-scheme: dark)" srcset="https://user-images.githubusercontent.com/1309177/232603514-c95e9b0f-6b31-43de-9a80-9e844173fd6a.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://user-images.githubusercontent.com/1309177/232603516-4fb4892d-585c-4b20-b810-3db9161831e4.svg">
<img alt="Shows a bar chart with benchmark results." src="https://user-images.githubusercontent.com/1309177/232603516-4fb4892d-585c-4b20-b810-3db9161831e4.svg">
</picture>
<p align="left">
    <i>
        Linting the CPython codebase from scratch.
        <p>Thanks to Astral for the benchmark.</p>
    </i>
</p>

<p><b>Why not other linters/formatters?</b></p>

The picture above describes the situation, this is the fastest package manager at the moment.   
On top of that, in my opinion, it is the most clean and technologically advanced project of its type.  

### What is Mypy? What is used for? ###
Mypy is a static type checker for Python, it leverages Python's type hinting ([PEP 484](https://peps.python.org/pep-0484/)) in order to increase type safety.    
Bear in mind that Python is not a statically typed language, meaning that even if Mypy will give a positive result, the code isn't type safe!   
<p><b>Why not other static type checker?</b></p>

They all had something weird about:
- pyright, gives error "Argument missing for parameter 'flush'" on print statement (not the best first impression, may need further analysis);
- pyre, only live checking, does NOT have a cli to run the check from;
- pyanalize, it may execute files that have `if __name__ == '__main__'` because it imports file in order to type check them;
- pytype, by the time I'm writing it does NOT support Python 3.13;


### What is Pre-commit? What is used for? ###
Pre-commit is a framework for managing and maintaining Git hooks.   
Hooks are a magical Git thing, they let you run actions on versioning events (eg. Git's pre-commit hook runs a script between running `git commit` command and actually creating a commit).  
In this way you can implement linter, formatter and static type checker into your versioning pipeline and you can version the hooks configuration too!  
In this project, we already set up pre-commit in order to create a pre-commit hook that runs exactly: formatter, linter, static type checker and tests too through UV.  
Last but not least, the combination of devbox and pre-commit makes mandatory the installation of Git hooks into every cloned repository.  
For sure everyone could avoid activating the devbox shell and just create a commit, but if you manage every dependency through devbox nobody will take that route (developers are lazy that's why they are efficient).

<p><b>Why not other Git hooks frameworks?</b></p>

By the time I am writing, I am not aware of any other framework like that.  
If anybody is aware of that, please feel free to open a PR with your considerations, otherwise open an issue or contact me and I will spend some time evaluating it. 


## Getting Started ##
- [Install devbox](https://www.jetify.com/docs/devbox/installing_devbox/) and let it handle all the work for you;
- Clone the project by: `git clone git@github.com:vallops99/bootstrap-python-project.git` (change the url in case you prefer HTTPS over SSH);
- Throw away the `.git` folder as you will customize the project per your needs: `rm -rf bootstrap-python-project/.git`;
- Rename the project's folder as you like: `mv bootstrap-python-project <insert_your_project_name_here>`;
- Get into your project: `cd <insert_your_project_name_here>`;
- Initialize your new repository: `git init`;
- Run `devbox shell`.

The shell that will open after the last command is managed by [Nix](https://nixos.org/) and it will contain all your project's basic needs.    
This means that UV, Ruff, Mypy, and Pre-commit will be already installed.    
Bear in mind that this "needs" are your environment requirements that will let you work, that are different from your project requirements.   

Furthermore, if you look inside `devbox.json` you'll find a line under the key `init_hook`: `"pre-commit install"`.   
This line basically "installs" the git hooks under your project's `.git` directory (as they should be in order to work by default).   

Bear in mind that your first commit will be slow due to dependencies installation, other commits will be faster.
