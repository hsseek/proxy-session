import time

import common
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def initiate_browser(is_tor_session: bool = False, is_headless: bool = False):
    # A chrome web driver with headless option
    service = Service(common.Constants.DRIVER_PATH)
    options = webdriver.ChromeOptions()
    if is_tor_session:
        options.add_argument('--proxy-server=socks5://127.0.0.1:9050')
    if is_headless:
        options.add_argument('headless')
        options.add_argument('disable-gpu')
    else:
        options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=service, options=options)
    return driver


def try_loading(session: webdriver.Chrome, url, timeout: float = 30, is_check_tor: bool = False):
    try:
        session.set_page_load_timeout(timeout)
        if is_check_tor:
            session.get('https://check.torproject.org/')
            time.sleep(1)
        session.get(url)
    except selenium.common.exceptions.TimeoutException:
        print('Timeout reached.')
    except Exception as exception:
        print('Exception raised.\n%s' % exception)
    finally:
        countdown = 3
        print('The browser will be closed in %d seconds.' % countdown)
        time.sleep(countdown)
        session.quit()


if __name__ == "__main__":
    normal_session = initiate_browser()
    try_loading(normal_session, common.Constants.prohibited_url, is_check_tor=True)

    # https://www.torproject.org/download/languages/
    tor_session = initiate_browser(is_tor_session=True)
    try_loading(tor_session, common.Constants.prohibited_url, is_check_tor=True)
