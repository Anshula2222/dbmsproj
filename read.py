import pandas as pd
import streamlit as st
import plotly.express as px

from database import view_all_user_account
from database import view_all_profile
from database import view_all_pref
from database import view_all_photos
from database import view_all_feedback





def read(table):
    if table=='User':
        result = view_all_user_account()
        # st.write(result)
        df = pd.DataFrame(result, columns=['Fname', 'Lname', 'Mail', 'Gender', 'Age', 'Phone', 'Uname'])
        with st.expander("View all user_accounts"):
            st.dataframe(df)


    elif table=='Profile':
        result = view_all_profile()
        # st.write(result)
        df = pd.DataFrame(result, columns=['Uname', 'Gender', 'Age', 'Height', 'Religion', 'Job', 'Nationality', 'Mothertongue'])
        with st.expander("View all Profiles"):
            st.dataframe(df)
            '''
        with st.expander("user Bank_name"):
            task_df = df['bank_name'].value_counts().to_frame()
            task_df = task_df.reset_index()
            st.dataframe(task_df)
            p1 = px.pie(task_df, names='index', values='bank_name')
            st.plotly_chart(p1)'''

    elif table=='Prefrence':
        result = view_all_pref()
        # st.write(result)
        df = pd.DataFrame(result, columns=['Uname', 'Gender', 'Age', 'Height', 'Religion', 'Job', 'Nationality', 'Mothertongue'])
        with st.expander("View all Prefrences"):
            st.dataframe(df)
        '''
        with st.expander("user promos"):
            task_df = df['usr_id'].value_counts().to_frame()
            task_df = task_df.reset_index()
            st.dataframe(task_df)
            p1 = px.pie(task_df, names='index', values='usr_id')
            st.plotly_chart(p1)'''


    elif table=='Photos':
        result = view_all_photos()
        # st.write(result)
        df = pd.DataFrame(result, columns=['transaction_id', 'transaction_date','transaction_detail', 'amount','to_id','from_id','type_trans'])
        with st.expander("View all transactions"):
            st.dataframe(df)


    elif table=='Feedback':
        result = view_all_feedback()
        # st.write(result)
        df = pd.DataFrame(result, columns=['Uname','Feedback'])
        with st.expander("View all feedbacks"):
            st.dataframe(df)
        '''
        with st.expander("user promos"):
            task_df = df['user_id'].value_counts().to_frame()
            task_df = task_df.reset_index()
            st.dataframe(task_df)
            p1 = px.pie(task_df, names='index', values='user_id')
            st.plotly_chart(p1)'''

'''
    elif table=='Feedback':
        result = view_all_data_dependents()
        # st.write(result)
        df = pd.DataFrame(result, columns=['dependent_id','trans_id','user_ref_id','fname','lname','phone' ,'email' ,'dob','relation'])
        with st.expander("View all dependents"):
            st.dataframe(df)
        


    elif table=='transaction_status':
        result = view_all_data_transaction_status()
        # st.write(result)
        df = pd.DataFrame(result, columns=['trans_id','u_id','status'])
        with st.expander("View all status"):
            st.dataframe(df)'''
        

