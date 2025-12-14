#Mutability

spice_mix = set()
print(f"Inital spice mix id: {id(spice_mix)}")
spice_mix.add("Ginger")
spice_mix.add("Cardamom")
spice_mix.add("Lemon")

#Checking id in memory
print(f"After spice mix id: {id(spice_mix)}")
