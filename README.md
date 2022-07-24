# check python version
py --version or python --version

- add python on "PATH" on system variables above windows apps or it won't work.
example of path: C:\Users\fabio\AppData\Local\Programs\Python\Python310

py -m venv ~/.virtualenvs/bin/activate  ??


# creating virtual envd
py -m venv .\testenv\

## usefull links
-https://stackoverflow.com/questions/41573587/what-is-the-difference-between-venv-pyvenv-pyenv-virtualenv-virtualenvwrappe

- https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

## setting virutal env
- creates environment
py -m venv env  
- use virtual env
.\env\Scripts\activate
- leave virtual env
deactivate
- using virtualenv, to set specific python version
virtualenv -p python3.9 env
- install dependencies
pip install -r requirements.txt

# Create requirements
```console
pip3 freeze > requirements.txt  # Python3
pip freeze > requirements.txt  # Python2
```

# anaconda

```console
# cheking anaconda version
conda -V

# update anaconda
conda update conda

# create envname   - Type conda search “^python$”  to see the list of available python versions.
conda create -n envname python=x.x anaconda

# activate conda environment
conda activate envname

# install package
conda install -n yourenvname package

# deactivate env
conda deactivate

# delete environment
conda remove -n envname -all

# allows conda on powershell
conda init powershell 

# deactivate auto on powershell
conda config --set auto_activate_base false

# install requirements
conda install --file requirements.txt 

# run conda project withs "python" so that it reads correct python version
```



# Installing pyenv - version management tool
pyenv is used to isolate Python versions.

on windows: 
https://github.com/pyenv-win/pyenv-win

## if windows, you probably need to run this first: 
- Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process  
or
- Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine

- ( after installation to block scrips again) Set-ExecutionPolicy -ExecutionPolicy restricted -Scope Process   

Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"

## **Add System Settings**

It's a easy way to use PowerShell here

1. Adding PYENV, PYENV_HOME and PYENV_ROOT to your Environment Variables

```pwsh
[System.Environment]::SetEnvironmentVariable('PYENV',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")

[System.Environment]::SetEnvironmentVariable('PYENV_ROOT',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")

[System.Environment]::SetEnvironmentVariable('PYENV_HOME',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
```

2. Now adding the following paths to your USER PATH variable in order to access the pyenv command

```pwsh
[System.Environment]::SetEnvironmentVariable('path', $env:USERPROFILE + "\.pyenv\pyenv-win\bin;" + $env:USERPROFILE + "\.pyenv\pyenv-win\shims;" + [System.Environment]::GetEnvironmentVariable('path', "User"),"User")
```

Installation is done. Hurray!

- to continue to run pyenv i had to run
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted



# git commands
- Setting your email address for every repository on your computer
git config --global user.email "{ID}+{username}@users.noreply.github.com"

- Revert your recent local commits (with your private email) which are getting failed to be pushed into repository.
git reset --soft HEAD~1 

- Stage and push those commits
git add .
git commit –m "<commit_message>"
git push