import streamlit as st
import pandas as pd
from PIL import Image


st.sidebar.title(":balloon: Day 3 :balloon:  Let's Get Started")

image = Image.open("/Users/raahool/applications/github/pythontutor/static/pythonlogo.png")
st.sidebar.image(image, width=150)
st.sidebar.info("""
                Today's Topic
                - Python Indentifiers and Reserve Words
                - Python Variables
                - Python Data Types
                - Types of Python Operators
                """)


pages_name = ["Indentifiers",
              "Reserve Words",
            "Python Variables",
             "Python Data Types",
              "Types of Python Operators",
              "Assignment"]

page = st.sidebar.radio('Navigations', pages_name)

if page == "Indentifiers":
    st.header("Indentifiers in Python")
    st.info(
        """ 
        #### Any name in python is consider as indentifiers
        it may be variable name, method name, class name

        Rules:
        - allowed symbols: a-z,A-Z, 0-9 , _
        
        - Should not start with digit 

        - case sensitive 

        - can't use reserved keywords

        - No length limit
        """
    )

    st.subheader('Python - Magic or Dunder Methods')
    st.markdown(
        """
        |Python Specials|Description|
        |------------|-------------|
        |_x      |  indicated that Private variable|
        |__x     | indicated that strongly private|
        | \_\_x\_\_   | it is language specific special identifiers|
        
        e.g., __name__, __add__ and many more
        """
    )
    st.code("print(dir(int))")

    st.markdown(
        """
        |Method|Description|
        |------|-----------|
        |__new__() | returns a new object |
        |__str__() | it is overridden to return a printable string representation of any user defined class|
        |__add__() | addition of these two distance objects is desired to be performed using the overloading + operator.|

        and Many more ....
        """
    )

    st.info(

        """
        - In many programming language main() function to indicate the starting point of execution.
        
        - In python, as Interpreted langauge we dont need main().
        The execution start from statement in program file

        - Python include special variable called __name__ that contain the scope of code being executed as a string

        - __main__ is the name of the top-level scope in which top-level code executes.

        """
    )

    st.success(
        '''
        Note: The Python script file executing from the command prompt/terminal will be executed under the top-level scope __main__ scope. However, importing a module will be executed under the module's own scope. So, the top-level scope will be __main__, and the second scope would be module's scope.

Thus, using the special variable __name__ and the top-level scope __main__ increases the reusability. The Python script file can be executed from the command prompt/termainal as an indipendent script as well as when imported as a module.

        '''
    )
if page == "Reserve Words":
    st.header("Keywords in Python")
    st.info(
        """
        33 keywords in python
        Rules:
        -----
        - only aplhabets symbols
        - Expect 
            True, 
            False and 
            None 
        all are lower case
        """
    )
    st.code(
        """
        import keywords
        print(keywords.kwlist)       
        """    
    )

if page == 'Python Variables':
    st.header("Variable")

    st.info(
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
    st.subheader("Creating Python Variables")
    st.code(
        """
        # In interactive Mode
        counter = 100          # Creates an integer variable
        miles   = 1000.0       # Creates a floating point variable
        name    = "Codelocked" # Creates a string variable
        """
    )

    st.subheader("Printing Python Variables")
    st.code(
        """
        # In Script Mode
        rain = True
        print(rain)

        # In interactive Mode
        >>> rain = "Y"
        >>> rain
        'Y'
        >>>
        """
    )

    st.subheader("Deleting variable")
    st.code(
        """
        # In interactive Mode
        student1, student2, student3 = "raahool", "supriya", "rashmika"
        print(student1, student2, student3)

        del student1, student2, studnet3
        print(student1, student2, studnet3)

        """
    )

    st.subheader("Multiple Assignments")
    st.code(
        """
        # In interactive Mode
        a = b = c = 100
        
        a,b,c = 1,2,"Codelocked"
        """
    )

    st.subheader('Local vs Global variable')

    st.code(
        """
        # In Script Mode
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
    st.header("Python Numeric Data Type")
    st.code(
        """
        # int,long,float,complex --> Py2
        # int, float,complex     --> py3
        
        # int (signed integers)
        # long (long integers)
        # float (floating point real values)
        # complex (complex numbers)

        a,b,c = 100,20.45,10+4j
        print(a,type(a))
        print(b,type(b))
        print(c,type(c))
        """
    )

    st.subheader("Python String Data Type")
    st.code(
        """
        str = "Codelocked"

        print(str)
        print(str[0],str[1:],str[2:5])
        # Repition on string with * operator
        print(str * 2) 
        # String concatenation with _ Operator
        print(str[0:4]+"Un"+str[4:])
        """
    )

    st.subheader("Python List Data Type")
    st.code(
        """
        # Most Versatile compound data types
        list = ["codelocked", 12, 23, 24.0, 9+4j]
        print(list[0])
        print(list[:])
        print(list[1:3])
        print(list[2:])
        print(list* 2)
        print(list + list)
        """
    )
    st.subheader("Python Tuple Data Type")
    st.code(
        """
        tuple = ("codelocked", 12, 23, 24.0, 9+4j)
        print(tuple[0])
        print(tuple[:])
        print(tuple[1:3])
        print(tuple[2:])
        print(tuple* 2)
        print(tuple + tuple)
        """
    )
    st.subheader("Python Ranges")
    st.code(
        """
        # range(start, stop, step)

        for i in range(5):
            print(i)
        """
    )

    st.subheader("Python Dictionary")
    st.code(
        """
        # Kind of hash table type

        dict = {}
        dict['one'] = "This is one"
        dict[2]     = "This is two"

        tinydict = {'name': 'john','code':6734, 'dept': 'sales'}

        print (dict['one'])       # Prints value for 'one' key
        print (dict[2])           # Prints value for 2 key
        print (tinydict)          # Prints complete dictionary
        print (tinydict.keys())   # Prints all the keys
        print (tinydict.values()) # Prints all the values
        """
    )

    st.subheader("Python Boolean Data Types")
    st.code(
        """
        a = True
        # display the value of a
        print(a)

        # display the data type of a
        print(type(a))
        """

    )

    st.header("Python Data Type Conversion")
    st.subheader("Convert to int")
    st.code(
        """
        a = int(input("Enter Number :"))
        vs
        a = int(float(input("Enter Number :")))
        
        """
    )

    st.header("Data Type Conversion Functions")
    st.markdown(
        """
        Sr. No.|function | description|
        |----|---------|-----------|
        |1|int(x [,base])|Converts x to an integer. base specifies the base if x is a string.|
        |2|long(x [,base] )| Converts x to a long integer. base specifies the base if x is a string.|
        |3|float(x)|Converts x to a floating-point number.|
        |4|complex(real [,imag])|Creates a complex number.|
        |5|str(x)|Converts object x to a string representation.|
        |6|repr(x)|Converts object x to an expression string.|
        |7|eval(str)|Evaluates a string and returns an object.|
        |8|tuple(s)|Converts s to a tuple.|
        |9|list(s)|Converts s to a list.|
        |10|set(s)|Converts s to a set.|
        |11|dict(d)|Creates a dictionary. d must be a sequence of (key,value) tuples.|
        |12|frozenset(s)|Converts s to a frozen set.|
        |13|chr(x)|Converts an integer to a character.|
        |14|unichr(x)|Converts an integer to a Unicode character.|
        |15|ord(x)|Converts a single character to its integer value.|
        |16|hex(x)|Converts an integer to a hexadecimal string.|
        |17|oct(x)|Converts an integer to an octal string.|
        """
    )

if page == "Types of Python Operators":
    st.header("Python language supports the following types of operators.")
    st.success("""
        #### Arithmetic Operators
        `+ - * / % ** //`
        """)
    st.success("""
        #### Comparison (Relational) Operators
        `== != > < >= <=`
        """)
    st.success("""    
        #### Assignment Operators
        `= += -= *= /= %= **= //=`
                       """)
    st.success("""
        #### Logical Operators
        and 
        
        or
        
        NOT
        """)
    st.success("""
        #### Bitwise Operators
            & 
            | 
            ^ 
            ~ 
            << 
            >>
                    """)
    st.success("""
        #### Membership Operators
        in 
        not in
         """)
    
    st.success("""
        #### Identity Operators
        is  
        is not
               
        """
    )

    st.subheader("Python Operators Precedence")
    st.markdown(
        """
        |Operator|Description|
        |---------|---------|
        |**                 | |Exponentiation (raise to the power)    |
        |~ + -             |  Complement, unary plus and minus (method names for the last two are +@ and -@)|
        |* / % //         |    Multiply, divide, modulo and floor division|
        |+ -             |                Addition and subtraction|
        |>> <<          |                 Right and left bitwise shift|
        |&                            |   Bitwise 'AND'|
        |^   \|                         |    Bitwise exclusive `OR' and regular `OR'|
        |<= < > >=                  |     Comparison operators|
        |<> == !=                  |      Equality operators|
        |= %= /= //= -= += *= **= |       Assignment operators|
        |is is not        |               Identity operators|
        |in not in       |                Membership operators|
        |not or and     |                 Logical operators|
        """
    )


if page == "Assignment":
    
    st.header("HACKER-RANK")
    st.info(
        """
     
        1. https://www.hackerrank.com/challenges/python-arithmetic-operators/problem?isFullScreen=true

        2. https://www.hackerrank.com/challenges/python-division/problem?isFullScreen=true

        3. https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true

        """)
    
    st.header("Write code")

    st.subheader("Develop Calculator program in Python")
    st.info(
        """
        - Should Addition, multiplication, division and substraction 
        - Extra creadt for well written program
        - Extra credit for use of interactive program 
        """
    )