import streamlit as st
import numpy as np
import pandas as pd
import datetime as dt

import Data_Munging

def add_the_class(new_class):
    '''
    this function is used to add a new class to the st.session_state["classify_Items"]
    :param new_class: a string to describe the new class
    :return: None
    '''
    if len(new_class)==0:
        return
    st.session_state['classify_Items'].append(new_class)
    return


def todayItemUI():
    """
    this is the UI function of this page
    :return: None
    """
    if len(st.session_state["classify_Items"])==0:
        st.session_state['classify_Items'] = ["数学分析", "高等代数", "cs","cs for text","运动"]
    st.title("Hey! What are you doing?🙂")
    st.title('')
    form = st.form("oneItem")
    with form:
        upcols=st.columns((1,1))
        upcols[0].time_input("Start time!",key="start_time")
        upcols[1].time_input("End time!",key="end_time")
        st.radio("Are you Studying?🙃", ("Yep!", "Not now"), key="study_or_not",horizontal=True)
        st.text_input("Write you item for free!",key="item_name")
        st.multiselect("Classify it!",key="classify",options=st.session_state["classify_Items"])
        st.text_area("Comment:",key="item_comment")
        cols = st.columns((1, 1))
        cols[0].slider("🤓 or 🥱", 0, 5, 0,key="item_state")
        cols[1].slider("😝-ness", 0, 5, 0,key="item_happiness")
        submitted = st.form_submit_button(label="Submit")
    if submitted:
        # add_row_to_gsheet(
        #     gsheet_connector,
        #     [[author, bug_type, comment, str(date), bug_severity]],
        # )
        classify=''
        for v in st.session_state["classify"]:
            if len(classify)!=0:
                classify=classify+'/'+v
            else:
                classify = v
        result = [st.session_state["start_time"],st.session_state["end_time"], st.session_state["item_name"],classify,st.session_state["study_or_not"],  st.session_state["item_comment"],st.session_state["item_state"],st.session_state["item_happiness"]]
        Data_Munging.addOneItem(result)
        st.success("Ready to next item!")
        st.balloons()

    add_the_class(st.text_input("Create new class"))
