# Logging exceptions

#### Use exc_info to include exception information

```
>>> import logging 
>>> try:
...    ...
... except Exception:
...    logging.error("An error occured", exc_info=True)
... 
Ellipsis
>>> 
```

```
try:
    ...
except UnrecoverableError:
    logging.exception("An error occured")
except Exception:
    logging.info("An error occured", exc_info=True)
    raise
```

```
try:
    dict()['nope']
except KeyError as e:
    logging.error("An error occured : %e", e)
```

### Scoping of the except
```
try:
    1/0
except ZeroDivisionError as e:
    pass

print(e)

# PEP 3110
# in short : exception -> traceback -> stack frame -> exception
```

### The tricky, raise within exception
```
>>> try:
...     1/0
... except Exception:
...     raise Exception("I failed to handle this")
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
Exception: I failed to handle this
>>> 
```

### reraise
```
>>> try:
...     1/0
... except Exception:
...     print("Nothing to see here, keep moving")
...     raise 
... 
Nothing to see here, keep moving
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ZeroDivisionError: division by zero
>>> 
```

### Chaining exception 
```
>>> try:
...     1/0
... except Exception as e:
...     raise Exception("We don't know how to divide") from e
... 
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ZeroDivisionError: division by zero

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
Exception: We don't know how to divide
```

### Eliding previous exception
```
>>> try:
...     1/0
... except Exception:
...     raise Exception("Something went bad dividing") from None
... 
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
Exception: Something went bad dividing
```

# Exception Atrributes
```
>>> try:
...     1/0
... except Exception as exc:
...     e = exc
... 
>>> e.message  # Was there in Py2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'ZeroDivisionError' object has no attribute 'message'
>>> e.
e.args             e.with_traceback(  
>>> e.args
('division by zero',)
>>> 
>>> e.with_traceback(None)
ZeroDivisionError('division by zero')
```

# Creating New classes
```
>>> class MyreallyCoolError(Exception):
...       pass
... 
>>> class MyCoolError(BaseException):
...      pass
... 

```