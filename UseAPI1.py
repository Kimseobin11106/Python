# 성일정보고 급식 api
import requests

def get_meals(dt):
    p = {
        'Type':'json',
        'ATPT_OFCOC_SC_CODE':'J10',
        'SD_SCHUL_CODE': '7530167',
        'MLSV_YMD': dt
    }

    url = 'https://open.neis.go.kr/hub/mealServiceDietInfo?Type=&pIndex=1&pSize=100&ATPT_OFCDC_SC_CODE=J10&SD_SCHUL_CODE=7530167'
    result = requests.get(url, params=p)

    try:
        if result.status_code == 200:
            meals = result.json()  # 결과를 json => dictionary 로 변환인식
            return meals['mealServiceDietInfo'][1]['row'][0]['DDISH_NM']
        else:
            return ''
    except:
        return ''

date = input('급식일자 입력해라. 20000101 형태')

meal = get_meals(dt=date)
if meal == '':
    print('자료가 없습니다.')
else:
    meal = str(meal).split('<br/>')
    for i in meal:
        print(i)
print(meal)