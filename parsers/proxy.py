import requests
from bs4 import BeautifulSoup
from random import choice


def get_proxy() -> dict:
    html = requests.get("https://free-proxy-list.net/").text
    soup = BeautifulSoup(html, 'lxml')
    proxies = []
    trs = soup.find('table', class_="table-striped").find('tbody').find_all('tr')[1:50]
    for tr in trs:
        tds = tr.find_all('td')
        if tds[6].text.strip() == "yes":
            schema = "https"
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            proxy = {'schema': schema, 'address': 'http://' + ip + ':' + port}
            proxies.append(proxy)

    return choice(proxies)
