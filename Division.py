# This function adds two numbers
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both inputs must be numbers."
    else:
        return result