class MedicalContainer:
    def __init__(self):
        self.type = "Bio-Hazardous Waste"
    
    def load(self):
        print("--- [!] High Security: Loading sealed red medical bins")
    
    def unload(self):
        print("--- [!] Safety Check: Unloading at Incinerator facility")

class RecycleContainer:
    def __init__(self):
        self.type = "Paper and Plastic"

    def load(self):
        print("--- [+] Loading general recyclables into the hopper.")

    def unload(self):
        print("--- [+] Unloading at the Sorting Plant.")


class Truck:
    def __init__(self, name, container):
        self.name = name
        self.container = container  
    
    def work(self):
        print(f"\n Truck '{self.name}' is starting its shift with {self.container.type}.")
        self.container.load()
        self.container.unload()

med_bin = MedicalContainer()
blue_bin = RecycleContainer()

job_1 = Truck("JHB-Waste-01", med_bin)
job_1.work()

print("\n[SYSTEM UPDATE]: Swapping containers for the next shift.")

job_1.container = blue_bin

job_1.work()



