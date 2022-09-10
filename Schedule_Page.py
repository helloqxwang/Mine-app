from io import StringIO
import datetime as dt
import streamlit as st
import UI_Class
import Data_Munging

def schedule_UI():
    """
    this is the UI fuction of schedule page
    :return: None
    """
    # st.date_input("Which day do you want to see?",key='date_of_schedule')
    # st.write(Data_Munging.fetch_schedule(st.session_state['date_of_schedule']))

    st.markdown('''
        # This is where I plan my life.
    ''')
    page = UI_Class.new_interface_sche_rec('schedule')
    page()