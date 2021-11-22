# Getting started
## Prerequisites
```
sudo apt install python3.9 python3-pip
sudo pip3 install pipenv
```
## Install
Clone the repository.
```
git pull https://github.com/hsseek/proxy-session
cd proxy-session
```
Build the virtual environment using `pipenv`.
```
pipenv install
pipenv --venv
```
Otherwise, you can install the following `pip` packages manually _(Not recommended)_.
```
pip3 install requests pysocks selenium beautifulsoup4
```

## Run
Run the script using on the virtual environment using `pipenv run` or `pipenv shell`.
```
cd proxy-session
pipenv run python3 requests_session.py
pipenv run python3 selenium_session.py
```
