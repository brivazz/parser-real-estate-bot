from datetime import datetime
import requests

from database import db


def get_json() -> dict:

    cookies = {
        'yuidss': '2190146811651901224',
        'suid': 'ea350b3d3b00cfafb2d0f551bae89efb.0d7d36b521eae342efc2882611050e38',
        '_csrf_token': '9f43b61b2615eaebb51f7f596a9e357ff2ad372d437b1e6a',
        'from': 'direct',
        'yandexuid': '2190146811651901224',
        'i': 'UwkKCQIhAxVLyhIjOuQKG9VFEkmr1QL5F7bYyIktMVpHK0MuPUAJrddXGbCEiHPnZawjdQw0dEVjrJBfXZmVysdBpDI=',
        'ymex': '1967261239.yrts.1651901239#1967261239.yrtsi.1651901239',
        'font_loaded': 'YSv1',
        'is_gdpr': '0',
        'gdpr': '0',
        '_ym_isad': '2',
        '_ym_uid': '1651901377938703144',
        '_ym_d': '1651901383',
        'amcuid': '4593740101651906151',
        'is_gdpr_b': 'CK2NTBDDcSgC',
        'prev_uaas_data': '2190146811651901224%23493497%23538052%23488330%23441433%23369991%23359396%23570995%23560745%23558935%23561214%23545039%23507280%23361531%23241661%23213159',
        'prev_uaas_expcrypted': 'kDU-d_ryyYDlQGUKNqDSTnP66t4AAcLrFyF4-tL9gMc-d6rF1An2Vt7hTvv5VaR_eajwRjVO62AndpaCfrAKNqWIEGkJ0rLpXoX4RP468Ua4IpKEfVzbN4rdSgpedgqaoylE4Ef0-iw8-VACQMiU3dBSrlCiqkrYFiLkY_fClgpVfWJD-x7BWSNr1BDw_2kwCD18ubR-NE0LjIgrSOpNQShyLYzDnzztIGxVkziCeWXUWbGLD98VIA%2C%2C',
        'rgid': '417899',
        '_yasc': '6Zih3uHsffDxlWfqdH0Q3yDwwCFRtx5h/ZD2UnHCpxfQhaX87EFrAw==',
        'from_lifetime': '1651914107033',
    }

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Client-View-Type': 'desktop',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'yuidss=2190146811651901224; suid=ea350b3d3b00cfafb2d0f551bae89efb.0d7d36b521eae342efc2882611050e38; _csrf_token=9f43b61b2615eaebb51f7f596a9e357ff2ad372d437b1e6a; from=direct; yandexuid=2190146811651901224; i=UwkKCQIhAxVLyhIjOuQKG9VFEkmr1QL5F7bYyIktMVpHK0MuPUAJrddXGbCEiHPnZawjdQw0dEVjrJBfXZmVysdBpDI=; ymex=1967261239.yrts.1651901239#1967261239.yrtsi.1651901239; font_loaded=YSv1; is_gdpr=0; gdpr=0; _ym_isad=2; _ym_uid=1651901377938703144; _ym_d=1651901383; amcuid=4593740101651906151; is_gdpr_b=CK2NTBDDcSgC; prev_uaas_data=2190146811651901224%23493497%23538052%23488330%23441433%23369991%23359396%23570995%23560745%23558935%23561214%23545039%23507280%23361531%23241661%23213159; prev_uaas_expcrypted=kDU-d_ryyYDlQGUKNqDSTnP66t4AAcLrFyF4-tL9gMc-d6rF1An2Vt7hTvv5VaR_eajwRjVO62AndpaCfrAKNqWIEGkJ0rLpXoX4RP468Ua4IpKEfVzbN4rdSgpedgqaoylE4Ef0-iw8-VACQMiU3dBSrlCiqkrYFiLkY_fClgpVfWJD-x7BWSNr1BDw_2kwCD18ubR-NE0LjIgrSOpNQShyLYzDnzztIGxVkziCeWXUWbGLD98VIA%2C%2C; rgid=417899; _yasc=6Zih3uHsffDxlWfqdH0Q3yDwwCFRtx5h/ZD2UnHCpxfQhaX87EFrAw==; from_lifetime=1651914107033',
        'Pragma': 'no-cache',
        'Referer': 'https://realty.yandex.ru/sankt-peterburg/kupit/uchastok/?priceMax=3000000&agents=NO',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'X-Retpath-Y': 'https://realty.yandex.ru/sankt-peterburg/kupit/uchastok/?priceMax=3000000&agents=NO',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'priceMax': '3000000',
        'agents': 'NO',
        'rgid': '417899',
        'type': 'SELL',
        'category': 'LOT',
        '_pageType': 'search',
        '_providers': [
            'seo',
            'queryId',
            'forms',
            'filters',
            'filtersParams',
            'direct',
            'mapsPromo',
            'newbuildingPromo',
            'refinements',
            'search',
            'react-search-data',
            'searchHistoryParams',
            'searchParams',
            'searchPresets',
            'serpDirectPicType',
            'showSurveyBanner',
            'seo-data-offers-count',
            'related-newbuildings',
            'breadcrumbs',
            'ads',
            'categoryTotalOffers',
            'footer-links',
            'site-special-projects',
        ],
        'crc': 'y0b9932cc61df8d0005ec849f153b7a9b',
    }

    url = 'https://realty.yandex.ru/gate/react-page/get/'
    response = requests.get(url=url,
                            params=params,
                            cookies=cookies,
                            headers=headers)
    response.raise_for_status()
    data = response.json()

    return data


def get_offers(data: dict) -> list:
    offers = []
    entities: list = data['response']['search']['offers']['entities']
    for item in entities:
        if db.check_database(int(item['offerId'])):
            continue
        offer = {}
        offer['id'] = int(item['offerId'])
        offer['title'] = str(item['area']['value']) + ' соток.'
        offer['price'] = item['price']['value']
        offer['url'] = item['shareUrl']
        offer['description'] = item['description']
        offer['geo'] = item['location']['geocoderAddress']
        if item.get('updateDate'):
            offer_date = datetime.strptime(item['updateDate'], "%Y-%m-%dT%H:%M:%SZ")
            offer_date = datetime.strftime(offer_date, '%d.%m.%Y в %H:%M')
        else:
            offer_date = datetime.strptime(item['creationDate'], "%Y-%m-%dT%H:%M:%SZ")
            offer_date = datetime.strftime(offer_date, '%d.%m.%Y в %H:%M')
        offer['date'] = offer_date
        offers.append(offer)
    db.save_to_db(offers)


def main():
    data = get_json()
    get_offers(data)
