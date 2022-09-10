import streamlit as st
import numpy as np
import pandas as pd
import datetime as dt
import Home_Page
import Schedule_Page
import Record_Page
import Self_Analysis_Page
import Explore_Page
st.set_page_config(
    page_title="Student Wang's page",
    page_icon="😍",
    initial_sidebar_state="auto",
    layout='wide'
)
PAGES = [
    'Home',
    'Schedule',
    'Record and Memo',
    'Self-analysis',
    'Explore'
]
st.sidebar.title("WWWelcome!😃")
st.sidebar.markdown('''
    This is a **test app** made by student Wang.
    Hope this tool can make him a better life ***PPPLEASE!!!***
''')
page = st.sidebar.radio('Navigation', PAGES, index=0)

site_about = st.sidebar.expander('Why I build this site')
with site_about:
    st.markdown('''
        ### This site is a sword.
        ### A sword I forge.
        ### A sword to kill INDULGENCE.   
        > ***Indulgence***, the evil, keep me from self-achievement endlessly. 
        > Nearly all the times when I stride forward singing militant songs, the indulgence drag me back 
        > ***creatively***  
        ### Indulgence, is exactly the rock of Sisyphus.


        ***The indulgence*** has disturbed me a lot ***but*** now I want to turn ***"has"*** to ***"had"***.  

        > ***However,*** unlike other challenge in life, this fucking problem can't be just attributed to envy, wrath, 
        > sloth, greed, gluttony, lust... 

        This is a ***time problem*** to a great content.  

        > In order word, I can figure out what I should and can't do sometime.  Frankly speaking, nealy most of the life.
        > However, in some time, I just forget the regret, anger, disappointment, and suffering last time,
        > *Rush into the abyss.*  
        ### In a word, **I just can't figure out then.**  
        ### **But 'then' counts**  
        > To defeat the problem, I write this site, determining **firmly** to hold **my** life in **my** hand.   
        # ***souhaite moi du succès***
    ''')

if page == 'Record and Memo':
    st.sidebar.write("""
           ## About
            Record you day!
            This page is designed to do ***three things***
            - check your record conveniently! 😍
            - update your record directly in this page!
            - upload a record in md!
           """)
    Record_Page.record_page_ui()
if page == 'Home':
    st.sidebar.write("""
               ## About
            Welcome to the home page!   
            This is the home page of my site.
            You can write yourself attentions and check then freely here.  
               """)
    Home_Page.home_UI()
if page == 'Schedule':
    st.sidebar.markdown("""
                   ## About

                Welcome to the schedule page!
                This page is designed to do ***three things***
                - check you schedule conveniently! 😍
                - write your schedule directly in this page!
                - upload your schedule in md!
                   """)
    Schedule_Page.schedule_UI()
if page == 'Self-analysis':
    show_page=Self_Analysis_Page.self_analysis_page()
    show_page.show()

if page == 'Explore':
    p = Explore_Page.explore_page()
    p.show('long')



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


