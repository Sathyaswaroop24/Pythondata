# Custom module for calculator

def calc(operation:str, x: int, y:int) -> str:
    """
    Accepts operation
    """
    if operation.lower() == 'add':
        return f"Addition is {x + y}"
    elif operation.lower() == "sub":
        return f"Subtraction is {x - y}"
    elif operation.lower() == "mul":
        return f"Multiplications is {x * y}"
    elif operation.lower() == "div":
        return f"Division in {x / y}"
    else:
        return "Case not found!"