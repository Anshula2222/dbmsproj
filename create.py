import streamlit as st
from database import add_data_user_account
from database import add_profile_info
from database import add_feedback
from database import add_pref
from database import add_photo

def create(table):
    if table=='User':
        #col1, col2 = st.columns(2)
        with col1:
            Uname = st.text_input("Uname:")
            Fname = st.text_input("Fname:")
            Lname =  st.text_input("Lname:")
            Gender =  st.text_input("Gender:")
            Mail =  st.text_input("Mail:")
            Age =  st.text_input("Age:")
            Phone =  st.text_input("Phone:")


        if st.button("Add data"):
            add_data_user_account(Fname, Lname, Mail, Gender, Age, Phone, Uname)
            st.success("Successfully Registered : {}".format(Uname))

    elif table=='Profile':
        col1, col2 = st.columns(2)
        with col1:
            Uname = st.text_input("Uname:")
            Gender = st.text_input("Gender:")
            Age =  st.text_input("Age:")
            Height = st.text_input("Height:")

        with col2:
            Religion = st.text_input("Religion:")
            Job = st.text_input("Job:")
            Nationality = st.text_input("Nationality:")
            Mothertongue =  st.text_input("Mothertongue:")
        if st.button("Add data"):
            add_profile_info(Uname, Gender, Age, Height, Religion, Job, Nationality, Mothertongue)
            st.success("Successfully added : {}".format(Uname))

    elif table == 'Prefrences':
        col1, col2 = st.columns(2)
        with col1:
            Uname = st.text_input("Uname:")
            Gender = st.text_input("Gender:")
            Age =  st.text_input("Age:")
            Height = st.text_input("Height:")
        with col2:
            Religion = st.text_input("Religion:")
            Job = st.text_input("Job:")
            Nationality = st.text_input("Nationality:")
            Mothertongue =  st.text_input("Mothertongue:")
        if st.button("Add data"):
            add_pref(Uname, Gender, Age, Height, Religion, Job, Nationality, Mothertongue)
            st.success("Successfully added : {}".format(Uname))
            
    elif table == 'Feedback':
        #col1, col2 = st.columns(2)
        Uname = st.text_input("Uname:")
        Feedback = st.text_input("Feedback:")
        if st.button("Add data"):
            add_feedback(Uname,Feedback)
            st.success("Successfully added : {}".format(Uname))



'''
    elif table == 'Photos':
        #col1, col2 = st.columns(2)
        with col1:
            Pid = st.text_input("Pid")
            Uname = st.text_input("Uname:")
        if st.button("Add data"):
            add_photo(prom_id,usr_id,transactions_no,duration,amount_value)
            st.success("Successfully added : {}".format(prom_id))'''

    