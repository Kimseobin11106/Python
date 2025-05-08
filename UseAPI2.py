# 해당 날짜 일별 박스오피스 api
import requests

def getRank(targetDt):
    url = 'https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt=' + targetDt
    response = requests.get(url)
    if response.status_code == 200:
        try: # 시도했을 때, 정상적으로 실행되면 안쪽
            result = response.json()
            return result['boxOfficeResult']['dailyBoxOfficeList']
        except: # try에서 오류 발생시 이쪽
            return []
    else:
        return []

dt = input("날짜 (yyyy-mm-dd)")
movies = getRank(dt) # 제대로 된 10개 리스트 또는 빈 리스트
if len(movies) == 0:
    print('값이 없습니다.')
else:
    for movie in movies: # movies 10개의 영화 정보
        print(movie['rank'] + " 위" + "  " + movie['movieNm'])