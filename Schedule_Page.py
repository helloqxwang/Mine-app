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
    def update_tab1(data):
        '''
        this function is used to update the schedule in tab1 after edit it
        :return: None
        '''
        if data is None:
            st.markdown('''
            ## Huh! You select a un-ordered day!
            ''')
        else:
            content.markdown(data)

    st.markdown('''
        # Remarkable! Doesn't it?
    ''')
    st.date_input('Select one date.',key='schedule_date')
    # this is the three tabs in this page
    tab1, tab2,tab3 = st.tabs(['My Schedule', 'Edit it!','Upload one'])
    with tab1:
        schedule = Data_Munging.fetch_md_schedule(st.session_state['schedule_date'])
        print(schedule)
        if schedule is None:
            st.markdown('''
            ## Huh! You select a un-ordered day!
            ''')
        else:
            content=st.markdown(schedule)
    with tab2:
        st.text_area("Write the schedule freely",Data_Munging.fetch_md_schedule(st.session_state['schedule_date']),
                     key='schedule_content',height=400)
        if st.session_state['schedule_content'] != 'None':
            print('teat_input is writting to the detabase')
            print(st.session_state['schedule_content'] )
            update_tab1(st.session_state['schedule_content'])
            Data_Munging.write_md_schedule(st.session_state['schedule_content'],st.session_state['schedule_date'])
    with tab3:
        st.file_uploader("Choose a file",key='uploaded_file')
        if st.session_state['uploaded_file'] is not None:
            uploaded_file=st.session_state['uploaded_file']
            bytes_data = uploaded_file.getvalue()
            # To convert to a string based IO:
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            # To read file as string:
            string_data = stringio.read()
            Data_Munging.write_md_schedule(string_data)
