import urllib.request
import datetime
import json

access_key= "Rybj1iOxIcwK1rIaEg5oljwMXyHbQpABMC10s1FtIOTl%2BYxLuG3EdjNPFpkQekG20fV36JRexszFaOJaFXKriQ%3D%3D"

def get_Finedust_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL: %s" % (datetime.datetime.now(), url))
        return None


def air_quality(area="%EB%8C%80%EA%B5%AC", numOfRows="10", searchCondition="HOUR"):

    end_point = "http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnMesureSidoLIst"

    parameters = "?_returnType=json&ServiceKey="+access_key
    parameters += "&numOfRows="+numOfRows
    parameters += "&sidoName="+area
    parameters += "&searchCondition="+searchCondition

    url = end_point+parameters

    retData = get_Finedust_url(url)

    if retData == None:
        return None
    else:
        return json.loads(retData)

def make_air_quality():

    json_data = []

    raw_data = air_quality()
    data_list = raw_data['list']
    for air_quality_dict in data_list:
        json_data.append(air_quality_dict)

    return json_data

jsonResult = make_air_quality()

with open('시군구별 실시간 평균정보 조회.json', 'w', encoding='utf-8') as outfile:
     retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
     outfile.write(retJson)



