import streamlit as st
import pandas as pd
from PIL import Image


col1, col2 = st.sidebar.columns(2)

with col1:
    st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2zXbuCACzfYCQqAXDxiKcWjiH3gojlltHtV7XN9D-dPhiP9M4YYnBo0exWeAYANa-U4IuW5-TGvAVkKz86c7DpweWcnROrDYNuK4AjIAlw2bguqUY5KwEj-Qmr0EvIRpihEfankorurHuleF7dtEuDxprJ9kSbvHOQ7ZlvVTbY-TS5H0KjEQ4EWi8FCU/s1600/pythonlogo.png",
              width=100)
with col2:
    st.title(":balloon: Control Flow")

st.sidebar.info("""
                [Day 4] Today's Topic
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

