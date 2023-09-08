import streamlit as st
import pandas as pd
from PIL import Image


st.sidebar.title(":balloon: Day 4 :balloon: Control Flow")

image = Image.open("/Users/raahool/applications/github/pythontutor/static/pythonlogo.png")
st.sidebar.image(image, width=150)
st.sidebar.info("""
                Today's Topic
                - Decision Making
                - Loops
                """)


pages_name = ["Decision Making",
             "Loops"]

page = st.sidebar.radio('Navigations', pages_name)

if page == 'Decision Making':
    st.header("if statements")

    st.header("if .. else statements")

    st.header("nested if statements")
