import streamlit as st

name = st.text_input("What is your name:")
age = st.number_input("How old are you:")
gender = st.selectbox("What is your gender:", ["male", "female"])
price = st.number_input("Enter your ticket price:")
size = st.number_input("Enter the number of people in your party:")

if st.button("Submit"):
    st.write(f"Name: {name}")
    st.write(f"Age: {age}")
    st.write(f"Gender: {gender}")
    st.write(f"Ticket Price: {price}")
    st.write(f"Party Size: {size}")