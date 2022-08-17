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
    st.date_input('Select one date.',key='schedule_date')
    # this is the three tabs in this page
    tab1, tab2,tab3 = st.tabs(['My Schedule', 'Edit it!','Upload one'])
    page=UI_Class.md_show_edit(tab1,tab2,'schedule',st.session_state['schedule_date'])
    page.show()
    with tab3:
        st.file_uploader("Choose a file",key='uploaded_file')
        if st.session_state['uploaded_file'] is not None:
            uploaded_file=st.session_state['uploaded_file']
            bytes_data = uploaded_file.getvalue()
            # To convert to a string based IO:
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            # To read file as string:
            string_data = stringio.read()
            Data_Munging.write_md_to_deta('schedule',string_data)
