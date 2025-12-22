

# value = 13

# if remainder := value % 5:
#     print(f"Not divisible, remainder is {remainder}")


# available_sizes = ["small", "medium", "large"]

# if (req_size := input("Enter your cup: ")) in available_sizes:
#     print(f"Serving {req_size} chai")
# else:
#     print(f"Size is unavailable - {available_sizes}")


flavors = ["masala", "ginger", "Lemon", "Mint"]

while (flavor := input("Choose your flavors: ")) not in flavors:
    print(f"Sorry, {flavor} not available")

print(f"You choos {flavor}")
