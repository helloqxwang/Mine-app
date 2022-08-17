import streamlit as st
import Data_Munging
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
import time
import requests

def load_lottieurl(url: str):
    '''
    this function is used to create animations
    :param url:
    :return:
    '''
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
def home_UI():
    '''
    # Good
    :return: Nome
    '''
    mytime = time.localtime()
    daytime = ''
    if mytime.tm_hour >= 6 and mytime.tm_hour <=11:
        daytime='Good Morning!'
    elif mytime.tm_hour > 11 and mytime.tm_hour <=13:
        daytime='Good Noon!'
    elif mytime.tm_hour >13 and mytime.tm_hour <=19:
        daytime='Good Afternoon!'
    elif mytime.tm_hour >19 and mytime.tm_hour <=22:
        daytime='Good Night!'
    else :
        daytime='Go to sleep!'

    # lottie_url_hello = "https://assets4.lottiefiles.com/packages/lf20_7psw7qge.json"
    # lottie_hello = load_lottieurl(lottie_url_hello)
    # st_lottie(lottie_hello, key="hello",loop=False,height=100,width=100)
    st.markdown('''
        # %s  St.Wang 🙂
    '''%daytime)

    tab1,tab2=st.tabs(['Pay Attention！','data for test'])
    with tab1:
        st.subheader('''
        Attention！！！
        按照计划执行\n
        不要着急\n
        数分、高代每天不要落下\n
        ''')
    with tab2:
        st.write(st.session_state)