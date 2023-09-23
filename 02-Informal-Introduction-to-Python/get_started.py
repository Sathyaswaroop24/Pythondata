import streamlit as st
import pandas as pd
from PIL import Image


col1, col2 = st.sidebar.columns(2)

with col1:
    st.image("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2zXbuCACzfYCQqAXDxiKcWjiH3gojlltHtV7XN9D-dPhiP9M4YYnBo0exWeAYANa-U4IuW5-TGvAVkKz86c7DpweWcnROrDYNuK4AjIAlw2bguqUY5KwEj-Qmr0EvIRpihEfankorurHuleF7dtEuDxprJ9kSbvHOQ7ZlvVTbY-TS5H0KjEQ4EWi8FCU/s1600/pythonlogo.png",
              width=100)
with col2:
    st.title(":balloon: Getting Started")

st.sidebar.info("""
                [Day 2] Today's Topic
                - Summary Till now 
                - Using the Python Interpreter
                - An Informal Introduction to Python
                - More Control Flow Tools
                """)


pages_name = ["Till now","Interpreter", "An Informal Introduction to Python",
              "Using Python as a Calculator",
              "First Steps Towards Programming"]

page = st.sidebar.radio('Navigations', pages_name)

if page == "Till now":
    st.subheader("Features of Python")
    st.success(
        """
        - Simple and easy to learn ***
        - Freeware and OpenSource
        - High Level programmer language
        - Platform Independent
        - Portable ***
        - Dynamically Typed *** 
        - Both Procedure oriented and Object oriented
        - Interpreted 
        - Extensible ***
        - Embedded ***
        - Extensive Library *****
        """
        )
    
    st.subheader("Limitation of Python")
    st.info(
        """
        - Performance Wise 
        - Mobile application
        """
    )

    st.subheader("Myth")
    st.error("Python is not suitable for Large scale enterprise applications")


    st.subheader("Flavors of Python")
    st.info(
        """
        - CPython
        - Jython or JPython
        - IronPython
        - PyPy (Python for Speed) --> PVM --> JIT (Just In Time Compiler)
        - RubyPython
        - AnacondaPython 
        """
    )

    st.image('https://cdn.ttgtmedia.com/rms/onlineimages/whatis-just_in_time_compiler-h.png')
    
    st.subheader("Python Versions")
    st.info(
        """
        - 1.0 --> It almost dead, nobody talk about it
        - 2.0 --> Stop support from last year
        - 3.0 --> In todays' talk
        """
    )
if page == 'Interpreter':
    
    st.subheader("The Python Interpreter")
    st.info(
        """
        Interpreter operats somehow like `UNIX shell`

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

    st.info(
        """
        - By default Python source is treated as encoded in `UTF-8`
        """
    )
    st.code(
        """
        # -*- coding: encoding -*-
        # __author__: codelocked

        def function_name():
            ''' Bruce Lee Movie '''
            return "Enter the New Dragon"
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
    st.text(
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
    st.header("Numbers")

    st.error("""
             Types of numbers available in python depends on which version of python you are using
            """)
    st.write("In Python 2.XX")
    st.info(
        """
        Types of number: int, long, float, complex

        whole number: int, long
        """
    )
    
    st.write("In Python 3.XX")
    st.info(
        """
        Types of number: int, float, complex
        """
    )
    
    st.code(
        """
        import sys; sys.maxint

        # Int and Long automatically handle by Python
        # Float
        # Complex  i = sqrt(-1)        
                
        z = 3 + 4.7j
                
        print(z.real, z.imag) 
        """
    )


    st.header("Text")

    st.info(
        """
         - In programming text represnted by strings
                   
        - Different ways in python to handle apostrope, quotation, long text with new lines
        """
    )
    st.code(
        """
        # Double quotes
        message = "Codelocked tutorial"

        # Single quotes            
        message2 = 'Another string for codelocked'    
                   
        # syntax error
        message = 'I'm in "codelocked" stuff'     

        '''
        Best way to treat single quotes as charater. 
        No error and no escape char
        '''
        message = "I'm in stuff"  
                   
        movie_quote = '''
        There is no middle ground.
        either you die like a hero
                   or live long enough'''`

        sanskrit_quotes = '''एकः क्षमावतां दोषो द्वतीयो नोपपद्यते। 
                            यदेनं क्षमया युक्तमशक्तं मन्यते जनः ॥'''
        
        """
    )

    st.success("So you can create strings with Single, double, tripple quotes")

    st.header("List**")

    st.info(
        """
        Comma-separated values (items) between square brackets

        Same type or different type items

        Lists can be indexed and sliced

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
