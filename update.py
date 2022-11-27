import datetime

import pandas as pd
import streamlit as st
from database import view_all_user_account
from database import view_all_profile
from database import view_all_pref


from database import view_only_user_account
from database import view_only_profile
from database import view_only_pref


from database import get_user_id
from database import get_tid
from database import get_transaction_id
from database import get_promo_id
from database import get_dependent_id
from database import get_trans_id
from database import get_prom_id

from database import edit_user_account_data
from database import edit_wallet_data
from database import edit_pref_data
from database import edit_promo_offers_data
from database import edit_dependents_data
from database import edit_transaction_status_data
from database import edit_promo_offers_transactions_data





def update(table):
    if table=='User':
        result = view_all_user_account()
        # st.write(result)
        df = pd.DataFrame(result, columns=['Fname', 'Lname', 'Mail', 'Gender', 'Age', 'Phone', 'Uname'])
        with st.expander("Current user_accounts"):
            st.dataframe(df)
        list_of_users = [i[0] for i in view_only_user_account()]
        selected_user = st.selectbox("user to Edit", list_of_users)
        selected_result = get_user_id(selected_user)
        # st.write(selected_result)
        if selected_result:
            Fname = selected_result[0][0]
            Lname = selected_result[0][1]
            Mail = selected_result[0][2]
            Gender = selected_result[0][3]
            Age = selected_result[0][4]
            Phone = selected_result[0][5]
            Uname = selected_result[0][6]
            # Layout of Create

            #col1, col2 ,col3= st.columns(3)
            #with col1:
            new_uname = st.text_input("Uname:",Uname)
            new_fname = st.text_input("Fname:", Fname)
            new_lname = st.text_input("Lname:", Lname)
            new_age = st.text_input("Age:", Age)
            new_mail= st.text_input("Mail:", Mail)
            new_gender= st.text_input("Gender:", Gender)
            new_phone= st.text_input("Phone:", Phone)
            '''
            with col2:
                new_phone = st.text_input("phone:",phone)
                new_email = st.text_input("email:",email)
                new_country = st.text_input("city:",country)
                new_city = st.text_input("city:",city)
                new_pincode = st.text_input("pincode:",pincode)
                new_bank_name = st.text_input("bank_name:",bank_name)'''
            if st.button("Update user_account"):
                edit_user_account_data(new_fname, new_lname, new_mail, new_gender, new_age, new_phone, new_uname,Fname, Lname, Mail, Gender, Age, Phone, Uname)
                st.success("Successfully updated:: {} to ::{}".format(Uname, new_uname))

        result2 = view_all_user_account()
        df2 = pd.DataFrame(result2, columns=['Fname', 'Lname', 'Mail', 'Gender', 'Age', 'Phone', 'Uname'])
        with st.expander("Updated data"):
            st.dataframe(df2)



    elif table=='Profile':
        result = view_all_profile()
        # st.write(result)
        df = pd.DataFrame(result, columns=['Uname', 'Gender', 'Age', 'Height', 'Religion', 'Job', 'Nationality', 'Mothertongue'])
        with st.expander("Current Profile"):
            st.dataframe(df)
        list_of_profiles = [i[0] for i in view_only_profile()]
        selected_profile = st.selectbox("user to Edit", list_of_profiles)
        selected_result = get_tid(selected_profile)
        # st.write(selected_result)
        if selected_result:
            Uname = selected_result[0][0]
            Gender = selected_result[0][1]
            Age = selected_result[0][2]
            Height = selected_result[0][3]
            Religion = selected_result[0][4]
            Job = selected_result[0][5]
            Nationality = selected_result[0][6]
            Mothertongue=selected_result[0][7]
            # Layout of Create
            col1, col2 ,col3= st.columns(3)
            with col1:
                new_uname = st.text_input("Uname:",Uname)
                new_gender = st.text_input("Gender:", Gender)
                new_age = st.text_input("Age:", Age)
                new_height = st.text_input("Height:", Height)
            with col2:
                new_religion = st.text_input("Religion:",Religion)
                new_job = st.text_input("Job:",Job)
                new_nationality = st.text_input("Nationality:",Nationality)
                new_mothertongue=st.test_input("Mothertongue:", Mothertongue)
                
            if st.button("Update Profile"):
                edit_wallet_data(new_uname,new_gender,new_age, new_height,new_religion,new_job,new_nationality,new_mothertongue,Uname, Gender, Age, Height, Religion, Job, Nationality, Mothertongue)
                st.success("Successfully updated:: {} to ::{}".format(Uname, new_uname))

        result2 = view_all_profile()
        df2 = pd.DataFrame(result2, columns=['Uname', 'Gender', 'Age', 'Height', 'Religion', 'Job', 'Nationality', 'Mothertongue'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='Prefrences':
        result = view_all_pref()
        # st.write(result)
        df = pd.DataFrame(result, columns=['Uname', 'Gender', 'Age', 'Height', 'Religion', 'Job', 'Nationality', 'Mothertongue'])
        with st.expander("Current Prefrences"):
            st.dataframe(df)
        list_of_pref = [i[0] for i in view_only_pref()]
        selected_pref = st.selectbox("user to Edit", list_of_pref)
        selected_result = get_tid(selected_pref)
        # st.write(selected_result)
        if selected_result:
            Uname = selected_result[0][0]
            Gender = selected_result[0][1]
            Age = selected_result[0][2]
            Height = selected_result[0][3]
            Religion = selected_result[0][4]
            Job = selected_result[0][5]
            Nationality = selected_result[0][6]
            Mothertongue=selected_result[0][7]
            # Layout of Create
            col1, col2 ,col3= st.columns(3)
            with col1:
                new_uname = st.text_input("Uname:",Uname)
                new_gender = st.text_input("Gender:", Gender)
                new_age = st.text_input("Age:", Age)
                new_height = st.text_input("Height:", Height)
            with col2:
                new_religion = st.text_input("Religion:",Religion)
                new_job = st.text_input("Job:",Job)
                new_nationality = st.text_input("Nationality:",Nationality)
                new_mothertongue=st.test_input("Mothertongue:", Mothertongue)
                
            if st.button("Update Profile"):
                edit_wallet_data(new_uname,new_gender,new_age, new_height,new_religion,new_job,new_nationality,new_mothertongue,Uname, Gender, Age, Height, Religion, Job, Nationality, Mothertongue)
                st.success("Successfully updated:: {} to ::{}".format(Uname, new_uname))

        result2 = view_all_profile()
        df2 = pd.DataFrame(result2, columns=['Uname', 'Gender', 'Age', 'Height', 'Religion', 'Job', 'Nationality', 'Mothertongue'])
        with st.expander("Updated data"):
            st.dataframe(df2)
'''
    elif table=='Prefrences':
        result = view_all_pref()
        # st.write(result)
        df = pd.DataFrame(result, columns=['Uname', 'Gender', 'Age', 'Height', 'Religion', 'Job', 'Nationality', 'Mothertongue'])
        with st.expander("Profile"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_pref()]


 #       selected_dealer = st.selectbox("user to Edit", list_of_)                       
 #?????????????????????????????????????????/


        selected_result = get_prom_id(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            Uname = selected_result[0][0]
            Gender = selected_result[0][1]
            Age = selected_result[0][2]
            Height = selected_result[0][3]
            Religion = selected_result[0][4]
            Job = selected_result[0][5]
            Nationality = selected_result[0][6]
            Mothertongue=selected_result[0][7]
            # Layout of Create

            col1, col2 ,col3= st.columns(3)
            with col1:
                new_uname = st.text_input("Uname:",Uname)
                new_gender = st.text_input("Gender:", Gender)
                new_age = st.text_input("Age:", Age)
                new_height = st.text_input("Height:", Height)
            with col2:
                new_religion = st.text_input("Religion:",Religion)
                new_job = st.text_input("Job:",Job)
                new_nationality = st.text_input("Nationality:",Nationality)
                new_mothertongue=st.test_input("Mothertongue:", Mothertongue)
                
            if st.button("Update Profile"):
                edit_pref_data(new_uname,new_gender,new_age, new_height,new_religion,new_job,new_nationality,new_mothertongue,Uname, Gender, Age, Height, Religion, Job, Nationality, Mothertongue)
                st.success("Successfully updated:: {} to ::{}".format(Uname, new_uname))

        result2 = view_all_profile()
        df2 = pd.DataFrame(result2, columns=['Uname', 'Gender', 'Age', 'Height', 'Religion', 'Job', 'Nationality', 'Mothertongue'])
        with st.expander("Updated data"):
            st.dataframe(df2)
'''

'''

    elif table=='transactions':
        result = view_all_data_transactions()
        # st.write(result)
        df = pd.DataFrame(result, columns=['transaction_id', 'transaction_date','transaction_detail', 'amount','to_id','from_id','type_trans'])
        with st.expander("Current transactions"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_data_transactions()]
        selected_dealer = st.selectbox("transactions to Edit", list_of_dealers)
        selected_result = get_transaction_id(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            transaction_id = selected_result[0][0]
            transaction_date = selected_result[0][1]
            transaction_detail = selected_result[0][2]
            amount = selected_result[0][3]
            to_id = selected_result[0][4]
            from_id = selected_result[0][5]
            type_trans = selected_result[0][6]
            
            # Layout of Create

            col1, col2 = st.columns(2)
            with col1:
                new_transaction_id = st.text_input("transaction_id:",transaction_id)
                new_transaction_date = st.text_input("transaction_date:", transaction_date)
                new_transaction_detail = st.text_input("transaction_detail:", transaction_detail)
                new_amount = st.text_input("amount:", amount)
            with col2:
                new_to_id = st.text_input("to_id:",to_id)
                new_from_id = st.text_input("from_id:",from_id)
                new_type_trans = st.text_input("type_trans:",type_trans)
                
            if st.button("Update book"):
                edit_transactions_data(new_transaction_id, new_transaction_date,new_transaction_detail, new_amount,new_to_id,new_from_id,new_type_trans,transaction_id, transaction_date,transaction_detail, amount,to_id,from_id,type_trans)
                st.success("Successfully updated:: {} to ::{}".format(transaction_id, new_transaction_id))

        result2 = view_all_s()
        df2 = pd.DataFrame(result2, columns=['transaction_id', 'transaction_date','transaction_detail', 'amount','to_id','from_id','type_trans'])
        with st.expander("Updated data"):
            st.dataframe(df2)



    elif table=='promo_offers':
        result = view_all_data_promo_offers()
        # st.write(result)
        df = pd.DataFrame(result, columns=['promo_id','user_id','start_date','end_date','duration','status', 'amount_value'])
        with st.expander("Current bookings"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_data_promo_offers()]
        selected_dealer = st.selectbox("user to Edit", list_of_dealers)
        selected_result = get_promo_id(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            promo_id = selected_result[0][0]
            user_id = selected_result[0][1]
            start_date = selected_result[0][2]
            end_date = selected_result[0][3]
            duration = selected_result[0][4]
            status = selected_result[0][5]
            amount_value = selected_result[0][6]
            # Layout of Create

            col1, col2 ,col3= st.columns(3)
            with col1:
                new_promo_id = st.text_input("promo_id:",promo_id)
                new_user_id = st.text_input("user_id:", user_id)
                new_start_date = st.text_input("start_date:", start_date)
                
            with col2:
                new_end_date = st.text_input("end_date:", end_date)
                new_duration = st.text_input("duration:",duration)
                new_status = st.text_input("status:",status)
                new_amount_value = st.text_input("amount_value:",amount_value)
            if st.button("Update book"):
                edit_promo_offers_data(new_promo_id,new_user_id,new_start_date,new_end_date,new_duration,new_status, new_amount_value,promo_id,user_id,start_date,end_date,duration,status, amount_value)
                st.success("Successfully updated:: {} to ::{}".format(promo_id, new_promo_id))

        result2 = view_all_data_promo_offers()
        df2 = pd.DataFrame(result2, columns=['promo_id','user_id','start_date','end_date','duration','status', 'amount_value'])
        with st.expander("Updated data"):
            st.dataframe(df2)

    elif table=='dependents':
        result = view_all_data_dependents()
        # st.write(result)
        df = pd.DataFrame(result, columns=['dependent_id','trans_id','user_ref_id','fname','lname','phone' ,'email' ,'dob','relation'])
        with st.expander("Current bookings"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_data_dependents()]
        selected_dealer = st.selectbox("user to Edit", list_of_dealers)
        selected_result = get_dependent_id(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            dependent_id = selected_result[0][0]
            trans_id = selected_result[0][1]
            user_ref_id = selected_result[0][2]
            fname = selected_result[0][3]
            lname = selected_result[0][4]
            phone = selected_result[0][5]
            email = selected_result[0][6]
            dob = selected_result[0][7]
            relation = selected_result[0][8]


            # Layout of Create

            col1, col2 ,col3= st.columns(3)
            with col1:
                new_dependent_id = st.text_input("dependent_id:",dependent_id)
                new_trans_id = st.text_input("trans_id:", trans_id)
                new_user_ref_id = st.text_input("user_ref_id:", user_ref_id)
                new_fname = st.text_input("fname:", fname)
            with col2:
                new_lname = st.text_input("lname:",lname)
                new_phone = st.text_input("phone:",phone)
                new_email = st.text_input("email:",email)
                new_dob = st.text_input("dob:",dob)
                new_relation = st.text_input("relation:",relation)
            if st.button("Update book"):
                edit_dependents_data(new_dependent_id,new_trans_id,new_user_ref_id,new_fname,new_lname,new_phone,new_email,new_dob,new_relation,dependent_id,trans_id,user_ref_id,fname,lname,phone,email,dob,relation)
                st.success("Successfully updated:: {} to ::{}".format(dependent_id, new_dependent_id))

        result2 = view_all_data_dependents()
        df2 = pd.DataFrame(result2, columns=['dependent_id','trans_id','user_ref_id','fname','lname','phone' ,'email' ,'dob','relation'])
        with st.expander("Updated data"):
            st.dataframe(df2)



    elif table=='transaction_status':
        result = view_all_data_transaction_status()
        # st.write(result)
        df = pd.DataFrame(result, columns=['trans_id','u_id','status'])
        with st.expander("Current bookings"):
            st.dataframe(df)
        list_of_dealers = [i[0] for i in view_only_data_transaction_status()]
        selected_dealer = st.selectbox("user to Edit", list_of_dealers)
        selected_result = get_trans_id(selected_dealer)
        # st.write(selected_result)
        if selected_result:
            trans_id = selected_result[0][0]
            u_id = selected_result[0][1]
            status = selected_result[0][2]

            # Layout of Create

            col1, col2 = st.columns(2)
            with col1:
                new_trans_id = st.text_input("trans_id:",trans_id)
                new_u_id = st.text_input("u_id:",u_id)
                
            with col2:
                new_status = st.text_input("status:",status)

                
            if st.button("Update book"):
                edit_transaction_status_data(new_trans_id,new_u_id,new_status,trans_id,u_id,status)
                st.success("Successfully updated:: {} to ::{}".format(trans_id, new_trans_id))

        result2 = view_all_data_transaction_status()
        df2 = pd.DataFrame(result2, columns=['trans_id','u_id','status'])
        with st.expander("Updated data"):
            st.dataframe(df2)
'''
