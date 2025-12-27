def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups poured"

    return pour_chai(n-1)

print(pour_chai(5))


chai_types = ["Siraj", "Shameel", "Ginger", "Kadak", "Ginger"]

strong_chai = list(filter(lambda chai: chai != "Ginger" , chai_types))

print(strong_chai)




