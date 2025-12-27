
#Comparison: Function vs. Module Docstrings
# Level	      |     Where to write it?             |  	How to access?
# Module.        Very first line of the file.          module_name.__doc__
# Class          First line inside the class block.    ClassName.__doc__
# Function       First line inside the def block.      function_name.__doc__

# 
import sys

"""
This is the module-level docstring.
It explains what this script does.
"""


# function.__doc__ returns a function doc string that is within a fuction.

def chai_flavor(flavor="Masala"):
    """
    Return the flavor of chai 
    """

    return flavor

print(f"Print module level documentation: {__doc__}")
print(f"Print function level documentation: {chai_flavor.__doc__}")
print(f"Print documentation of an imported module(sys): {sys.__doc__}")
print(f"Print documentation of an imported module(sys): {help(sys)}")
print(chai_flavor.__name__)




