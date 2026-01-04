class Chai:
    """
    Docstring for Chai
    """
    origin = "India"

Chai.is_hot = True #Adding more property to Chai class

print(Chai.origin)
print(Chai.is_hot)

#creating objects from class chai

masala = Chai() #Instance namespace
print(f"Masala {masala.origin}")
print(f"Masala {masala.is_hot}")


# The instance variable now shadows the class variable. Because Python finds is_hot in the instance namespace first, 
# it stops looking and never reaches the class-level True.

# 2. The Lookup Hierarchy (LEGB Rule)
#   When you try to access a variable, Python looks through namespaces in a specific order. For classes, it follows a simplified version of this chain:
#   Instance Namespace: Does the specific object (e.g., my_robot) have this attribute?
#   Class Namespace: If not, does the class (e.g., Robot) have it?
#   Base Class Namespace: If the class inherits from another, it checks the parent class.

masala.is_hot = False
print("Class: ", Chai.is_hot) # Class namespace is True
print(f"Masala {masala.is_hot}") # Instance namespace is False.


# See the "Secret" dictionaries
print("CHAI CLASS NAMESPACE:", Chai.__dict__)
print("MASALA INSTANCE NAMESPACE:", masala.__dict__)
