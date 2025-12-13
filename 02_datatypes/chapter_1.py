sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")

sugar_amount = 12
print(f"Initial sugar: {sugar_amount}")

# The value did not change but rather what changed is the referrence. Never check immutability by value but rather by identity.
# In memory the 2 still exists

#Demo
print(f"ID of 2: {id(2)}")
print(f"ID of 12 {id(12)}")
