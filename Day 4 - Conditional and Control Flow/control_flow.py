import streamlit as st
import pandas as pd
from PIL import Image


st.sidebar.title(":balloon: Day 4 :balloon: Control Flow")
'''
image = Image.open("/Users/raahool/applications/github/pythontutor/static/pythonlogo.png")
st.sidebar.image(image, width=150)
'''
st.sidebar.info("""
                Today's Topic
                - More Control Flow Tools
                """)

st.header("if statements")

st.subheader("#TODO:")
st.code(
    """
    Write a program to get integer input and print it is positive/negative/zero
    ---------------
    Input: 45
    Output: Enter number is Positive number
    """
    )

st.header("for statements")
st.code(
    """
    Measure some strings
    ---------------------
    Input: ["raahool","Supriya","Rashmika"]
    Output: 
    raahool 7
    Supriya 7
    Rashmika 8
    """
    )

st.code(
    """
    Iterate over the collection

    users = {'raahool': 'active', 'supriya': 'inactive', 'rashmika': 'active'}

    """
)

st.header("Range Function")

st.code(
    """
    for i in range(5):
        print(i)
    """
)

