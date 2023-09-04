import streamlit as st
import pandas as pd
from PIL import Image

image = Image.open("/Users/raahool/applications/github/pythontutor/static/pythonlogo.png")
st.sidebar.image(image, caption='Welcome To Codelocked')
st.sidebar.info("""
                Today's Topic
                - Using the Python Interpreter
                - An Informal Introduction to Python
                - More Control Flow Tools
                """)

st.title('Day 2: Get Started Using the Python Interpreter :balloon:')

pages_name = ["Interpreter", "An Informal Introduction to Python",
              "Using Python as a Calculator",
              "First Steps Towards Programming"]

page = st.radio('Navigations', pages_name)

if page == 'Interpreter':
    st.subheader("The Python Interpreter [/usr/local/bin/python3.11]")
    st.markdown(
        """
        - Interpreter operats somehow like `UNIX shell`

        - `python -c command [arg]`

        - `python -m module [arg]`
        
        """
    )

    st.subheader("Argument Passing")
    st.code(
        """
        import sys
        sys.argv[0]
        """
    )

    st.subheader("The Interpreter and Its Environment")

    st.markdown(
        """
        - By default Python source is treated as encoded in `UTF-8`

        `# -*- coding: encoding -*-`

        """
    )

if page == "An Informal Introduction to Python":
    st.subheader(
        "An Informal Introduction to Python"
    )

    st.code(
        """
        >>>
        ...
        """
    )

    st.text("Comment in Python # ")
    st.markdown(
        """
        - Single line Comments
        - Multiline Comments
        - Docstring Comments
        """
    )
    
    st.code(
        """
        # This is a comment.

        '''
        This is a multiline
        comment.
        '''

        def add(a, b):
            '''Function to add the value of a and b'''
            return a+b

        print(add.__doc__)

        """
    )

if page == "Using Python as a Calculator":
    st.subheader("Numbers")

    st.markdown(
        """
        ### Types of numbers available in python depends on which version of python you are using
        
        IN python 2
        ----------------
        ##### Types of number: int, long, float, complex
        ##### whole number: int, long

        import sys; sys.maxint

        Int and Long automatically handle by Python

        Float

        Complex  i = sqrt(-1)        
                
        `z = 3 + 4.7j`
         
        `z.real`
                
        `z.imag`    

        IN python 3
        ----------------
        ##### Types of number: int, float, complex
                   
        `import sys; sys.maxint`

        """
    )


    st.subheader("Text")

    st.markdown(
        """
         - In programming text represnted by strings
                   
        - Different ways in python to handle apostrope, quotation, long text with new lines
                   
        `message = "Codelocked tutorial"`       # Double quotes
                   
        `message2 = 'Another string for codelocked'     # Single quotes
                   
        `message = 'I'm in "codelocked" stuff'     # syntax error

        `message = "I'm in stuff"  # Best way to treat single quotes as charater. No error no escape char
                   
        `movie_quote = '''There is no middle ground.
        either you die like a hero
                   or live long enough'''`

        `sanskrit_quotes = '''एकः क्षमावतां दोषो द्वतीयो नोपपद्यते। 
                            यदेनं क्षमया युक्तमशक्तं मन्यते जनः ॥'''`
        
        So you can create strings with Single, double, tripple quotes  
        """
    )

    st.subheader("List")

    st.markdown(
        """
        - comma-separated values (items) between square brackets

        - same type or different type items

        - lists can be indexed and sliced

        """
    )

if page == "First Steps Towards Programming":
    st.code(
        """
        # Fibonacci series:
        # the sum of two elements defines the next
        a, b = 0, 1                    # Multiple assignments 
        while a < 10:
            print(a)
            a, b = b, a+b
        """
    )
