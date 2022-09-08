<p align=center>

  <img style="width:20%;" src="https://i.imgur.com/nWWudwU.png"/>

  <br>
  <span>Don't spend too much time farming. Touch grass and let this script do the work for you.</span>
  <br>

<p align="center">
  <a href="#installation">Installation</a>
  &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#usage">Usage</a>
</p>

<p align="center">
<a href="https://asciinema.org/a/223115">
<img src="./images/sherlock_demo.gif"/>
</a>
</p>


## Installation

```console
# clone this repo
$ git clone https://github.com/frozdbyte/autofarmer.git

# change the working directory to autofarmer
$ cd autofarmer

# install the requirements
$ py firsttimesetup.py
or
$ python3 firsttimesetup.py

# Configure your item and iventory positions
$ py findpositions.py
```

## Usage

```console
$ python3 farmer.py

$ python3 findpositions.py
usage: findpositions.py [--skip]

optional arguments:
--skip -> creates a config file with 0 values. Use this if you dont want the scripts to drag the items to another inventory

$ python3 firsttimesetup.py
usage: firsttimesetup.py [--cmd]

optional arguments:
--cmd -> enables manualy chaning the pip command used to install dependencies
```
