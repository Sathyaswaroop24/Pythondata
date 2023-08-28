import streamlit as st
import pandas as pd
import time

st.title('Mistake Based Learning :sunglasses:')


st.sidebar.title("CODELOCKED")
st.sidebar.success("Day 0")

st.text("")


tab1, tab2, tab3, tab4, tab5 = st.tabs(
    ["Python Stuff",
     "Web Frameworks",
     "Data Science and Machine learning",
     "Challenge Task",
     "Bonus"])

with tab1:
    st.header("Basics of Python")
    with st.expander("1. Introduction"):
        st.caption("""
        - Open Source and different version
                   
        - Simple and so easy to learn
                   
        - Versatile and can be use to create many different things
                   
        - powerful development libraries include AI, ML etc
        """)

    with st.expander("2. Python Features"):
        st.caption("""
        - Easy-to-learn, Easy-to-Read, Easy-to-Maintain
                   
        - A broad Standar Library
                   
        - Interactive Mode
        
        - Portable
                   
        - Extendable
                   
        - Databases
                   
        - GUI Programming
                   
        - Scalable 
        """)

    with st.expander("3. Python Advance Features"):
        st.caption("""
        - Functional and structured programming methods as well OOP
                   
        - Scripting language or can be compiled to byte-code for buliding large application
                   
        - It provides very ligh-level dynamic data types and support dynamic type checking
                   
        - It support automatic garbage collection
                   
        - It can be easily intergrated with C, C++, COM, ActaiveX, CORBA and JAVA
        """)
        st.image('https://static.streamlit.io/examples/dice.jpg')


    with st.expander("4. Environment Setup"):
        st.caption("""
        - virtualenv
                   
        - python environment wrapper (pew)
                   
        - venv
                   
        - pipenv
                   
        - https://towardsdatascience.com/comparing-python-virtual-environment-tools-9a6543643a44?gi=92066116744e
        """)

    with st.expander("5. Basic Syntax"):
        st.caption("""
        - Interactive Mode programming
                   
        - Script Mode Programming
        
        - python Identifiers
                   
        - Python reserve words
        
        - python Lines and Indentation
                   
        - Python Multi-Line Statments
        """)

    with st.expander("6. Hello World in Python"):
        st.caption("""
        - Interative Mode
                   
        - Script mode
        """)

    with st.expander("7. Introduction to Python Strings"):
        st.caption("""
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
        """)

    with st.expander("8. Numbers in Python 2"):
        st.caption("""
        ```Types of numbers available in python depends on which version of python you are using
        
        IN python 2
        ----------------
        # Types of number: int, long, float, complex
        # whole number: int, long

        import sys; sys.maxint

        Int and Long automatically handle by Python

        Float

        Complex  i = sqrt(-1)
                z = 3 + 4.7j
                z.real
                z.imag       
        """)

    with st.expander("9. Numbers in Python 3"):
        st.caption("""
        ```Types of numbers available in python depends on which version of python you are using
        
        IN python 3
        ----------------
        # Types of number: int, float, complex
                   
        import sys; sys.maxint

        Float

        Complex  i = sqrt(-1)
                z = 3 + 4.7j
                z.real
                z.imag       
        """)

    with st.expander("10. Arithmatic in python 2 vs 3"):
        st.caption("""
        """)

    with st.expander("11. Interactive Help"):
        st.caption("""
        """)

    with st.expander("Further to advance in python"):
        st.caption("""
        13. Python Boolean
        14. Datetime moduel in python
        15. IF then ELSE in python
        16. Python Functions
        17. Sets in Python
        18. Python Lists
        19. Python dictionaries
        20. Python Tuples
        21. Logging in Python
        22. CSV Files in Python
        23. List comprehension
        24. Python Classes and objects
        25. JSON n python
        26. XML and Element tree
        27. Lambda Expression and Anonymous Function
        28. MAP, FILtER and reduce
        29. Sorting in python
        30. Unit test in python
        31. Exception on python
        32. Urllib - GET request
        33. Special Method
        34. Iteration, Iterables and itertools
        35. Generators in python
        36. Regurlar expression
        37. Python Pickle
        38. PEP (Python Enhancement Proposals)
        39. Decorators
        40. And More...
        """)


with tab2:
    st.header("Web Frameworks")
    with st.expander("Different Web Frameworks"):
        st.caption("""
        - Django
                   
        - Flask
            
        - FastAPI
                   
        - Streamlit
                   
        - Docker container and Deployment of python application

        """)

with tab3:
    st.header("Data Science and Machine learning")
    with st.expander("1. Introduction"):
        st.caption("""

        - Pandas
                   
        - Matplotlib and seaborn
                   
        - Sklearn
                   
        - More on Colab, Kaggle and huggingface
        """)

    import numpy as np
    import pydeck as pdk

    chart_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])

    st.pydeck_chart(pdk.Deck(
        map_style=None,
        initial_view_state=pdk.ViewState(
            latitude=37.76,
            longitude=-122.4,
            zoom=11,
            pitch=50,
        ),
        layers=[
            pdk.Layer(
            'HexagonLayer',
            data=chart_data,
            get_position='[lon, lat]',
            radius=200,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
            ),
            pdk.Layer(
                'ScatterplotLayer',
                data=chart_data,
                get_position='[lon, lat]',
                get_color='[200, 30, 0, 160]',
                get_radius=200,
            ),
        ],
    ))
with tab4:
    st.header("Challenge Task")
    with st.expander("HSBC Python Developer Coding Test"):
        st.markdown("""
        
        Design and implement a RESTful API service using any Python framework you wish. The service will
        accept IPv4 addresses and domains, query external services and return appropriate responses.

        #### You Will Need
        - A python IDE
        - Python version 3.8+
        - A `URLScan.io` API Key
            * These are free and can be obtained here: https://urlscan.io/about-api/
                * If you do not wish to sign up for an API key, please let us know and we will
        create one for you

        - A `VirusTotal` API key
            * These are free and can be obtained here: https://support.virustotal.com/hc/en-
        us/articles/115002088769-Please-give-me-an-API-key
                * If you do not wish to sign up for an API key, please let us know and we will
        create one for you

        #### Input
        The service should expose 3 endpoints:
        |            METHOD | SOURCE | INPUT|
        |-------|----------|------------|
        |GET | PATH | type: str = “ip” or “domain”  data: &lt;ipv4 or domain name&gt; Example:  `/ip/1.2.3.4`  &  `/domain/hsbc.com` |
        |GET |PARAMS |type: str = “ip” or “domain” data: &lt;ipv4 or domain name&gt;  Example:  `?type=ip&amp;data=1.2.3.4`  &   `?type=domain&amp;data=hsbc.com`
        |POST |BODY(JSON)| type: str = “ip” or “domain”       data: &lt;ipv4 or domain name&gt;        Example:  `{“type”: “ip”, “data”: “1.2.3.4”}`  & `{“type”: “domain”, “data”: “hsbc.com”}` |
        #### Processing
        Incoming data should be parsed to ensure it looks valid. Either data modelling or regular expressions
        are acceptable for this.
        When data is validated, you should perform the following actions:
        - Submit the data to both VirusTotal and URLScan.io

        - Parse the data and determine whether either of these services consider the data malicious

        #### Output
        You should return data according to this schema with an appropriate status code:
        `
                    
                {
                    
                “virustotal”: Union[dict[virustotal_object], None],
        
                “urlscan”: Union[dict[urlscan_object], None],
        
                “malicious”: bool
            }


        #### Extra Credit
        - Resolve domains and include the resolved IP in the return object
        - Include additional free or opensource APIs/services to query

        #### Caveats
        - Feel free to use existing libraries or spin your own
        - The service should run as-is either directly or via a service manager like Gunicorn
        """)

with tab5:
    st.header("Bonus")
    with st.expander("World of AI"):
        st.caption("""
        - ChatGTP
                
        - Bard
        """)
