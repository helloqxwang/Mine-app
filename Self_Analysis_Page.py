import streamlit as st
import Data_Munging
from io import StringIO
import Data_Munging
import UI_Class

class self_analysis_page:
    def show(self):
        st.markdown('''
            # This is the test version~😄
        ''')
        page=UI_Class.self_analysis_calss()
        page()
