import folium, requests

address = '서울특별시 서초구 강남대로 459(서초동) 백암 빌딩'
url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address

api_key = '5ae558165760e3cd65577d48aa32fbff'
header = {'Authorization': 'KakaoAK ' + api_key}

def getGocoder(address):
    result = ''

    r = requests.get(url, headers=header)

    if r.status_code == 200:
        try:
            result_address = r.json()["documents"][0]["address"]
            result = result_address["y"], result_address["x"]
        except Exception as err:
            return None
    else:
        result = "ERROR[" + str(r.status_code) + "]"

    return result

address_latlng = getGocoder(address)

latitude = address_latlng[0]
longitude = address_latlng[1]

print('주소지 :', address)
print('위도 :', latitude)
print('경도 :', longitude)


shopinfo = '서초 비트점'
foli_map = folium.Map(location=[latitude, longitude], zoom_start=17)
myicon = folium.Icon(color='red', icon='info-sign')
folium.Marker([latitude, longitude], popup=shopinfo, \
              icon=myicon).add_to(foli_map)

folium.CircleMarker([latitude, longitude], radius=300, color='blue', \
            fill_color='red', fill=False, popup=shopinfo).add_to(foli_map)

foli_map.save('c:/imsi/my_map_graph.html')
print('파일 저장 완료')




