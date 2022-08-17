import streamlit as st
import Data_Munging
from streamlit_lottie import st_lottie
from streamlit_lottie import st_lottie_spinner
from io import StringIO
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
    this is the UI of home page
    :return: Nome
    '''
    hour = time.strftime('%H')
    daytime = ''
    if hour >= '6' and hour <='11':
        daytime='Good Morning!'
    elif hour > '11' and hour <='13':
        daytime='Good Noon!'
    elif hour >'13' and hour <='19':
        daytime='Good Afternoon!'
    elif hour > '19' and hour <= '22':
        daytime='Good Night!'
    else :
        daytime='Go to sleep!'

    # The following is concerned about how add animation to the page.
    # lottie_url_hello = "https://assets4.lottiefiles.com/packages/lf20_7psw7qge.json"
    # lottie_hello = load_lottieurl(lottie_url_hello)
    # st_lottie(lottie_hello, key="hello",loop=False,height=100,width=100)
    st.markdown('''
        # %s  St.Wang 🙂
    ''' % daytime)
    tab1, tab2, tab3 = st.tabs(['Attention', 'Edit it!', 'Upload one'])
    attention = Data_Munging.fetch_md_att_from_data()
    content = tab1.markdown('''
      ## No Attentions!   
      # enjoy you life!😃
                    ''')
    if attention is not None:
        content.markdown(attention)
    with tab2:
        form = st.form("text input")
        with form:
            text_content = st.text_area("Write your attention!",
                                        Data_Munging.fetch_md_att_from_data(),
                                        key='attention_content', height=400)
            submitted = st.form_submit_button(label="Update!")
        if submitted:
            text = st.session_state['attention_content']
            if text is None or text == '' or text == 'None':
                content.markdown('''
                      ## No Attentions!   
                      # enjoy you life!😃
                                    ''')
            else:
                content.markdown(text)
            Data_Munging.write_md_att_from_data(st.session_state['attention_content'])
    with tab3:
        st.file_uploader("Choose a file",key='uploaded_file')
        if st.session_state['uploaded_file'] is not None:
            uploaded_file=st.session_state['uploaded_file']
            bytes_data = uploaded_file.getvalue()
            # To convert to a string based IO:
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            # To read file as string:
            string_data = stringio.read()
            Data_Munging.write_md_att_from_data()