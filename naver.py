import time

try:
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd

    url = 'https://finance.naver.com/marketindex/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    exchangeList = soup.select('#exchangeList > li')
    exchange_datas = []
    baseUrl = 'https://finance.naver.com'

    for item in exchangeList:
        data = {
            'title' : item.select_one('.h_lst').get_text(),
            'exchange' : item.select_one('.value').get_text(),
            'change' : item.select_one('.change').get_text(),
            'updown' : item.select_one('div.head_info > .blind').get_text(),
            'link' : baseUrl + item.select_one('a')['href']
        }

        # print(data)
        exchange_datas.append(data)

    df = pd.DataFrame(exchange_datas)
    df.to_excel('./data_web_data/naver_finance.xlsx', encoding='utf-8')

    print('save clear')
    time.sleep(3)

except:
    print('ModuleNotFoundError')
    time.sleep(3)