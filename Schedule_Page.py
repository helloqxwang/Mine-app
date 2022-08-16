from io import StringIO

import streamlit as st

import Data_Munging
def schedule_UI():
    """
    this is the UI fuction of schedule page
    :return: None
    """
    # st.date_input("Which day do you want to see?",key='date_of_schedule')
    # st.write(Data_Munging.fetch_schedule(st.session_state['date_of_schedule']))
    st.markdown('''
        # NOT DONE YET!:sunny:
    ''')
    st.file_uploader("Choose a file",key='uploaded_file')
    if st.session_state['uploaded_file'] is not None:
        uploaded_file=st.session_state['uploaded_file']
        bytes_data = uploaded_file.getvalue()
        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        # To read file as string:
        string_data = stringio.read()
        Data_Munging.write_md_schedule(string_data)