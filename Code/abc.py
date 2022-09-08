import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image
  
# loading in the model to predict on the data
pickle_in = open('gb.pkl', 'rb')
gb = pickle.load(pickle_in)
  
def welcome():
    return 'welcome all'
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(account_length,voice_mail_plan,voice_mail_messages,day_mins,evening_mins,night_mins,international_mins,customer_service_calls,international_plan,day_calls,day_charge,evening_calls,evening_charge,night_calls,night_charge,international_calls,international_charge,total_charge):  
   
    prediction = gb.predict(
        [[account_length,voice_mail_plan,voice_mail_messages,day_mins,evening_mins,night_mins,international_mins,customer_service_calls,international_plan,day_calls,day_charge,evening_calls,evening_charge,night_calls,night_charge,international_calls,international_charge,total_charge]])
    print(prediction)
    return prediction
      
  
# this is the main function in which we define our webpage 
def main():
      # giving the webpage a title
    st.title("telecommunication_churn")
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Streamlit telecommunications_churn ML App </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    account_length = st.text_input("account length", "Type Here")
    voice_mail_plan=st.sidebar.selectbox("voice mail plan:", [0,1])
    voice_mail_messages = st.text_input("voice mail messages", "Type Here")
    day_mins= st.text_input("day mins", "Type Here")
    evening_mins = st.text_input("evening mins", "Type Here")
    night_mins = st.text_input("night mins", "Type Here")
    international_mins = st.text_input("international mins", "Type Here")
    customer_service_calls=st.sidebar.selectbox("customer service calls:", [0,1,2,3,4,5,6,7,8,9])
    international_plan=st.sidebar.selectbox("international plan:", [0,1])
    day_calls = st.text_input("day calls", "Type Here")
    day_charge = st.text_input("day charge", "Type Here")
    evening_calls = st.text_input("evening calls", "Type Here")
    evening_charge = st.text_input("evening charge", "Type Here")
    night_calls = st.text_input("night calls", "Type Here")
    night_charge = st.text_input("night charge", "Type Here")
    international_calls = st.text_input("international calls", "Type Here")
    international_charge= st.text_input("international_charge", "Type Here")
    total_charge= st.text_input("total_charge", "Type Here")
    result =""
      
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
    if st.button("Predict"):
        result = prediction(account_length,voice_mail_plan,voice_mail_messages,day_mins,evening_mins,night_mins,international_mins,customer_service_calls,international_plan,day_calls,day_charge,evening_calls,evening_charge,night_calls,night_charge,international_calls,international_charge,total_charge)
    st.success('The output is {}'.format(result))
     
if __name__=='__main__':
    main()




