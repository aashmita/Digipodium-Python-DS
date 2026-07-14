# 14 July 2026
# pip install streamlit
# analysis , visualization, applicatins -> we require fronted - in flask -> end to end frontend backend database - library in which we can use pre defined componenets - tailwind css, html,css,java
# easy to make application , dashboard page, either power bi excel, ui does not matter

# Streamlit : is a UI library which provides ready to use components

# to run : python -m streamlit run filename.py

# pip install list

import streamlit as st # used to import library and server will also not start without it 

st.title("Welcome to my Dashboard")  # Heading
st.markdown("Performs all the operations easily")  # normal content
st.write("Hello")

fnum = st.chat_input()
fnum = st.number_input("enter first number")
fnum = st.number_input("enter second number")

c1,c2 = st.columns(2)
fnum = c1.number_input("Enter first nnumber")
snum = c2.number_input("Enter second number")

operations = ["Add","Sub","Mul","Div"]
choice = st.radio("Select an operation",operations)

button = st.button("Calculate")

result = 0
if button:
    if choice == "Add":
        result = fnum+snum
    if choice == "Sub":
        result = fnum - snum
    if choice == "Mul":
        result = fnum*snum
    if choice == "Div":
        result = fnum/snum

st.success(f"Result is {result}")

st.balloons()
st.snow()

st.toast("Saved Successfully! ")