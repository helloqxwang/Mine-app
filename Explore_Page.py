import datetime

import streamlit as st
import UI_Class

class explore_page:
    kind = ''
    def __init__(self):
        kind =''

    def show (self,k):
        # if(k=='elements'):
        #    page = UI_Class.elements_test()
        #    page.show()
        # elif(k=='long'):
        #     tab1 ,tab2 = st.tabs(['1','2'])
        #     page = UI_Class.long_term_stuff_show(tab1,tab2,'schedule',datetime.date.today())
        #     page()
        # else:
        #     st.markdown('''
        #     # there is not a page on %s now
        #     '''%k
     st.markdown("# this is a test area")
