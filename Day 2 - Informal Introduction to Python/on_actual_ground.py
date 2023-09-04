import streamlit as st
import pandas as pd
from PIL import Image

image = Image.open("/Users/raahool/applications/github/pythontutor/static/pythonlogo.png")
st.sidebar.image(image, caption='Welcome To Codelocked')
st.sidebar.info("""
                Today's Topic
                - Python Variables
                - Python Data Types
                - Types of Python Operators
                """)

st.title("Day 3: Let's Get Started :balloon:")

pages_name = ["Python Variables",
             "Python Data Types",
              "Types of Python Operators",
              "Assignment"]

page = st.radio('Navigations', pages_name)

if page == 'Python Variables':
    st.subheader("The Python Interpreter [/usr/local/bin/python3.11]")
    st.markdown(
        """
        - No explicit declaration to reserve memory space

        - A Python variable is created automatically when you assign a value to it

        - Must start with Letter and _ only

        - cannot start with Number or special charaters $, (, * \% \etc.

        - contain alpha-numeric characters and underscores

        - variables are Case-sensitive

        - reserved keywords can not be user as variables
        """
    )
    st.code(
        """
        counter = 100          # Creates an integer variable
        miles   = 1000.0       # Creates a floating point variable
        name    = "Codelocked" # Creates a string variable
        """
    )

    st.subheader("Printing Python Variables")

    st.subheader("Deleting variable")

    st.subheader("Multiple Assignments")
    st.code(
        """
        a = b = c = 100
        
        a,b,c = 1,2,"Codelocked"
        """
    )

    st.subheader('Local vs Global variable')

    st.code(
        """
        # Python Local Variable
        def sum(x,y):
            sum = x + y
            return sum
            print(sum(5, 10))
        """
    )


    st.code(
        """
        # Python Global Variable
        x = 5
        y = 10
        def sum():
            sum = x + y
            return sum
        print(sum())
        """
    )

if page == "Python Data Types":
    st.subheader("Python Numeric Data Type")
    st.markdown(
        """
        - int,long,float,complex --> Py2
        - int, float,complex     --> py3
        """
    )

    st.subheader("Python String Data Type")
    st.subheader("Python List Data Type")
    st.subheader("Python Tuple Data Type")
    st.subheader("Python Ranges")
    st.code(
        """
        range(start, stop, step)
        """
    )

    st.subheader("Python Dictionary")
    st.subheader("Python Boolean Data Types")

    st.header("Python Data Type Conversion")

    st.header("Data Type Conversion Functions")

if page == "Types of Python Operators":
    st.markdown(
        """
        Python language supports the following types of operators.

        - Arithmetic Operators
        `+ - * / % ** //`

        - Comparison (Relational) Operators
        `== != > < >= <=`
        
        - Assignment Operators
        `= += -= *= /= %= **= //=`

        - Logical Operators
        `and or NOT`
        
        - Bitwise Operators
        `& | ^ ~ << >>`

        - Membership Operators
        `in not in`

        - Identity Operators
        ` is  is not`
        """
    )

    st.subheader("Python Operators Precedence")
    st.code(
        """
        **                  Exponentiation (raise to the power)    
        ~ + -               Complement, unary plus and minus (method names for the last two are +@ and -@)
        * / % //             Multiply, divide, modulo and floor division
        + -                             Addition and subtraction
        >> <<                           Right and left bitwise shift
        &                               Bitwise 'AND'
        ^ |                             Bitwise exclusive `OR' and regular `OR'
        <= < > >=                       Comparison operators
        <> == !=                        Equality operators
        = %= /= //= -= += *= **=        Assignment operators
        is is not                       Identity operators
        in not in                       Membership operators
        not or and                      Logical operators
        """
    )


if page == "Assignment":
    st.success(
        """
        HACKERRANK
        ===========

        1. https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true

        2. https://www.hackerrank.com/challenges/python-division/problem?isFullScreen=true

        3. https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true

        
        PYTHON SCRIPT CODE DEVELOPMENT
        ==============================
        4. Develop Calculator program in Python
        - Should Addition, multiplication, division and substraction 
        - Extra creadt for well written program
        - Extra credit for use of interactive program 
        """
    )