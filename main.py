import requests
import json


def get_data():
    cookies = {
        'HINTS_FIO_COOKIE_NAME': '2',
        'MVID_CATALOG_STATE': '1',
        'MVID_FILTER_CODES': 'true',
        'MVID_FILTER_TOOLTIP': '1',
        'MVID_FLOCKTORY_ON': 'true',
        'MVID_GIFT_KIT': 'true',
        'MVID_IS_NEW_BR_WIDGET': 'true',
        'MVID_LAYOUT_TYPE': '1',
        'MVID_GUEST_ID': '20772621777',
        'MVID_GET_LOCATION_BY_DADATA': 'DaData',
        'MVID_GEOLOCATION_NEEDED': 'true',
        'MVID_CART_MULTI_DELETE': 'false',
        'MVID_CALC_BONUS_RUBLES_PROFIT': 'false',
        'MVID_ADDRESS_COMMENT_AB_TEST': '2',
        'MVID_BLACK_FRIDAY_ENABLED': 'true',
        'MVID_KLADR_ID': '7800000800000',
        'MVID_CITY_ID': '7300087',
        'MVID_ABC_TEST_WIDGET': '0',
        'MVID_AB_PROMO_DAILY': '1',
        'MVID_AB_SERVICES_DESCRIPTION': 'var4',
        'MVID_AB_TEST_COMPARE_ONBOARDING': 'true',
        'MVID_WEBP_ENABLED': 'true',
        'MVID_SERVICES_MINI_BLOCK': 'var2',
        'MVID_REGION_ID': '6',
        'MVID_PRM20_CMS': 'true',
        'MVID_PRICE_FIRST': '2',
        'MVID_NEW_MBONUS_BLOCK': 'true',
        'MVID_NEW_LK_OTP_TIMER': 'true',
        'MVID_NEW_LK_CHECK_CAPTCHA': 'true',
        'MVID_NEW_DESKTOP_FILTERS': 'true',
        'MVID_NEW_ACCESSORY': 'true',
        'MVID_REGION_SHOP': 'S904',
        'MVID_TAXI_DELIVERY_INTERVALS_VIEW': 'old',
        'MVID_TIMEZONE_OFFSET': '3',
        'PICKUP_SEAMLESS_AB_TEST': '2',
        'PRESELECT_COURIER_DELIVERY_FOR_KBT': 'true',
        'PROMOLISTING_WITHOUT_STOCK_AB_TEST': '2',
        'searchType2': '2',
        'NEED_REQUIRE_APPLY_DISCOUNT': 'true',
        'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1',
        '__SourceTracker': 'google__organic',
        'admitad_deduplication_cookie': 'google__organic',
        '_ym_uid': '1653753894644640400',
        '_ym_d': '1653753894',
        'tmr_lvid': 'a8e9244c2b221102cfadcf23086f3b28',
        'tmr_lvidTS': '1653753894578',
        'gdeslon.ru.__arc_domain': 'gdeslon.ru',
        'gdeslon.ru.user_id': '716b2b5e-662e-4530-a02d-a4525b38183b',
        'uxs_uid': 'ea37bb10-de9f-11ec-98c7-511d990250d6',
        'afUserId': 'f753480e-963d-4277-887a-e2c9ab986c8a-p',
        'flocktory-uuid': '8cf42439-a93f-4cec-b846-e6cb9727e43b-4',
        'adrcid': 'AMI7wRocleeo2J5wl-_xAQg',
        '__ttl__widget__ui': '1653753978129-45a6661860ff',
        'wurfl_device_id': 'generic_web_browser',
        'MVID_OLD_NEW': 'eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==',
        'MVID_NEW_OLD': 'eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9',
        'deviceType': 'desktop',
        '__lhash_': '5f68156e466d86dcd59eee91d07e9748',
        'MVID_2_exp_in_1': '1',
        'MVID_GTM_DELAY': 'true',
        'MVID_LP_HANDOVER': '2',
        'MVID_LP_SOLD_VARIANTS': '3',
        'MVID_MCLICK': 'true',
        'MVID_MINI_PDP': 'true',
        'COMPARISON_INDICATOR': 'false',
        'MVID_NEW_LK_LOGIN': 'true',
        'flacktory': 'no',
        'MVID_MOBILE_FILTERS': 'false',
        'MVID_NEW_LK': 'true',
        'MVID_SERVICES': '111',
        'MVID_SMART_BANNER_BOTTOM': 'true',
        'MVID_SUPER_FILTERS': 'false',
        '_gid': 'GA1.2.575282947.1658511135',
        'SMSError': '',
        'authError': '',
        '_ym_isad': '2',
        'advcake_track_id': 'b861e3b0-5cbb-7365-f320-fef2e0c8c867',
        'advcake_session_id': '2776e131-3ac1-db3f-2b55-65c9116cb61e',
        'AF_SYNC': '1658511143401',
        'JSESSIONID': 'qTGSvhfX8XTH12lVmvLXC1KSTD7djyK3ZX71qGzTYvFrvWx057vM!-62409494',
        'bIPs': '930512162',
        'BIGipServeratg-ps-prod_tcp80': '1208278026.20480.0000',
        'MVID_GTM_BROWSER_THEME': '1',
        'BIGipServeratg-ps-prod_tcp80_clone': '1208278026.20480.0000',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VqX3xALX8XR0t9cRkmG00lMGlrLx5cWGQZDzBvJ2Z6SgtHSlYWGG89OkUJZR0uU1tCSDsYGjhrH2NHYiNMWT56Kx4ZfGwkUQkOYUREX28beyJfKggkYzVfGUNqTg1pN1wUPHVlPkdyey48Zh9iT10kQ1E/SF5dSRIyYhJAQE1HDTdAXjdXYTAPFhFNRxU9VlJPQyhrG3FYMA==amlzHQ==',
        '__zzatgib-w-mvideo': 'MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VqX3xALX8XR0t9cRkmG00lMGlrLx5cWGQZDzBvJ2Z6SgtHSlYWGG89OkUJZR0uU1tCSDsYGjhrH2NHYiNMWT56Kx4ZfGwkUQkOYUREX28beyJfKggkYzVfGUNqTg1pN1wUPHVlPkdyey48Zh9iT10kQ1E/SF5dSRIyYhJAQE1HDTdAXjdXYTAPFhFNRxU9VlJPQyhrG3FYMA==amlzHQ==',
        'cfidsgib-w-mvideo': '/xubvAgyUpEo4JHu2HP26YVPnWYdcLtBAldJuqk0/Y2NAacSiSOAWk0N32I2FjNFHDQGr6Pcoa2F9Aao2Med/kRF+vfKuZYOI+grZZGM5etuxQ9esSbuxpLqXlHMAm8bpN8G1S14DqMRKy4EPivcPKo1iFC/hwd341XHpA==',
        'cfidsgib-w-mvideo': '/xubvAgyUpEo4JHu2HP26YVPnWYdcLtBAldJuqk0/Y2NAacSiSOAWk0N32I2FjNFHDQGr6Pcoa2F9Aao2Med/kRF+vfKuZYOI+grZZGM5etuxQ9esSbuxpLqXlHMAm8bpN8G1S14DqMRKy4EPivcPKo1iFC/hwd341XHpA==',
        'gsscgib-w-mvideo': 'JB8vPsk8dw314zQREiBwtzpBPH120dyGsPz27yy61LQWeK++p9Fe5eOYDy3NfbsmWtWFK595LM/Rk/yR3r40z6r6x4HPLjPHQ8wvdXAVuWlbgeW1rhqUnJOZykoxoLuLJI1hb46nI+sL93U8ZeN0Xbi8IOk5IcT6qEIS9FI6Hk9tBfx03dOo0tc1HTt9ySbAtmdB8YkdyXVkj3mWFdL9jI0nh5T3+YeIuGBKA9mjK4HHT6th5/+mbG2FtPDGdA==',
        'gsscgib-w-mvideo': 'JB8vPsk8dw314zQREiBwtzpBPH120dyGsPz27yy61LQWeK++p9Fe5eOYDy3NfbsmWtWFK595LM/Rk/yR3r40z6r6x4HPLjPHQ8wvdXAVuWlbgeW1rhqUnJOZykoxoLuLJI1hb46nI+sL93U8ZeN0Xbi8IOk5IcT6qEIS9FI6Hk9tBfx03dOo0tc1HTt9ySbAtmdB8YkdyXVkj3mWFdL9jI0nh5T3+YeIuGBKA9mjK4HHT6th5/+mbG2FtPDGdA==',
        'fgsscgib-w-mvideo': '8a7Qce15489c25e40e0af6328280477d0a3e6955',
        'fgsscgib-w-mvideo': '8a7Qce15489c25e40e0af6328280477d0a3e6955',
        'cfidsgib-w-mvideo': '417UiGx+9Fe0G7Mvi6aEYHkjmEhvEFNk1vVYecVZocK1i0JNbqyz/dPnU12x7buHR17FM3T5BemsDiLJcPenywxSd5iWSXBq0K67GZ7dEoNDvn2KRQTDW/UkmOxy+rBL2seNETnibn3aSZiq15U5jIU6krOe+6I7ugxnQA==',
        'CACHE_INDICATOR': 'false',
        'MVID_WISH_LIST': '30063320',
        '_dc_gtm_UA-1873769-1': '1',
        '_dc_gtm_UA-1873769-37': '1',
        'mindboxDeviceUUID': 'cb7a11a1-81af-48f8-a973-07027615b129',
        'directCrm-session': '%7B%22deviceGuid%22%3A%22cb7a11a1-81af-48f8-a973-07027615b129%22%7D',
        '_ga': 'GA1.2.1612517612.1653753892',
        'tmr_detect': '0%7C1658511477454',
        'tmr_reqNum': '148',
        '_ga_CFMZTSS5FM': 'GS1.1.1658511134.3.1.1658511493.0',
        '_ga_BNX5WPP3YK': 'GS1.1.1658511134.3.1.1658511493.60',
        'MVID_ENVCLOUD': 'prod2',
    }

    headers = {
        'authority': 'www.mvideo.ru',
        'accept': 'application/json',
        'accept-language': 'ru-RU,ru;q=0.9,en-VG;q=0.8,en;q=0.7,en-US;q=0.6',
        # Requests sorts cookies= alphabetically
        # 'cookie': 'HINTS_FIO_COOKIE_NAME=2; MVID_CATALOG_STATE=1; MVID_FILTER_CODES=true; MVID_FILTER_TOOLTIP=1; MVID_FLOCKTORY_ON=true; MVID_GIFT_KIT=true; MVID_IS_NEW_BR_WIDGET=true; MVID_LAYOUT_TYPE=1; MVID_GUEST_ID=20772621777; MVID_GET_LOCATION_BY_DADATA=DaData; MVID_GEOLOCATION_NEEDED=true; MVID_CART_MULTI_DELETE=false; MVID_CALC_BONUS_RUBLES_PROFIT=false; MVID_ADDRESS_COMMENT_AB_TEST=2; MVID_BLACK_FRIDAY_ENABLED=true; MVID_KLADR_ID=7800000800000; MVID_CITY_ID=7300087; MVID_ABC_TEST_WIDGET=0; MVID_AB_PROMO_DAILY=1; MVID_AB_SERVICES_DESCRIPTION=var4; MVID_AB_TEST_COMPARE_ONBOARDING=true; MVID_WEBP_ENABLED=true; MVID_SERVICES_MINI_BLOCK=var2; MVID_REGION_ID=6; MVID_PRM20_CMS=true; MVID_PRICE_FIRST=2; MVID_NEW_MBONUS_BLOCK=true; MVID_NEW_LK_OTP_TIMER=true; MVID_NEW_LK_CHECK_CAPTCHA=true; MVID_NEW_DESKTOP_FILTERS=true; MVID_NEW_ACCESSORY=true; MVID_REGION_SHOP=S904; MVID_TAXI_DELIVERY_INTERVALS_VIEW=old; MVID_TIMEZONE_OFFSET=3; PICKUP_SEAMLESS_AB_TEST=2; PRESELECT_COURIER_DELIVERY_FOR_KBT=true; PROMOLISTING_WITHOUT_STOCK_AB_TEST=2; searchType2=2; NEED_REQUIRE_APPLY_DISCOUNT=true; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; __SourceTracker=google__organic; admitad_deduplication_cookie=google__organic; _ym_uid=1653753894644640400; _ym_d=1653753894; tmr_lvid=a8e9244c2b221102cfadcf23086f3b28; tmr_lvidTS=1653753894578; gdeslon.ru.__arc_domain=gdeslon.ru; gdeslon.ru.user_id=716b2b5e-662e-4530-a02d-a4525b38183b; uxs_uid=ea37bb10-de9f-11ec-98c7-511d990250d6; afUserId=f753480e-963d-4277-887a-e2c9ab986c8a-p; flocktory-uuid=8cf42439-a93f-4cec-b846-e6cb9727e43b-4; adrcid=AMI7wRocleeo2J5wl-_xAQg; __ttl__widget__ui=1653753978129-45a6661860ff; wurfl_device_id=generic_web_browser; MVID_OLD_NEW=eyJjb21wYXJpc29uIjogdHJ1ZSwgImZhdm9yaXRlIjogdHJ1ZSwgImNhcnQiOiB0cnVlfQ==; MVID_NEW_OLD=eyJjYXJ0IjpmYWxzZSwiZmF2b3JpdGUiOnRydWUsImNvbXBhcmlzb24iOnRydWV9; deviceType=desktop; __lhash_=5f68156e466d86dcd59eee91d07e9748; MVID_2_exp_in_1=1; MVID_GTM_DELAY=true; MVID_LP_HANDOVER=2; MVID_LP_SOLD_VARIANTS=3; MVID_MCLICK=true; MVID_MINI_PDP=true; COMPARISON_INDICATOR=false; MVID_NEW_LK_LOGIN=true; flacktory=no; MVID_MOBILE_FILTERS=false; MVID_NEW_LK=true; MVID_SERVICES=111; MVID_SMART_BANNER_BOTTOM=true; MVID_SUPER_FILTERS=false; _gid=GA1.2.575282947.1658511135; SMSError=; authError=; _ym_isad=2; advcake_track_id=b861e3b0-5cbb-7365-f320-fef2e0c8c867; advcake_session_id=2776e131-3ac1-db3f-2b55-65c9116cb61e; AF_SYNC=1658511143401; JSESSIONID=qTGSvhfX8XTH12lVmvLXC1KSTD7djyK3ZX71qGzTYvFrvWx057vM!-62409494; bIPs=930512162; BIGipServeratg-ps-prod_tcp80=1208278026.20480.0000; MVID_GTM_BROWSER_THEME=1; BIGipServeratg-ps-prod_tcp80_clone=1208278026.20480.0000; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VqX3xALX8XR0t9cRkmG00lMGlrLx5cWGQZDzBvJ2Z6SgtHSlYWGG89OkUJZR0uU1tCSDsYGjhrH2NHYiNMWT56Kx4ZfGwkUQkOYUREX28beyJfKggkYzVfGUNqTg1pN1wUPHVlPkdyey48Zh9iT10kQ1E/SF5dSRIyYhJAQE1HDTdAXjdXYTAPFhFNRxU9VlJPQyhrG3FYMA==amlzHQ==; __zzatgib-w-mvideo=MDA0dC0cTApcfEJcdGswPi17CT4VHThHKHIzd2VqX3xALX8XR0t9cRkmG00lMGlrLx5cWGQZDzBvJ2Z6SgtHSlYWGG89OkUJZR0uU1tCSDsYGjhrH2NHYiNMWT56Kx4ZfGwkUQkOYUREX28beyJfKggkYzVfGUNqTg1pN1wUPHVlPkdyey48Zh9iT10kQ1E/SF5dSRIyYhJAQE1HDTdAXjdXYTAPFhFNRxU9VlJPQyhrG3FYMA==amlzHQ==; cfidsgib-w-mvideo=/xubvAgyUpEo4JHu2HP26YVPnWYdcLtBAldJuqk0/Y2NAacSiSOAWk0N32I2FjNFHDQGr6Pcoa2F9Aao2Med/kRF+vfKuZYOI+grZZGM5etuxQ9esSbuxpLqXlHMAm8bpN8G1S14DqMRKy4EPivcPKo1iFC/hwd341XHpA==; cfidsgib-w-mvideo=/xubvAgyUpEo4JHu2HP26YVPnWYdcLtBAldJuqk0/Y2NAacSiSOAWk0N32I2FjNFHDQGr6Pcoa2F9Aao2Med/kRF+vfKuZYOI+grZZGM5etuxQ9esSbuxpLqXlHMAm8bpN8G1S14DqMRKy4EPivcPKo1iFC/hwd341XHpA==; gsscgib-w-mvideo=JB8vPsk8dw314zQREiBwtzpBPH120dyGsPz27yy61LQWeK++p9Fe5eOYDy3NfbsmWtWFK595LM/Rk/yR3r40z6r6x4HPLjPHQ8wvdXAVuWlbgeW1rhqUnJOZykoxoLuLJI1hb46nI+sL93U8ZeN0Xbi8IOk5IcT6qEIS9FI6Hk9tBfx03dOo0tc1HTt9ySbAtmdB8YkdyXVkj3mWFdL9jI0nh5T3+YeIuGBKA9mjK4HHT6th5/+mbG2FtPDGdA==; gsscgib-w-mvideo=JB8vPsk8dw314zQREiBwtzpBPH120dyGsPz27yy61LQWeK++p9Fe5eOYDy3NfbsmWtWFK595LM/Rk/yR3r40z6r6x4HPLjPHQ8wvdXAVuWlbgeW1rhqUnJOZykoxoLuLJI1hb46nI+sL93U8ZeN0Xbi8IOk5IcT6qEIS9FI6Hk9tBfx03dOo0tc1HTt9ySbAtmdB8YkdyXVkj3mWFdL9jI0nh5T3+YeIuGBKA9mjK4HHT6th5/+mbG2FtPDGdA==; fgsscgib-w-mvideo=8a7Qce15489c25e40e0af6328280477d0a3e6955; fgsscgib-w-mvideo=8a7Qce15489c25e40e0af6328280477d0a3e6955; cfidsgib-w-mvideo=417UiGx+9Fe0G7Mvi6aEYHkjmEhvEFNk1vVYecVZocK1i0JNbqyz/dPnU12x7buHR17FM3T5BemsDiLJcPenywxSd5iWSXBq0K67GZ7dEoNDvn2KRQTDW/UkmOxy+rBL2seNETnibn3aSZiq15U5jIU6krOe+6I7ugxnQA==; CACHE_INDICATOR=false; MVID_WISH_LIST=30063320; _dc_gtm_UA-1873769-1=1; _dc_gtm_UA-1873769-37=1; mindboxDeviceUUID=cb7a11a1-81af-48f8-a973-07027615b129; directCrm-session=%7B%22deviceGuid%22%3A%22cb7a11a1-81af-48f8-a973-07027615b129%22%7D; _ga=GA1.2.1612517612.1653753892; tmr_detect=0%7C1658511477454; tmr_reqNum=148; _ga_CFMZTSS5FM=GS1.1.1658511134.3.1.1658511493.0; _ga_BNX5WPP3YK=GS1.1.1658511134.3.1.1658511493.60; MVID_ENVCLOUD=prod2',
        'referer': 'https://www.mvideo.ru/noutbuki-planshety-komputery-8/noutbuki-118/f/skidka=da/tolko-v-nalichii=da',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'x-set-application-id': '8f52e915-ddb8-4aaa-bb46-d4e2093bd62a',
    }

    params = {
        'categoryId': '118',
        'offset': '0',
        'limit': '24',
        'filterParams': [
            'WyJza2lka2EiLCIiLCJkYSJd',
            'WyJ0b2xrby12LW5hbGljaGlpIiwiIiwiZGEiXQ==',
        ],
        'doTranslit': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/listing', params=params, cookies=cookies,
                            headers=headers).json()
    # print(response)

    products_ids = response.get('body').get('products')

    with open('1_products_ids.json', 'w', encoding='utf-8') as file:
        json.dump(products_ids, file, indent=4, ensure_ascii=False)

    # print(products_ids)

    json_data = {
        'productIds': products_ids,
        'mediaTypes': [
            'images',
        ],
        'category': True,
        'status': True,
        'brand': True,
        'propertyTypes': [
            'KEY',
        ],
        'propertiesConfig': {
            'propertiesPortionSize': 5,
        },
        'multioffer': False,
    }

    response = requests.post('https://www.mvideo.ru/bff/product-details/list', cookies=cookies, headers=headers,
                             json=json_data).json()

    with open('2_items.json', 'w', encoding='utf-8') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    # print(len(response.get('body').get('products')))

    products_ids_str = ','.join(products_ids)

    params = {
        'productIds': products_ids_str,
        'addBonusRubles': 'true',
        'isPromoApplied': 'true',
    }

    response = requests.get('https://www.mvideo.ru/bff/products/prices', params=params, cookies=cookies,
                            headers=headers).json()

    with open('3_prices.json', 'w', encoding='utf-8') as file:
        json.dump(response, file, indent=4, ensure_ascii=False)

    items_prices = {}

    material_prices = response.get('body').get('materialPrices')

    for item in material_prices:
        item_id = item.get('price').get('productId')
        item_base_price = item.get('price').get('basePrice')
        item_sale_price = item.get('price').get('salePrice')
        item_bonus = item.get('bonusRubles').get('total')

        items_prices[item_id] = {
            'item_basePrice': item_base_price,
            'item_salePrice': item_sale_price,
            'item_bonus': item_bonus
        }

    with open('4_items_prices.json', 'w', encoding='utf-8') as file:
        json.dump(items_prices, file, indent=4, ensure_ascii=False)


def get_result():
    with open('2_items.json', encoding='utf-8') as file:
        products_data = json.load(file)

    with open('4_items_prices.json', encoding='utf-8') as file:
        products_prices = json.load(file)

    products_data = products_data.get('body').get('products')

    for item in products_data:
        products_ids = item.get('productId')

        if products_ids in products_prices:
            prices = products_prices[products_ids]

        item['item_basePrice'] = prices.get('item_basePrice')
        item['item_salePrice'] = prices.get('item_salePrice')
        item['item_bonus'] = prices.get('item_bonus')

    with open('5_result.json', 'w', encoding='utf-8') as file:
        json.dump(products_data, file, indent=4, ensure_ascii=False)


def main():
    get_data()
    get_result()


if __name__ == '__main__':
    main()
