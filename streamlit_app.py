# [ 출처 ] ---------------------------------------------------------------------------------
# https://blog.zarathu.com/posts/2023-02-01-streamlit/#streamlit-%EC%86%8C%EA%B0%9C

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

# [ 사이드바 영역 ] ---------------------------------------------------------------------------------
st.sidebar.title('데이터 수집 연도')
slider_range = st.sidebar.slider( "연도를 선택하세요", 2021, 2024, (2023, 2024) ) # 기본값, 앞 뒤로 2개 설정 /  하나만 하는 경우 value=2.5 이런 식으로 설정가능

st.sidebar.title('제품 항목')
select_species = st.sidebar.selectbox( '분석하려는 제품 카테고리', ['TV','AV'] )

st.sidebar.title('키워드')
select_species = st.sidebar.selectbox( '분석하려는 특정 키워드', ['game','outdoor','interior'] )

#select_multi_species = st.sidebar.multiselect( '확인하고 싶은 종을 선택하세요. 복수선택', ['setosa','versicolor','virginica'] )
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
#st.title('고객 VOC를 분석하여 인사이트를 도출하는 분석 과제')
#st.header('헤더 메시지 입니다')
st.subheader('고객 VOC를 분석하여 인사이트를 도출하는 분석 과제')
#----------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------
# 탭 생성 : 첫번째 탭의 이름은 Tab A 로, Tab B로 표시합니다. 
tab1, tab2= st.tabs(['① Topic Modeling' , '② webOS Log Analysis'])
#test_img = Image.open('orange_text.png')

with tab1:
  st.write('LDA (잠재 디리클레 할당) 방법을 이용해, VOC에서 주요한 토픽을 찾아 냄')

#    st.image(test_img)
  list = [
  ['TV','TV','mode','TV','TV','mode','TV','mode','TV','TV'],
  ['screen','mode','TV','very','no','TV','like','TV','watch','use'],
  ['LD','up','playing','play','input','some','HDMI','only','playing','playing'],
  ['very','picture','HDR','screen','lag','settings','game','quality','play','play'],
  ['play','black','settings','sound','doesnt','PC','all','picture','mode','good'],
  ['playing','setting','out','more','like','like','use','if','pictire','screen'],
  ['video','screen','looks','mode','dark','no','PS5','play','like','HDR'],
  ['PS5','VRR','after','get','some','color','work','video','very','video']
  ]
  df = pd.DataFrame(list, columns=["토픽1", "토픽2", "토픽3", "토픽4", "토픽5", "토픽6", "토픽7", "토픽8", "토픽9", "토픽10"])
  st.table(df)

  st.subheader('주요 인사이트')
  st.write('1. Topic 1 ~ Topic 10 공통 : "TV에서 게임을 할 때 mode 설정에 문제가 있음" ')
  st.write('2. Topic 2 : "화면이 검게 보이는 문제가 있음" ')
  st.write('3. Topic 5 : "입력시 지연이 문제가 됨" ')
  st.write('4. Topic 7 : "콘솔게임이 연결시 HDMI 연결에 문제" ')

with tab2:
  st.write('webOS의 해당 USP의 대당 사용빈도의 시계열 데이터를 분석함')

#----------------------------------------------------------------------------------------------------
