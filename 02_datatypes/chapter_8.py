
ingredients = ["Water", "Milk", "Black tea"]
ingredients.append("Sugar")
print(f"Ingredients are: {ingredients}")

ingredients.remove("Water")
print(f"Ingredients are: {ingredients}")

ingredients.insert(0, "Moraj")
print(f"Ingredients are: {ingredients}")

# Operator overloading: An operator being used to do more than one task.
# Operator overloading is a concept in programming that allows you to redefine 
# or customize the way standard operators (like 1$+, -, *, /, =, <, >,$ etc.) 
# behave when applied to user-defined data types (objects of classes)

base_liquid = ["water", "milk"]
extra_flavor = ["Ginger"]
full_flavor = base_liquid + extra_flavor

print(f"Operator overload {full_flavor}") # Operator overload ['water', 'milk', 'Ginger']

strong_brew = ["Siraj"] * 3 # strong brew ['Siraj', 'Siraj', 'Siraj']
print(f"strong brew {strong_brew}")

strong_brew2 = ["Siraj", "Motaung"] * 3 # strong brew2 ['Siraj', 'Motaung', 'Siraj', 'Motaung', 'Siraj', 'Motaung']
print(f"strong brew2 {strong_brew2}") 
