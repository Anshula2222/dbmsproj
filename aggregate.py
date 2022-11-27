import streamlit as st
import pandas as pd
from database import aggregate_2
from database import aggregate
#from database import aggregate_3
#from database import aggregate_4
from database import add_feedback

def agg():
    def create(table):
        if table=='Feedback':
            Uname = st.text_input("Uname")
            Feedback= st.text_input("Feedback")
            if st.button("Add data"):
                add_feedback(Uname,Feedback)

    '''if st.button('Display Bank Count'):
        df=pd.DataFrame(aggregate(),columns=['Bank_Name','Count'])
        st.dataframe(df)'''
    
    if st.button('Total Feedbacks Recieved'):
        df=pd.DataFrame(aggregate(),columns=['Feedback','Total Amount'])
        st.dataframe(df)
    if st.button('Display Average rating'):
        df=pd.DataFrame(aggregate_2(),columns=['Average'])
        st.dataframe(df)
    '''if st.button('Display Max amount'):
        df=pd.DataFrame(aggregate_2(),columns=['First Name','Amount'])
        st.dataframe(df)'''