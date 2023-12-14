import streamlit as st
st.set_page_config(layout = "wide")

st.header("Hi, my name is Shivam,")
st.header("And welcome to my website")
st.text("This is a simple website, on this website you will be able to check which one of the 3 numbers you're going to enter is the largest number.")
st.text("so lets get started...")

a = st.number_input("Enter the first number")
b = st.number_input("Enter the second number")
c = st.number_input("Enter the third number")

def largest(a, b, c):
    if(a>b):
        if(a>c):
            return a
        else:
            return c
    else:
        if(b>c):
            return b
        else:
            return c
        
st.write("The largest among the 3 numbers you entered is ", largest(a,b,c))

st.header("heyyyy")

