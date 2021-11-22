import common
import requests
from bs4 import BeautifulSoup


def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # get the HTTP response and construct soup object
    soup = BeautifulSoup(requests.get(url).content, "html.parser")
    proxies = []
    for row in soup.select('div.fpl-list > table.table > tbody > tr'):
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            host = f"{ip}:{port}"
            proxies.append(host)
        except IndexError:
            continue
    return proxies


def get_proxy_session(sampling_url: str):
    timeout = 10
    session = requests.session()
    try:
        code = session.get(sampling_url, timeout=timeout).status_code
        if code == 200:
            print('The url is accessible.')
            return session
    except Exception as proxy_exception:
        print('Error: Cannot load %s.\n%s' % (sampling_url, proxy_exception))
        free_proxy_list = get_free_proxies()
        for i, proxy in enumerate(free_proxy_list):
            try:
                session.proxies = {'http': 'http://' + proxy,
                                   'https://': 'https://' + proxy}
                if session.get(sampling_url, timeout=timeout).status_code == 200:
                    print('%s worked.(trial %d) ' % (proxy, i + 1))
                    return session
            except Exception as e:
                print('%s failed. %s' % (proxy, e))


def get_tor_session():
    req = requests.session()
    # Tor uses the 9050 port as the default socks port
    req.proxies = {'http': 'socks5://127.0.0.1:9050',
                   'https': 'socks5://127.0.0.1:9050'}
    return req


def get_ip(session: requests.Session) -> str:
    # return session.get('https://api.ipify.org').content.decode('utf8')
    return session.get('https://icanhazip.com').text.strip()


def try_loading(session: requests.Session, url, timeout: float = 5):
    try:
        session.get(url, timeout=timeout)
        print('Status code: %d\n' % session.get(url, timeout=timeout).status_code)
    except requests.exceptions.ReadTimeout:
        print('Timeout reached.\n')
    except requests.exceptions.ConnectionError:
        print('Connection error.\n')
    except Exception as exception:
        print('Exception raised.\n%s\n' % exception)
    finally:
        session.close()


if __name__ == "__main__":
    normal_session = requests.session()
    print('Original IP address: %s' % get_ip(normal_session))
    try_loading(normal_session, common.Constants.prohibited_url)

    print('Try loading with a tor service.')
    tor_session = get_tor_session()
    print('Tor IP address: %s' % get_ip(tor_session))
    try_loading(tor_session, common.Constants.prohibited_url)

    print('Try loading with via a proxy server.')
    proxy_session = get_proxy_session(common.Constants.prohibited_url)
    if proxy_session is not None:
        print('Proxy IP address: %s' % get_ip(tor_session))
        try_loading(proxy_session, common.Constants.prohibited_url)
    else:
        print('Error: Cannot find working proxy for the url.')