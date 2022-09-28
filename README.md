# Alpha Vantage API Example
Hello world code to extract currency info from Alpha Vantage and return it in a CSV format.

## Setup
1) Ensure PYENV and Python are installed (See "PYENV and Python 3.8.10 Install" below)
2) Create VENV for project (See "Create VENV for project" below)
3) Get Alpha Vantage API key from https://www.alphavantage.co/documentation/
4) To run: `python stocks.py <API KEY>`
5) To test:  `python -m unittest tests/stocks_test.py`

# Create VENV for project
[Additional Install pyenv-virtualenv Info](https://github.com/pyenv/pyenv-virtualenv#installing-with-homebrew-for-macos-users)

Example install for ingestion:
```
pyenv virtualenv 3.8.10 stocks-alpha-3.8.10
```

Then activate (will need this if you are running tests from command line):
```
pyenv activate stocks-alpha-3.8.10
```

### Install Requirements:
```
pip install -r requirements.txt
```

# PYENV and Python 3.8.10 Install

## Install PyEnv
* Use [pyenv](https://github.com/pyenv/pyenv/wiki) to Install Python 3.8.
```
# Maybe optional xcode -> xcode-select --install
# Maybe optional homebrew -> /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew update
brew install openssl readline sqlite3 xz zlib
brew install pyenv
```

## Update bash profile
Now add this to your shell profile (for me .zszchrc)
```
# Pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```
Use [this to check](https://github.com/pyenv/pyenv/wiki#how-to-verify-that-i-have-set-up-pyenv-correctly)

### Install Python 3.8.10
Latest [3.8 release](https://www.python.org/downloads/release/python-3810/)
```
pyenv install -l - list all versions available.
pyenv install 3.8.10
pyenv shell 3.8.10
source ~/.zshrc
python --version
-> Python 3.8.10 
```
