# Manage python environment in macos

## Install homebrew
go to https://brew.sh and follow the instruction.
 
## install pyenv
```
brew update
brew install pyenv
```
## Install python 3.8.7 in pyenv
```
pyenv install 3.8.7
```
## Set python 3.8 as global python
```
pyenv global 3.8.7
```
## Add pyenv to .zshrc
Add the following commands to the .zshrc
```
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
```

# Use pyenv-virtualenv to create virtual environments
## Install pyenv-virtualenv
```
brew install pyenv-virtualenv
```
##  Add pyenv-virtualenv to your .zshrc
Add the following command to your .zshrc file.
```
eval "$(pyenv virtualenv-init -)"
```
## Create virtual environment
```
pyenv virtualenv 3.8.7 <your-virtual-env-name>
```

## To activate the virtual environment
```
pyenv activate <your-virtual-env-name>
```

## Move to the project directory, and set local python environment

```
pyenv local your-virtual-env-name
```

## List, delete virtual environments
```
virtualenv   Create a Python virtualenv using the pyenv-virtualenv plugin
virtualenv-delete   Uninstall a specific Python virtualenv
virtualenv-init   Configure the shell environment for pyenv-virtualenv
virtualenv-prefix   Display real_prefix for a Python virtualenv version
virtualenvs   List all Python virtualenvs found in `$PYENV_ROOT/versions/*'.
```
