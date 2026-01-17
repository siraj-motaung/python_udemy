class InvalidChaiError(Exception):
    pass

def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40}

    try:
        if flavor not in menu:
            raise InvalidChaiError("That chai is not available")
        if not isinstance(cups, int):
            raise TypeError("The number of cups must be an integer")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} of {flavor} chai: rands {total}")
    except Exception as e:
        print("Error: ", e)
    finally:
        print("Thank you for visiting chaicode!")


bill("mint", 2)
print("----------------------------")
bill("masala", "three")
print("-----------------------------")
bill("Ginger", 3)
