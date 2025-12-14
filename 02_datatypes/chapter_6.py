chai_type = "Ginger chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} please !")

chai_description = "Aromatic and Bold"

print(f"First word: {chai_description[:8]}")
print(f"last word: {chai_description[12:]}")
print(f"reverse: {chai_description[::-1]}")

#Including special characters/other languages to be represented in python.

label_text = "Chai Spécial"
encoded_label = label_text.encode("utf-8")
decoded_label = encoded_label.decode("utf-8")
print(f"Non encoded label: {label_text}")
print(f"Encoded label: {encoded_label}")
print(f"Decoded label: {decoded_label}")

