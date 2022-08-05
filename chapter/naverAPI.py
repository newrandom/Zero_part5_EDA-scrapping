import os
import sys
import urllib.request

def naver_api(id, pw, search, where, **kwarg):
    ''' naver_api function v0.4
    id : id(str)
    pw : password(str)
    search : to search things(str)
    where : api node(str)
    
    **start_num : 검색결과 시작지정위치 (int)
    **disp_num : 검색결과 출력건수 지정 (int)
    '''

    # ==========**kwarg list ==== #
    # id = kwarg.get('id')
    # pw = kwarg.get('password')
    # search = kwarg.get('search')
    # where = kwarg.get('where')

    start_num = kwarg.get('start_num', 1)
    disp_num = kwarg.get('disp_num', 10)

    # ===== # 
    client_id = id             # INPUT
    client_secret = pw       # INPUT

    if 1 <= start_num <= 1000:       # 기본값(1), 최대값 (1000)
        param_start = '&start=' + str(start_num)
        if 1 <= disp_num <= 100 :    # 기본값(10), 최대값 (100)
            param_disp = '&display=' + str(disp_num)        # v0.3 - & add
        else:
            return print('Wrong display number')
    else:
        return print('Wrong start number')
        
    encText = urllib.parse.quote(search)     # INPUT
    url = f'https://openapi.naver.com/v1/search/{where}?query=' + encText + param_start + param_disp  # json 결과
    # url = f'https://openapi.naver.com/v1/search/{where}.xml?query=' + encText     # xml 결과
    print(url)
    

    request = urllib.request.Request(url)
    # request = urllib.request.Request(url, headers={'User-Agent' : 'Chrome'})

    request.add_header('X-Naver-Client-Id', client_id)
    request.add_header('X-Naver-Client-Secret', client_secret)

    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if (rescode==200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
        return response_body.decode('utf-8')    # v0.4 - add
    else:
        print('Error Code :' + rescode)