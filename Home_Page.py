import streamlit as st
import Data_Munging
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import time
import requests
def home_UI():
    '''
    this is the UI of the home page
    :return: Nome
    '''
    st.title("😛  Welcome to the App of Wang's")
    st.markdown('''
        
    ''')

    def load_lottieurl(url: str):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    lottie_url_hello = "https://assets4.lottiefiles.com/packages/lf20_7psw7qge.json"
    lottie_hello = load_lottieurl(lottie_url_hello)
    st_lottie(lottie_hello, key="hello",loop=False,height=100,width=100)

    tab1,tab2,tab3=st.tabs(['Today\' schedule','Pay Attention！','data for test'])
    with tab1:
        schedule=Data_Munging.fetch_md_schedule()
        st.markdown(schedule)
    with tab2:
        st.subheader('''
        Attention！！！
        按照计划执行\n
        不要着急\n
        数分、高代每天不要落下\n
        ''')
    with tab3:
        st.write(st.session_state)
        record = Data_Munging.fetchAllRecord()
        st.write(record)