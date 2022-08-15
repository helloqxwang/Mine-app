import streamlit as st
import Data_Munging
def home_UI():
    '''
    this is the UI of the home page
    :return: Nome
    '''
    st.title("😛  Welcome to the App of Wang's")
    st.title('')
    st.subheader('''
    Attention！！！
    按照计划执行\n
    不要着急\n
    数分、高代每天不要落下\n
    ''')
    st.write(st.session_state)
    record = Data_Munging.fetchAllRecord()
    st.write(record)