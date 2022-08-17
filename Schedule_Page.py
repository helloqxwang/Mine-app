from io import StringIO
import datetime as dt
import streamlit as st

import Data_Munging
class md_show_edit:
    tab1 = None
    tab2 = None
    kind=''
    date = None
    def __init__(self,t1,t2,k,d) ->None :
        self.tab1=t1
        self.tab2=t2
        self.kind=k
        self.date=d
    def show(self) ->None :
        def update_tab1(data):
            '''
            this function is used to update the content in tab1 after editing it
            :return: None
            '''
            if data is None:
                st.markdown('''
                ## Huh! You select a un-ordered day!
                ''')
            else:
                content.markdown(data)

        with self.tab1:
            schedule = Data_Munging.fetch_md_schedule(self.date)
            print(schedule)
            if schedule is None:
                st.markdown('''
                ## Huh! You select a un-ordered day!
                ''')
            else:
                content = st.markdown(schedule)
        with self.tab2:
            form = st.form("text input")
            with form:
                text_content = st.text_area("Write the %s freely"%(self.kind),
                                            Data_Munging.fetch_md_schedule(self.date),
                                            key='the_content', height=400)
                submitted = st.form_submit_button(label="Update!")
            if submitted:
                print('teat_input is written to the detabase')
                # st.write(st.session_state['schedule_content'])
                update_tab1(st.session_state['the_content'])
                # st.write(st.session_state['schedule_content'])
                Data_Munging.write_md_schedule(st.session_state['the_content'], self.date)
                # st.write(st.session_state['schedule_content'])


def schedule_UI():
    """
    this is the UI fuction of schedule page
    :return: None
    """
    # st.date_input("Which day do you want to see?",key='date_of_schedule')
    # st.write(Data_Munging.fetch_schedule(st.session_state['date_of_schedule']))

    st.markdown('''
        # Remarkable! Doesn't it?
    ''')
    st.date_input('Select one date.',key='schedule_date')
    # this is the three tabs in this page
    tab1, tab2,tab3 = st.tabs(['My Schedule', 'Edit it!','Upload one'])
    page=md_show_edit(tab1,tab2,'schedule',st.session_state['schedule_date'])
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
            Data_Munging.write_md_schedule(string_data)
