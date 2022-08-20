import streamlit as st
import Data_Munging
import datetime as dt
import streamlit_ace
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
