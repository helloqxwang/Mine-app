import pandas as pd
import datetime as dt
import os
import streamlit as st

recordPlace="Data/Record/ItemDoneEachDay.csv"
def fetchAllRecord(date=dt.datetime.today().date()):
    """
    this function is used to fetch all Records for one day
    :param date: the date of the Records
    :return: a dataframe from the csv file
    """
    fileName = "Data/Record/"+date.isoformat()+"_Record.csv"
    df=pd.read_csv(fileName)
    return df

def addOneItem(data):
    """
    this function is used to add one item to today's record
    if the record is not set up yet, it will set up it.
    :param data: a list containing all the information of the Item
    :return: None
    """
    today= dt.datetime.today().date()
    fileName = "Data/Record/"+today.isoformat()+"_Record.csv"
    if not os.path.exists(fileName):
        os.system(r'touch %s' %fileName)
        dataFrame = pd.DataFrame(columns=['start_time','end_time', 'item_id','classify','happy or not', 'comment','state','happiness'],index=[])
        dataFrame.to_csv(fileName,index=False,encoding = 'utf_8_sig')
        st.session_state['Item_number'] = 0
    df=pd.read_csv(fileName)
    #st.session_state['Item_number'] +=1
    print(len(data))
    print(df.shape)
    df.loc[df.shape[0]]=data
    df.to_csv(fileName,index=False,encoding = 'utf_8_sig')
    return

def fetch_schedule(date):
    '''
    this is a function to fetch the schedule of a certain day
    :param date: the date of the schedule fetched
    :return: a dataframe containing the Schedule in the date
    '''
    fileName = "Data/Schedule/"+date.isoformat()+"_Schedule.csv"
    df = pd.read_csv(fileName)
    return df