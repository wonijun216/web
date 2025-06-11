import streamlit as st
import random

st.set_page_config(page_title="오늘 뭐 먹지?", page_icon="🍽️")

# --- 제목 및 소개 ---
st.markdown("<h1 style='text-align:center; color:#FF6347;'>🍽️ 오늘 뭐 먹지?</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>식사 메뉴가 고민될 때! 당신에게 딱 맞는 메뉴를 추천해드려요 😋</h4>", unsafe_allow_html=True)
st.markdown("---")

# --- 음식 종류별 데이터 ---
menu_db = {
    "한식": [
        ("김치찌개", "https://cdn.pixabay.com/photo/2023/02/04/12/30/kimchi-stew-7766636_960_720.jpg"),
        ("불고기", "https://cdn.pixabay.com/photo/2022/11/26/07/44/bulgogi-7618684_960_720.jpg"),
        ("비빔밥", "https://recipe1.ezmember.co.kr/cache/recipe/2015/06/18/3a432b90f1c5d6ffbe688927f7e4a02b1.jpg"),
        ("된장찌개", "https://recipe1.ezmember.co.kr/cache/recipe/2017/02/07/5aa5d34e1739fa09aa1b28a8de7b33fb1.jpg")
    ],
    "중식": [
        ("짜장면", "https://recipe1.ezmember.co.kr/cache/recipe/2020/06/23/2026cd3f43176c4cc3d823372ee0b2d11.jpg"),
        ("탕수육", "https://cdn.pixabay.com/photo/2020/12/02/10/38/sweet-and-sour-pork-5794721_960_720.jpg"),
        ("마파두부", "https://cdn.pixabay.com/photo/2021/02/02/12/08/mapo-tofu-5974609_960_720.jpg"),
        ("볶음밥", "https://cdn.pixabay.com/photo/2016/03/05/19/02/abstract-1238247_960_720.jpg")
    ],
    "일식": [
        ("초밥", "https://cdn.pixabay.com/photo/2017/05/07/08/56/sushi-2292953_960_720.jpg"),
        ("돈카츠", "https://cdn.pixabay.com/photo/2020/09/07/01/22/japanese-food-5551314_960_720.jpg"),
        ("우동", "https://cdn.pixabay.com/photo/2017/04/25/11/28/udon-2268805_960_720.jpg"),
        ("규동", "https://cdn.pixabay.com/photo/2022/03/11/14/01/food-7061411_960_720.jpg")
    ],
    "양식": [
        ("파스타", "https://cdn.pixabay.com/photo/2015/04/08/13/13/food-712665_960_720.jpg"),
        ("스테이크", "https://cdn.pixabay.com/photo/2016/03/05/19/02/abstract-1238247_960_720.jpg"),
        ("햄버거", "https://cdn.pixabay.com/photo/2014/10/23/18/05/burger-500054_960_720.jpg"),
        ("피자", "https://cdn.pixabay.com/photo/2017/12/09/08/18/pizza-3007395_960_720.jpg")
    ]
}

# --- 사용자 선택 ---
meal_time = st.radio("🍴 지금은 언제인가요?", ["아침", "점심", "저녁"], horizontal=True)
food_type = st.selectbox("🍱 어떤 음식을 먹고 싶나요?", list(menu_db.keys()))

# --- 추천 함수 ---
def recommend_menu(food_type):
    return random.choice(menu_db[food_type])

# --- 추천 결과 표시 ---
if st.button("✨ 메뉴 추천받기!"):
    menu, image_url = recommend_menu(food_type)
    st.success(f"오늘의 추천 메뉴는 👉 **{menu}** 입니다!")
    st.image(image_url, use_container_width=True, caption=f"{menu}")
else:
    st.info("원하는 음식 종류를 선택하고 버튼을 눌러주세요 😊")

st.markdown("---")

# --- 푸터 ---
st.markdown("<p style='text-align:center; font-size:13px;'>© 2025 오늘 뭐 먹지? | 스트림릿으로 만든 간단한 추천 서비스</p>", unsafe_allow_html=True)
