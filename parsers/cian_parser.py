from datetime import datetime
import requests

from database import db


import json


def get_json():

    cookies = {
        '_CIAN_GK': 'ae29c8b6-c1c9-4450-8882-2f6946ca62f3',
        'session_region_id': '2',
        'session_main_town_region_id': '2',
        'login_mro_popup': '1',
        '_gcl_au': '1.1.1815962790.1651823536',
        'sopr_utm': '%7B%22utm_source%22%3A+%22direct%22%2C+%22utm_medium%22%3A+%22None%22%7D',
        'sopr_session': '6b436e75346641b3',
        'uxfb_usertype': 'searcher',
        'uxs_uid': '72c935d0-cd11-11ec-8bcd-2b1044767462',
        'tmr_lvid': '632bb878004c001bd95f3d6865eef82d',
        'tmr_lvidTS': '1651823536857',
        '_ym_uid': '1651823537506970284',
        '_ym_d': '1651823537',
        '_ga': 'GA1.2.80883031.1651823537',
        '_gid': 'GA1.2.1749550238.1651823537',
        '_ym_isad': '2',
        '_ym_visorc': 'b',
        'afUserId': '16ae43be-8c57-4878-8dd8-7fa71b14eb24-p',
        'AF_SYNC': '1651823538432',
        'serp_registration_trigger_popup': '1',
        '_cc_id': '24e472dde65e2a271ef4f89dcffa654b',
        'panoramaId_expiry': '1651911265000',
        '__cf_bm': 'EX7wX3wFkfoF.gZGxSw1WKDcC4IJ5wdfLHhrHV5Uex4-1651825467-0-AUWFDpmDeggzd+FgpELB6t9kn9WjmO4wVnGLL5VoGAH/YO3OSIxKSGtG7pp0or6cgbnSSfO/FGzFCdCYy2Ipods=',
        'tmr_reqNum': '68',
        '_dc_gtm_UA-30374201-1': '1',
    }

    headers = {
        'authority': 'api.cian.ru',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'no-cache',
        'content-type': 'text/plain;charset=UTF-8',
        # Requests sorts cookies= alphabetically
        # 'cookie': '_CIAN_GK=ae29c8b6-c1c9-4450-8882-2f6946ca62f3; session_region_id=2; session_main_town_region_id=2; login_mro_popup=1; _gcl_au=1.1.1815962790.1651823536; sopr_utm=%7B%22utm_source%22%3A+%22direct%22%2C+%22utm_medium%22%3A+%22None%22%7D; sopr_session=6b436e75346641b3; uxfb_usertype=searcher; uxs_uid=72c935d0-cd11-11ec-8bcd-2b1044767462; tmr_lvid=632bb878004c001bd95f3d6865eef82d; tmr_lvidTS=1651823536857; _ym_uid=1651823537506970284; _ym_d=1651823537; _ga=GA1.2.80883031.1651823537; _gid=GA1.2.1749550238.1651823537; _ym_isad=2; _ym_visorc=b; afUserId=16ae43be-8c57-4878-8dd8-7fa71b14eb24-p; AF_SYNC=1651823538432; serp_registration_trigger_popup=1; _cc_id=24e472dde65e2a271ef4f89dcffa654b; panoramaId_expiry=1651911265000; __cf_bm=EX7wX3wFkfoF.gZGxSw1WKDcC4IJ5wdfLHhrHV5Uex4-1651825467-0-AUWFDpmDeggzd+FgpELB6t9kn9WjmO4wVnGLL5VoGAH/YO3OSIxKSGtG7pp0or6cgbnSSfO/FGzFCdCYy2Ipods=; tmr_reqNum=68; _dc_gtm_UA-30374201-1=1',
        'origin': 'https://spb.cian.ru',
        'pragma': 'no-cache',
        'referer': 'https://spb.cian.ru/',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    }

    data = '{"jsonQuery":{"sort":{"type":"term","value":"creation_date_desc"},"is_by_homeowner":{"type":"term","value":true},"_type":"suburbansale","suburban_offer_filter":{"type":"term","value":2},"region":{"type":"terms","value":[2]},"object_type":{"type":"terms","value":[1,2,3,4]},"engine_version":{"type":"term","value":2},"currency":{"type":"term","value":2},"price":{"type":"range","value":{"lte":3000000}}}}'

    # url = 'https://api.cian.ru/search-offers/v2/search-offers-desktop/'
    # response = requests.post(url=url,
    #                          cookies=cookies,
    #                          headers=headers,
    #                          data=data)
    # result = response.json()
    with open(r'C:\Users\yatep\OneDrive\Рабочий стол\Evgeny_Lukin_Parser_2\data_from_parsing\cian_dict.json', encoding='utf-8') as file:
        result = json.load(file)
    # print(result)

    return result


def get_offers(data: dict) -> list:
    offers = list()
    items: list = data['data']['offersSerialized']
    for item in items:
        if db.check_database(item['cianId']):
            continue
        offer = {}
        offer['id'] = item['cianId']
        offer['title'] = item['land']['area'] + ' соток.'
        offer['price'] = item['bargainTerms']['price']
        offer['url'] = item['fullUrl']
        offer['description'] = item['description'].replace('\n', ' ')
        offer['geo'] = item['geo']['userInput']
        timestamp = datetime.fromtimestamp(item['addedTimestamp'])
        timestamp = datetime.strftime(timestamp, '%d.%m.%Y в %H:%M')
        offer['date'] = timestamp
        offers.append(offer)
    db.save_to_db(offers)


def main():
    data = get_json()
    get_offers(data)
