import streamlit as st
import numpy as np
import pandas as pd
import datetime as dt
import UI_Class
import Data_Munging
from io import StringIO

def record_page_ui():
    '''
    this is the UI of the record_page
    :return:
    '''
    st.markdown('''
            # This is where I record my life.
        ''')
    st.date_input('Select one date.', key='record_date')
    # this is the three tabs in this page
    tab1, tab2, tab3 = st.tabs(['What\'s up?', 'Edit it!', 'Upload one'])
    page = UI_Class.md_show_edit(tab1, tab2, 'record', st.session_state['record_date'])
    page.show()
    with tab3:
        st.file_uploader("Choose a file", key='uploaded_file')
        if st.session_state['uploaded_file'] is not None:
            uploaded_file = st.session_state['uploaded_file']
            bytes_data = uploaded_file.getvalue()
            # To convert to a string based IO:
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            # To read file as string:
            string_data = stringio.read()
            Data_Munging.write_md_to_deta('record', string_data)
