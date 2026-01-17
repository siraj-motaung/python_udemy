
#Print will run because we did not raise anything.
def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "elaichai"]:
        print("HI")
        #raise ValueError("Unsupported chai flavor...")
    print(f"brewing {flavor} chai...")


#Will stop execution and print won't run
def brew_chai_raise(flavor):
    if flavor not in ["masala", "ginger", "elaichai"]:
        print("HI")
        # Execution will stop here.
        raise ValueError("Unsupported chai flavor...")
    print(f"brewing {flavor} chai...")

brew_chai("mint")
brew_chai_raise("mint")


