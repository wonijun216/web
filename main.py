import streamlit as st
import folium
from streamlit_folium import st_folium
import random

# --- 여행지 데이터 ---
places = {
    "바르셀로나": {
        "location": [41.3851, 2.1734],
        "description": "🎨 예술과 건축의 도시, 가우디의 사그라다 파밀리아와 구엘 공원을 꼭 보세요!",
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/e7/Sagrada_Familia_01.jpg"
    },
    "마드리드": {
        "location": [40.4168, -3.7038],
        "description": "🏛️ 왕궁, 프라도 미술관, 그리고 활기찬 그랑비아 거리까지!",
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/5f/Palacio_de_Comunicaciones_-_07.jpg"
    },
    "세비야": {
        "location": [37.3891, -5.9845],
        "description": "💃 플라멩코의 고향, 알카사르 궁전과 세비야 대성당이 매력적이에요!",
        "image": "https://upload.wikimedia.org/wikipedia/commons/a/a9/La_Giralda.jpg"
    },
    "그라나다": {
        "location": [37.1773, -3.5986],
        "description": "🏰 알함브라 궁전이 있는 동화 같은 도시!",
        "image": "https://upload.wikimedia.org/wikipedia/commons/d/d3/Alhambra_1.jpg"
    },
}

# --- 페이지 타이틀 ---
st.markdown("<h1 style='color:#C71585;'>🇪🇸 ¡Bienvenido! 스페인 여행 가이드</h1>", unsafe_allow_html=True)
st.markdown("스페인의 아름다운 도시들을 지도와 함께 흥미롭게 알아보세요!")

# --- 랜덤 추천 여행지 ---
st.subheader("🎲 오늘의 랜덤 추천 도시")
random_place = random.choice(list(places.keys()))
info = places[random_place]
st.success(f"**{random_place}**: {info['description']}")
st.image(info['image'], caption=random_place, use_column_width=True)

st.markdown("---")

# --- 선택 도시 설명 섹션 ---
st.subheader("🌍 여행하고 싶은 도시를 선택해보세요!")
selected = st.selectbox("도시를 선택하세요", list(places.keys()))

if selected:
    st.image(places[selected]["image"], use_column_width=True, caption=selected)
    st.info(places[selected]["description"])

st.markdown("---")

# --- Folium 지도 ---
st.subheader("🗺️ 스페인 여행지 지도 보기")
map_center = [40.0, -3.7]
m = folium.Map(location=map_center, zoom_start=6)

for name, info in places.items():
    folium.Marker(
        location=info["location"],
        popup=f"<b>{name}</b><br>{info['description']}",
        tooltip=name,
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(m)

st_data = st_folium(m, width=700, height=500)

# --- 클릭한 도시 정보 표시 ---
if st_data["last_object_clicked"]:
    clicked_location = st_data["last_object_clicked"]["lat"], st_data["last_object_clicked"]["lng"]
    
    def distance(loc1, loc2):
        return ((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)**0.5

    closest = min(places.keys(), key=lambda name: distance(clicked_location, places[name]["location"]))
    place = places[closest]
    st.subheader(f"📍 지도에서 선택한 도시: {closest}")
    st.write(place["description"])
    st.image(place["image"], use_column_width=True)

# --- 퀴즈 (옵션) ---
with st.expander("❓ 스페인 여행지 퀴즈에 도전해볼래요?"):
    answer = st.radio("플라멩코 춤의 본고장은 어디일까요?", ("마드리드", "바르셀로나", "세비야", "그라나다"))
    if st.button("정답 확인"):
        if answer == "세비야":
            st.success("🎉 정답입니다! 세비야는 플라멩코의 본고장이에요.")
        else:
            st.error("😢 아쉬워요! 정답은 세비야입니다.")

