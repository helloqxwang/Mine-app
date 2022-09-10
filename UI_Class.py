import streamlit as st
import Data_Munging
import datetime as dt
import streamlit_ace
from streamlit_elements import dashboard
import json
from io import StringIO
from pathlib import Path
from streamlit_elements import elements, sync, event
from types import SimpleNamespace
from dashboard import Dashboard, Editor, Card, DataGrid, Radar, Pie,Player

# this is the old version of the scheudle page.
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

    @staticmethod
    def set_the_ace(kind,date = None):
        st.subheader('Write your %s freely!' % kind)
        if date is None :
            input_content = streamlit_ace.st_ace(
                height=400,
                value=Data_Munging.fetch_md_att_from_data(),
                language='markdown',
                theme='twilight',
                font_size=17,
                key='ace_%s' % kind
            )
        else :
            input_content = streamlit_ace.st_ace(
                height=400,
                value=Data_Munging.fetch_md_from_deta(kind, date),
                language='markdown',
                theme='twilight',
                font_size=17,
                key='ace_%s' % kind
            )
        return input_content


    def show(self) ->None :
        schedule = Data_Munging.fetch_md_from_deta(self.kind,self.date)
        content=self.tab1.markdown('''
            ## Huh! You select a un-ordered day!
                ''')
        if schedule is not None:
            content.markdown(schedule)
        with self.tab2:
            c1, c2 = st.columns([1.5, 1])
            with c1:
                input = streamlit_ace.st_ace(
                    height=400,
                    value=Data_Munging.fetch_md_from_deta(self.kind, self.date),
                    language='markdown',
                    theme='twilight',
                    font_size=17,
                    key='ace_%s' % self.kind
                )
            if input:
                c2.subheader("MD Preview:")
                c2.markdown(input)
                Data_Munging.write_md_to_deta(self.kind, input, self.date)
                content.markdown(input)

class record_by_form:

    def add_the_class(self,new_class):
        '''
        this function is used to add a new class to the st.session_state["classify_Items"]
        :param new_class: a string to describe the new class
        :return: None
        '''
        if len(new_class) == 0:
            return
        st.session_state['classify_Items'].append(new_class)
        return

    def todayItemUI(self):
        """
        this is the UI function of this page
        :return: None
        """
        if len(st.session_state["classify_Items"]) == 0:
            st.session_state['classify_Items'] = ["数学分析", "高等代数", "cs", "cs for text", "运动"]
        st.title("Hey! What are you doing?🙂")
        st.title('')
        form = st.form("oneItem")
        with form:
            upcols = st.columns((1, 1))
            upcols[0].time_input("Start time!", key="start_time")
            upcols[1].time_input("End time!", key="end_time")
            st.radio("Are you Studying?🙃", ("Yep!", "Not now"), key="study_or_not", horizontal=True)
            st.text_input("Write you item for free!", key="item_name")
            st.multiselect("Classify it!", key="classify", options=st.session_state["classify_Items"])
            st.text_area("Comment:", key="item_comment")
            cols = st.columns((1, 1))
            cols[0].slider("🤓 or 🥱", 0, 5, 0, key="item_state")
            cols[1].slider("😝-ness", 0, 5, 0, key="item_happiness")
            submitted = st.form_submit_button(label="Submit")
        if submitted:
            # add_row_to_gsheet(
            #     gsheet_connector,
            #     [[author, bug_type, comment, str(date), bug_severity]],
            # )
            classify = ''
            for v in st.session_state["classify"]:
                if len(classify) != 0:
                    classify = classify + '/' + v
                else:
                    classify = v
            result = [st.session_state["start_time"], st.session_state["end_time"], st.session_state["item_name"],
                      classify, st.session_state["study_or_not"], st.session_state["item_comment"],
                      st.session_state["item_state"], st.session_state["item_happiness"]]
            Data_Munging.addOneItem(result)
            st.success("Ready to next item!")
            st.balloons()
            self.add_the_class(st.text_input("Create new class"))

class elements_test:

    def show(self):
        if "w" not in st.session_state:
            board = Dashboard()
            w = SimpleNamespace(
                dashboard=board,
                editor=Editor(board, 0, 0, 6, 11, minW=3, minH=3),
                player=Player(board, 0, 12, 6, 10, minH=5),
                pie=Pie(board, 6, 0, 6, 7, minW=3, minH=4),
                radar=Radar(board, 12, 7, 3, 7, minW=2, minH=4),
                card=Card(board, 6, 7, 3, 7, minW=2, minH=4),
                data_grid=DataGrid(board, 6, 13, 6, 7, minH=4),
            )
            st.session_state.w = w

            w.editor.add_tab("Card content", Card.DEFAULT_CONTENT, "plaintext")
            w.editor.add_tab("Data grid", json.dumps(DataGrid.DEFAULT_ROWS, indent=2), "json")
            w.editor.add_tab("Radar chart", json.dumps(Radar.DEFAULT_DATA, indent=2), "json")
            w.editor.add_tab("Pie chart", json.dumps(Pie.DEFAULT_DATA, indent=2), "json")
        else:
            w = st.session_state.w

        with elements("demo"):
            event.Hotkey("ctrl+s", sync(), bindInputs=True, overrideDefault=True)

            with w.dashboard(rowHeight=57):
                w.editor()
                w.player()
                w.pie(w.editor.get_content("Pie chart"))
                w.radar(w.editor.get_content("Radar chart"))
                w.card(w.editor.get_content("Card content"))
                w.data_grid(w.editor.get_content("Data grid"))

# this is a test class, using the mui.
class long_term_stuff_show:
    tab1 = None
    tab2 = None
    kind = ''
    date = None

    def __init__(self, t1, t2, k, d) -> None:
        self.tab1 = t1
        self.tab2 = t2
        self.kind = k
        self.date = d

    @staticmethod
    def set_the_ace(kind, date):
        st.subheader('Write your %s freely!' % kind)
        input_content = streamlit_ace.st_ace(
            height=400,
            value=Data_Munging.fetch_md_from_deta(kind, date),
            language='markdown',
            theme='twilight',
            font_size=17,
            key='ace_%s' % kind
        )
        return input_content

    def __call__(self):
        with self.tab1:
            c1, c2 = st.columns([3, 2])
            schedule = Data_Munging.fetch_md_from_deta(self.kind, self.date)
            content = c1.markdown('''
                            ## Huh! You select a un-ordered day!
                                ''')
            if schedule is not None:
                content.markdown(schedule)
            with c2:
                input = streamlit_ace.st_ace(
                    height=400,
                    value=Data_Munging.fetch_md_from_deta(self.kind, self.date),
                    language='markdown',
                    theme='twilight',
                    font_size=17,
                    key='ace_%s' % self.kind
                )
            if input:
                content.markdown(input)
                Data_Munging.write_md_to_deta(self.kind, input, self.date)
                content.markdown(input)
        with self.tab2:
            date_list=[]
            i=0
            dd=dt.date.today()
            while i<6:
                date_list.append(dd)
                dd = dd+dt.timedelta(days=1)
                i = i+1
            if "w" not in st.session_state:
                board = Dashboard()
                w = SimpleNamespace(
                    dashboard=board,
                    card2=Card(board, 0,0,0,0, minW=2, minH=4),
                    editor=Editor(board, 0, 0, 6, 11, minW=3, minH=3),
                    data_grid=DataGrid(board, 6, 13, 6, 7, minH=4),
                )
                st.session_state.w = w

                w.editor.add_tab("Card content", Card.DEFAULT_CONTENT, "plaintext")
            else:
                w = st.session_state.w
            # 从这里开始进行显示
            with elements("demo"):
                event.Hotkey("ctrl+s", sync(), bindInputs=True, overrideDefault=True)

                with w.dashboard(rowHeight=70):
                    w.editor()
                    #w.card(Data_Munging.fetch_md_from_deta(self.kind, date_list[1]))
                    w.card(Data_Munging.fetch_md_from_deta(self.kind, date_list[0]))
                    w.data_grid(w.editor.get_content("Data grid"))

# this class is used to display the schedule in recent 8 days.
# this class is also used to display the self-analysis.
# this class is used in the new_interface_sche_rec now.
class long_time_item_show:
    def __init__(self,kind,dd,bias=0,open=True):
        self.kind=kind
        self.date=dd+dt.timedelta(days=bias)
        self.expand=open

    def show_item(
            self,item,day, expanded= True
    ):
        with st.expander(day.isoformat(), expanded=expanded):
                st.markdown(item)

    def __call__(self):
        st.header("Recent 8 days")
        R8W_L, R8W_R = st.columns(2)
        dd = []
        for i in range(8):
            dd.append(self.date + dt.timedelta(days=i))
        item_list = [Data_Munging.fetch_md_from_deta(self.kind, d) for d in dd]
        with R8W_L:
            for i in range(0,8,2):
                self.show_item(item_list[i], dd[i])
        with R8W_R:
            for i in range(1, 8,2):
                self.show_item(item_list[i], dd[i])
        _, centering, _ = st.columns([3, 2, 3])
        with centering:
            if st.button("Update the page!"):
                st.experimental_rerun()

def set_the_md(kind,date):
    '''
            this function is used to construct a md_view to show the schedule stuff
            and have a button to change the page into a md
            :param kind:
            :param date:
            :return:
            '''
    mode = st.radio(
        "Read it or Edit it?",('read', 'edit'),horizontal=True)

    if mode == 'read':
        schedule = Data_Munging.fetch_md_from_deta(kind, date)
        content = st.markdown('''
                                                        ## Huh! You select a un-ordered day!
                                                            ''')
        if schedule is not None:
            content.markdown(schedule)
    else:
        input = streamlit_ace.st_ace(
            height=400,
            value=Data_Munging.fetch_md_from_deta(kind, date),
            language='markdown',
            theme='twilight',
            font_size=17,
            key='ace_%s' % kind
        )
        if input:
            Data_Munging.write_md_to_deta(kind, input, date)

# this class is used in schedule page now
class new_interface_sche_rec:
    kind=''

    def __init__(self,k):
        self.kind = k

    @staticmethod
    def set_the_ace(kind, date=None):
        st.subheader('Write your %s freely!' % kind)
        if date is None:
            input_content = streamlit_ace.st_ace(
                height=400,
                value=Data_Munging.fetch_md_att_from_data(),
                language='markdown',
                theme='twilight',
                font_size=17,
                key='ace_%s' % kind
            )
        else:
            input_content = streamlit_ace.st_ace(
                height=400,
                value=Data_Munging.fetch_md_from_deta(kind, date),
                language='markdown',
                theme='twilight',
                font_size=17,
                key='ace_%s' % kind
            )
        return input_content

    def __call__(self,*args):
        st.date_input('Select one date.', key='date')
        # this is the three tabs in this page
        tab1, tab2, tab3 = st.tabs(['My Schedule', 'Recent 8 days', 'Upload one'])
        date=st.session_state['date']
        with tab1:
            set_the_md(self.kind,st.session_state['date'])
        with tab2:
            page=long_time_item_show('schedule',st.session_state['date'])
            page()
        with tab3:
            st.file_uploader("Choose a file", key='uploaded_file')
            if st.session_state['uploaded_file'] is not None:
                uploaded_file = st.session_state['uploaded_file']
                bytes_data = uploaded_file.getvalue()
                # To convert to a string based IO:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                # To read file as string:
                string_data = stringio.read()
                Data_Munging.write_md_to_deta('schedule', string_data)

# this is the self-analysis page
class self_analysis_calss:
    def __call__(self,*args):
        st.date_input('Select one date.', key='date')
        # this is the three tabs in this page
        tab1, tab2, tab3 = st.tabs(['Recent 8 days', 'Today\'s analysis', 'Upload one'])
        date=st.session_state['date']
        with tab1:
            page = long_time_item_show('analysis',st.session_state['date'],-7)
            page()
        with tab2:
            input = streamlit_ace.st_ace(
                height=400,
                value=Data_Munging.fetch_md_from_deta('analysis', date),
                language='markdown',
                theme='twilight',
                font_size=17,
                key='ace_%s' % 'analysis'
            )
            if input:
                Data_Munging.write_md_to_deta('analysis', input, date)
        with tab3:
            st.file_uploader("Choose a file", key='uploaded_file')
            if st.session_state['uploaded_file'] is not None:
                uploaded_file = st.session_state['uploaded_file']
                bytes_data = uploaded_file.getvalue()
                # To convert to a string based IO:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                # To read file as string:
                string_data = stringio.read()
                Data_Munging.write_md_to_deta('analysis', string_data)