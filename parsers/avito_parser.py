import json
from datetime import datetime
from urllib.parse import unquote

import requests
from bs4 import BeautifulSoup

from database import db


URL = 'https://www.avito.ru/sankt-peterburg/doma_dachi_kottedzhi/prodam/do-3-mln-rubley-ASgBAgECAUSUA9AQAUXGmgwXeyJmcm9tIjowLCJ0byI6MzAwMDAwMH0?user=1'


def get_html(URL):

    headers = {
        'authority': 'www.avito.ru',
        'method': 'GET',
        'path': '/sankt-peterburg/doma_dachi_kottedzhi/prodam/do-3-mln-rubley-ASgBAgECAUSUA9AQAUXGmgwXeyJmcm9tIjowLCJ0byI6MzAwMDAwMH0?user=1',
        'scheme': 'https',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'cookie': 'u=2tapup3v.1oa5g1j.1ib8xxmftuc00; v=1651572195; buyer_laas_location=653240; luri=sankt-peterburg; buyer_location_id=653240; _gcl_au=1.1.1064730760.1651572208; _gid=GA1.2.235335484.1651572208; adrdel=1; adrcid=AkMx-13XR_OgCkj_0I8Snyg; showedStoryIds=136-133-111-135-124-129-134-132-131-128-125-121-122-120-116-115-112-104-103-99-94; _ym_uid=1651572279859743709; _ym_d=1651572279; _ym_isad=1; _ym_visorc=b; f=5.0c4f4b6d233fb90636b4dd61b04726f147e1eada7172e06c47e1eada7172e06c47e1eada7172e06c47e1eada7172e06cb59320d6eb6303c1b59320d6eb6303c1b59320d6eb6303c147e1eada7172e06c8a38e2c5b3e08b898a38e2c5b3e08b890df103df0c26013a0df103df0c26013a2ebf3cb6fd35a0ac0df103df0c26013a8b1472fe2f9ba6b984dcacfe8ebe897bfa4d7ea84258c63d59c9621b2c0fa58f915ac1de0d034112ad09145d3e31a56946b8ae4e81acb9fae2415097439d4047fb0fb526bb39450a46b8ae4e81acb9fa34d62295fceb188dd99271d186dc1cd03de19da9ed218fe2d50b96489ab264edd50b96489ab264edd50b96489ab264ed46b8ae4e81acb9fa38e6a683f47425a8352c31daf983fa077a7b6c33f74d335c84df0fd22b85d35f40c395117dd828f6cb5ec09fa5c57cfa2c3b882b9005e0e3fd1e6c82c813ba390e28148569569b79a5b5e2f84776a9d33ec3c01f8dcca8a82ebf3cb6fd35a0ac0df103df0c26013a28a353c4323c7a3a140a384acbddd7486f27f6274560082c3de19da9ed218fe23de19da9ed218fe2ddb881eef125a8703b2a42e40573ac3c8edd6a0f40cbfd87da3d420d6cca468c; isCriteoSetNew=true; ft="0Bs2U/Wg0GcKhUX/bCZMqVawG2n3jIxX6avq67uS9rpr9z5zrQdUsMNSxt/WHsIukdqg/3z+jFbjITqvd4z/N5U07q9sP18iPTk/wyujnCapZ844vOu72DJ22kZmZ/TnxI01izrzpDy4c1SZUrTXJIAXby2+h+bwjfOxM6ZsN3nG1X8gfyZSoZ/Vexdz5mnr"; dfp_group=50; sx=H4sIAAAAAAAC%2F1TOy5HCMAwA0F58zsE%2FSRbdyJYdAoEkED4Lk973xM7SwJv3Nj4E9tE1cBijcqpUchESiLYECWx2b3M3O7PcZqlQlVKysNzrJPxq1%2F3PiQ%2FHfAXTmWp2DsEhcHS4dQZKldZSjZKxSW6uIBBqCyFDsJQ%2B8pHHSU%2FTWkYYpqdX3%2Bsw3B%2B38XDmkNOXHBJvnUFELErYGBkwIlfKNbAS2FJI%2F86yjn2fhmvrfX%2BbhyHMkdXL8pwujkr8LydE2jojmT02KzYLN2udg5q5aoqSVXyCj3xeJnroEZ75Ne8tzY91nqTSutf%2BdBm%2BzzGGbfsNAAD%2F%2FzOhiM1pAQAA; abp=0; _ga=GA1.2.1004786703.1651572208; SEARCH_HISTORY_IDS=1; _ga_9E363E7BES=GS1.1.1651572208.1.1.1651573056.60; cto_bundle=KSkvI19EcXhOSzAxZTVWTnd5VzRPa3pvMjhQU214SUU3d2ElMkZRJTJGdkRabnolMkZFTDZLeU80VXgyNGolMkJKWW5zWVFOWWlLUHBjMFE4T2NOdk90ejhpdWRTam1WelJubzJCZ0ZEd1UzVjc0UVBlSnFBbENXR2R5MFhGJTJGVktaOUhJa0xqRUd6bEtPSUV2YU1NczdObVVFNk00RVdZT05nJTNEJTNE; buyer_from_page=catalog',
        'pragma': 'no-cache',
        'referer': 'https://www.avito.ru/sankt-peterburg/doma_dachi_kottedzhi',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': "Windows",
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
    }

    # response = requests.get(url=URL, headers=headers)
    # response.raise_for_status()
    # html = response.text

    with open(r'C:\Users\yatep\OneDrive\Рабочий стол\Evgeny_Lukin_Parser_2\data_from_parsing\avito_doma_do_3mln.html', encoding='utf-8') as file:
        html = file.read()

    return html


def get_json(html) -> dict:
    soup = BeautifulSoup(html, 'lxml')

    scripts = soup.find_all('script')
    for script in scripts:
        if 'window.__initialData__' in script.text:
            json_text = script.text.split(';')[0].split('=')[-1].strip()
            json_text = unquote(json_text)
            json_text = json_text[1:-1]
            data = json.loads(json_text)

    return data


def get_offers(data: dict) -> list:
    SITE = 'https://www.avito.ru'
    offers = []
    for key in data:
        if 'single-page' in key:
            items: list = data[key]['data']['catalog']['items'][1:]
            for item in items:
                if item.get('id'):
                    if db.check_database(item['id']):
                        continue
                    offer = {}
                    offer['id'] = item['id']
                    offer['title'] = item['title']
                    offer['price'] = item['priceDetailed']['value']
                    offer['url'] = SITE + item['urlPath']
                    offer['description'] = item['description'].replace('\n', '').replace('\xa0', ' ')
                    try:
                        geo = item['geo']['geoReferences'][0]['content']
                    except IndexError:
                        geo = ''
                    if geo:
                        geo = geo.replace('\xa0', ' ')
                    address = item['geo']['formattedAddress']
                    offer['geo'] = geo + ' ' + address
                    timestamp = datetime.fromtimestamp(item['sortTimeStamp'] / 1000)
                    timestamp = datetime.strftime(timestamp, '%d.%m.%Y в %H:%m')
                    offer['date'] = timestamp
                    offers.append(offer)
    db.save_to_db(offers)

    return offers


def main():
    html = get_html(URL)
    data = get_json(html)
    offers = get_offers(data)
    return offers
