# [ 출처 ] ---------------------------------------------------------------------------------
# https://blog.zarathu.com/posts/2023-02-01-streamlit/#streamlit-%EC%86%8C%EA%B0%9C

import streamlit as st
from PIL import Image

# [ 사이드바 영역 ] ---------------------------------------------------------------------------------
st.sidebar.title('1. 슬라이드 컨트롤')

slider_range = st.sidebar.slider( "범위를 선택하세요", 0, 10, (0, 10) ) # 기본값, 앞 뒤로 2개 설정 /  하나만 하는 경우 value=2.5 이런 식으로 설정가능

st.sidebar.title('2. 드롭다운 리스트')

select_species = st.sidebar.selectbox( '확인하고 싶은 종을 선택하세요', ['setosa','versicolor','virginica'] )

select_multi_species = st.sidebar.multiselect( '확인하고 싶은 종을 선택하세요. 복수선택', ['setosa','versicolor','virginica'] )
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
st.title('DX Level2 과제')
#st.header('헤더 메시지 입니다')
#st.subheader('서브헤더 메시지 입니다')
st.write("주요 결과물 입니다")
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다. 
tab1, tab2= st.tabs(['① Topic Modeling' , '② Image Analytics'])
test_img = Image.open('orange_text.png')

with tab1:
  st.write('hello')
#    st.image(test_img)
    
with tab2:
  st.write('hi')
#----------------------------------------------------------------------------------------------------
