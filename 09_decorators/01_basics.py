# The line from functools import wraps is used specifically to solve a "hidden" problem with decorators: metadata loss.
# WITHOUT @wraps
# @my_decorator
# def greet():
#     """This function says hello."""
#     print("Hello!")
# print(greet.__name__)  # Prints: 'wrapper' (Oops!)
# print(greet.__doc__)   # Prints: None (The docstring is gone!)

# wraps is a decorator for your decorator. It "copies" the identity(Preserves metadata) of the original function (its name, docstring, and arguments)
# onto the wrapper so that the function still looks like itself after being decorated.

# from functools import wraps

# def my_decorator(func):
#     @wraps(func)  # <--- This copies metadata from 'func' to 'wrapper'
#     def wrapper(*args, **kwargs):
#         print("Before function runs")
#         result = func(*args, **kwargs)
#         print("After function runs")
#         return result
#     return wrapper

# @my_decorator
# def greet():
#     """This function says hello."""
#     print("Hello!")

# print(greet.__name__)  # Now correctly prints: 'greet'
# print(greet.__doc__)   # Now correctly prints: 'This function says hello.'


from functools import wraps

def my_decorator(func):

    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    
    return wrapper

@my_decorator
def greet():
    print("Hello from decorators class from chaicode")

greet()
print(greet.__name__)
