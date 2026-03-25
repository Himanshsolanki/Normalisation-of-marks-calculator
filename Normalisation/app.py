import streamlit as st
import numpy as np 

# title 
st.title("Marks Normalizer")
st.write("Calculate your normalized score based on class performance.")

#input
marks = st.number_input("Enter the marks you have achieved in your paper : ", value = 0.0)
max_val = st.number_input("Enter the max marks achieved in your class : ", value = 1.0)
min_val = st.number_input("Enter the min marks achieved in your class : ", value = 0.0)

if max_val > min_val : 
    normalised = (marks - min_val) / (max_val - min_val) *50

    st.divider()
    st.subheader("Final Result")
    st.metric(label = "Normalised Score (Out of 50)", value = f"{normalised:.2f}")

else :
    st.error("maximum marks cannot be less than minimum")

st.write("Created by Himansh Solanki")




