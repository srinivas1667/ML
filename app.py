import streamlit as st
import joblib
model = joblib.load('spam-ham') # we are laoding the pipeline model using joblib
st.title('SPAM-HAM CLASSIFIER') # it creates a title in web app 
ip = st.text_import('Enter The Message') # it creates a text box in the web app
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])  # st.button will create a button witrh name predict . The 0th element in op variable is displayed as a title
