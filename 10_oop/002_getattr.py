"""
getattr(object, name) is a built-in function that allows you to access an attribute using a string. 
This is incredibly useful when you don't know the attribute name until the code is actually running
 (e.g., reading from a configuration file or user input).
"""

class MedicalWaste:
    def __init__(self):
        self.category = "Infectious"
        self.treatment = "Autoclave"

bin_1 = MedicalWaste()

# Normal access
print(bin_1.category)

# Dynamic access using a string
attribute_name = "treatment" 
print(getattr(bin_1, attribute_name)) # Prints "Autoclave"(bin_1.treatment)

# Safe access with a default value (prevents AttributeError)
print(getattr(bin_1, "volume", "Attribute not found"))
