import streamlit as st
import pandas as pd
from PIL import Image

image = Image.open("C:\\Users\\rahul\\Desktop\\Python\\pythontutor\\static\\pythonlogo.png")
st.sidebar.image(image, caption='Python')
st.sidebar.info("""
                Today's Topic
                - Python Introduction
                - Environment Setup""")

st.title('Day 1: Intro to Python :balloon:')

pages_name = ["Introduction", "Features", "Advance features", "Environment Setup"]
page = st.radio('Navigations', pages_name)

if page == 'Introduction':

    st.info(':link: WIKIPEDIA https://g.co/kgs/zT4b9h')
    
    st.info(':link: PYTHON.ORG https://www.python.org/')
    
    st.checkbox("Open Source and different version", key=None)  
                
    st.checkbox("Simple and so easy to learn", key=None)
                
    st.checkbox("Versatile and can be use to create many different things", key=None)
                
    st.checkbox("Powerful development libraries include AI, ML etc", key=None)
    st.checkbox("What is High Level Langague vs Low Level Language ?", key=None)
    st.checkbox("What is general-purpose programming language GPL ? vs Domain Specific PL ?", key=None)
    st.checkbox("What is Design philosophy emphasizes code readability ?", key=None)
    st.checkbox("Python is dynamically typed and garbage-collected ?", key=None)

    st.subheader("Python is Interpreted Language")
    
    st.header(":hand: Hello World ?")
    st.subheader("In Java")
    st.code("""
            public class HelloWorld
            {
                public static void main(String[] args)
                {
                    System.out.println("Hello World")
                }
            }""")
    st.subheader("In C")
    st.code("""
            #include<stdio.h>
            void main()
            {
            printf("Hello World");
            }
            """)

if page == 'Features':        
    st.checkbox("Easy-to-Read, Easy-to-Maintain", key=None)
    st.code("""
            def today_will_rain(cloud):
                '''Pseudo code for understanding''' 
                if cloud:
                    return "Yes! it will rain :-)"
                return "No! :-("
            """)
    st.checkbox("Easy-to-learn", key=None)
    st.code("""
            # Assign variables
            a,b = 10,20
            """)
    st.checkbox("Easy-to-Maintain", key=None)
    
    st.checkbox("A broad Standard Library", key=None)
    st.info("""Python bulk of Labrires works on cross plaform 
            compatible on  UNIX, Windows, and Macintosh        
            """)      
                
    st.checkbox("Interactive Mode - help in dubugging and testing", key=None)
    
    st.checkbox("Portable - Runs on wide verity of platform e.g., rasberryPI", key=None)
                
    st.checkbox("Extendable - can add low level modules to python Interpreter", key=None)
                
    st.checkbox("Databases", key=None)
                
    st.checkbox("GUI Programming", key=None)
                
    st.checkbox("Scalable - support larger programs better than shell scripting", key=None) 

    st.checkbox("Dynamically Type language")
    st.code("explore ---> type()")

if page == 'Advance features':        
    st.code("""Developed by - Guido van Rossum and name it
                from popular BBC show - Monty python's Circus""")
        
    st.error("What Gudio did - ")

    st.code('''
            While developing Python, he borrow all the features from all the langauges
            - Functional Programming Features ---> C
            - OOP                             ---> C++   
            - Scripting langauges features    ---> Perl & Shell Script
            - Modular Programming features    ---> Modula-3
            ''')
    st.success('Everything in python can be convert to Modules')

    st.code('''
            ########################
            # Functional Programming
            ########################
            def f1():print("Say Hello from function") 
            
            ########################
            # OOP
            ########################
            class C1:
                def __init__(self):
                    print("Say Hello from class")   
            
            ########################
            # Scripting 
            ########################
            message = "Say hello from Script"
            if __name__ == __main__:
                print(message)
            
            ########################
            # Modular
            ########################
            Demo

            ''')
    st.checkbox("Scripting language or can be compiled to byte-code for buliding large application", key=None)
                
    st.checkbox("It provides very ligh-level dynamic data types and support dynamic type checking", key=None)
                
    st.checkbox("It support automatic garbage collection", key=None)
                
    st.checkbox("It can be easily intergrated with C, C++, COM, ActaiveX, CORBA and JAVA", key=None)
    
    st.image('https://static.streamlit.io/examples/dice.jpg')


if page == "Environment Setup":
    st.caption("""
    - virtualenv https://virtualenv.pypa.io/en/latest/installation.html
                
    - venv https://docs.python.org/3/library/venv.html
                
    - pipenv  https://pypi.org/project/pipenv/
                
    - https://towardsdatascience.com/comparing-python-virtual-environment-tools-9a6543643a44?gi=92066116744e
    """)

    st.info("We will go ahead with Anaconda/Miniconda")
