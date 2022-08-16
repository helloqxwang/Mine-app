import streamlit as st
import numpy as np
import pandas as pd
import datetime as dt
import Home_Page
import Data_Munging
import Schedule_Page
import TodayItem


st.set_page_config(
    page_title="Student Wang's page",
    page_icon="😛",
    initial_sidebar_state="expanded"
)
st.session_state["classify_Items"]=[]
df = pd.DataFrame({'item': [],'PS': []})
PAGES = [
    'Home',
    'Schedule',
    'What have been done today',
    'Self-analysis'
]
st.sidebar.title("WWWelcome!😃")
st.sidebar.markdown('''
    This is a **test app** made by student Wang.
    Hope this tool can make him a better life ***PPPLEASE!!!***
''')
page = st.sidebar.radio('Navigation', PAGES, index=0)
if page == 'What have been done today':
    st.sidebar.write("""
           ## About

        Record your day!
           """)
    TodayItem.todayItemUI()
if page=='Home':
    st.sidebar.write("""
               ## About

            Welcome to the home page!
               """)
    Home_Page.home_UI()
if page=='Schedule':
    st.sidebar.markdown("""
                   ## About

                Welcome to the schedule page!
                This page is designed to do *two things*
                - upload a schedule as a md file
                - write a schedule directly in this page(not done yet)
                   """)
    Schedule_Page.schedule_UI()



# from gsheetsdb import connect
# Create a connection object.
# conn = connect()
# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
# @st.cache(ttl=600)
# def run_query(query):
#     rows = conn.execute(query, headers=1)
#     rows = rows.fetchall()
#     return rows
# sheet_url="https://docs.google.com/spreadsheets/d/1d8QhjQ7zH1dZLDoFYX3LcGKwsvNkH97qGJci_fP2qzc/edit?usp=sharing"
# rows = run_query(f'SELECT * FROM "{sheet_url}"')


