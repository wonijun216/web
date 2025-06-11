import streamlit as st
import folium
from streamlit_folium import st_folium

# 제목
st.title("🇪🇸 스페인 여행 가이드")
st.write("스페인의 대표적인 여행지를 지도와 함께 쉽고 자세히 소개합니다!")

# 여행지 데이터
places = {
    "바르셀로나": {
        "location": [41.3851, 2.1734],
        "description": "가우디의 도시, 사그라다 파밀리아와 구엘 공원이 유명합니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/e7/Sagrada_Familia_01.jpg"
    },
    "마드리드": {
        "location": [40.4168, -3.7038],
        "description": "스페인의 수도, 프라도 미술관과 레티로 공원을 방문해보세요.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Palacio_de_Comunicaciones_-_07.jpg"
    },
    "세비야": {
        "location": [37.3891, -5.9845],
        "description": "플라멩코의 본고장, 세비야 대성당과 히랄다탑이 인상적입니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/a/a9/La_Giralda.jpg"
    },
    "그라나다": {
        "location": [37.1773, -3.5986],
        "description": "알함브라 궁전으로 유명한 안달루시아의 보석 같은 도시입니다.",
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Alhambra_1.jpg"
    },
}

# 지도 생성
map_center = [40.0, -3.7]
m = folium.Map(location=map_center, zoom_start=6)

# 마커 추가
for name, info in places.items():
    folium.Marker(
        location=info["location"],
        popup=name,
        tooltip=info["description"]
    ).add_to(m)

# 지도 출력
st.subheader("📍 여행지 지도")
st_data = st_folium(m, width=700, height=500)

# 선택한 장소 표시
if st_data["last_object_clicked"]:
    clicked_location = st_data["last_object_clicked"]["lat"], st_data["last_object_clicked"]["lng"]
    
    # 선택된 위치와 가장 가까운 도시 찾기
    def distance(loc1, loc2):
        return ((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)**0.5

    closest = None
    min_dist = float('inf')
    for name, info in places.items():
        d = distance(clicked_location, info["location"])
        if d < min_dist:
            min_dist = d
            closest = name

    # 해당 도시 정보 출력
    place = places[closest]
    st.subheader(f"📌 {closest}")
    st.write(place["description"])
    st.image(place["image"], use_column_width=True)
