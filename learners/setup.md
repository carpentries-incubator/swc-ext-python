---
title: Setup
permalink: /setup/
---

## Setup

### Installing Python 

Follow the directions listed in the [python installation section of Carpentries workshop website template](https://carpentries.github.io/workshop-template/#python) for your operating system.

### Getting the Data

The data we will be using is taken from the [gapminder] dataset.
To obtain it, download and unzip the file
[python-novice-gapminder-data.zip](episodes/files/python-novice-gapminder-data.zip).
In order to follow the presented material, you should launch a Jupyter
notebook in the root directory (see Starting Python section below).

### Starting Python

We will teach Python using the [Jupyter lab][jupyter], a
programming environment that runs in a web browser. Jupyter requires a reasonably
up-to-date browser, preferably a current version of Chrome, Safari, or Firefox
(note that Internet Explorer version 9 and below are *not* supported). If you
installed Python using conda and have setup the `carpentries` conda environment, Jupyter should already be on your system.

To start the notebook, open a terminal or git bash or miniforge prompt.

Then, activate the carpentries conda enviornment

```bash
conda activate carpentries
```

Then, navigate to your project folder. If it is called `swc` and located on your `Desktop` it might look something like this:
```bash
cd ~/Desktop/swc
```

then launch jupter:

```bash
$ jupyter lab
```

To start the Python interpreter without the notebook, open a terminal
or Git Bash or miniforge prompt and type the command:

```bash
$ python
```

[python]: https://python.org
[gapminder]: https://gapminder.org
[jupyter]: https://jupyter.org/
[jupyter-install]: https://jupyter.readthedocs.io/en/latest/install.html#optional-for-experienced-python-developers-installing-jupyter-with-pip



