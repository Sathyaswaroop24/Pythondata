Let's just raise an exception ?

```
raise Exception("Broken Code")
```

```
try:
    ...
expect KeyError:
    # rasie Exception("Broken code")
    rasie CustomException("Broken code") as None
```

```
try:
    ...
expect RuntimeError:
    ...
expect (KeyError, ValueError):
    ...
expect:
    ...
```

### Actaully we can put anything with expect
exception_in_variable = Exception
def exception_f():
    return Exception

```
try:
    ...
except exception_in_variable:
    ...
except exception_f:
    ...
except non_existing_exception:
    ...
```

#### using finally
```
try:
    ...
except Exception:
    print("Failed")
finally:
    print("finished")
```

#### using else
```
try:
    ...
except Exception:
    print("Failed")
else:
    print("Succeed")
```

