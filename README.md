# Getting started
## Prerequisites
### Packages
```
sudo apt install python3.9 python3-pip tor
```
```
pip3 install pipenv
```
### Services
`tor` service must be running if you want to use a `tor` session.
```
sudo systemctl start tor
systemctl status tor
```
```
● tor.service - Anonymizing overlay network for TCP (multi-instance-master)
     Loaded: loaded (/lib/systemd/system/tor.service; enabled; vendor preset: enabled)
     Active: active (exited) since Mon 1900-01-01 00:00:00 UST; 1s ago
    Process: 971 ExecStart=/bin/true (code=exited, status=0/SUCCESS)
   Main PID: 971 (code=exited, status=0/SUCCESS)
        CPU: 1ms
```
### ChromeDriver
To use Selenium Chrome emulator, chromedriver must be downloaded from the [download page](https://chromedriver.chromium.org/downloads).
Also, you must specify its path in `common.py`.
```
# common.py
class Constants:
    DRIVER_PATH = '/path/to/chromedriver'
```

## Install
Clone the repository.
```
git clone https://github.com/hsseek/proxy-session
cd proxy-session
```
Build the virtual environment using `pipenv`.
```
pipenv install
```
_Otherwise, you can install the following `pip` packages manually(Not recommended)_.
```
pip3 install requests pysocks selenium beautifulsoup4
```

## Run
Run the script on the `pipenv` virtual environment using `pipenv run` or `pipenv shell`.
```
pipenv run python3 requests_session.py
```
```
pipenv run python3 selenium_session.py
```
