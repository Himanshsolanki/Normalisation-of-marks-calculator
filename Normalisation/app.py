import streamlit as st
import numpy as np 

# title 
st.title("Marks Normalizer")
st.write("Calculate your normalized score based on class performance.")

#input
marks = st.number_input("Enter the marks you have achieved in your paper : ", value = None, placeholder = "Enter Value")
max_val = st.number_input("Enter the max marks achieved in your class : ", value = None, placeholder = "Enter Value")
min_val = st.number_input("Enter the min marks achieved in your class : ", value = None, placeholder = "Enter Value")

if marks is not None and max_val is not None and min_val is not None : 
    if max_val > min_val : 
        normalised = (marks - min_val) / (max_val - min_val) *50

        st.divider()
        st.subheader("Final Result")
        st.metric(label = "Normalised Score (Out of 50)", value = f"{normalised:.2f}")

    else :
        st.error("maximum marks cannot be less than minimum")
    
else : 
    st.warning("Please enter all values.")

st.write("Created by Himansh Solanki")




