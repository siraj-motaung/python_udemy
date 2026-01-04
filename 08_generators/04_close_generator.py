def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Rooibos"
    yield "Joko"

def full_menue():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menue():
    print(chai)

def chai_stall():
    try:
        while True:
            order = yield "waiting for chai order"
            print(f"My {order}")
    except:
        print("Stall closed, No more chai")

stall = chai_stall()
print(next(stall))
stall.send("YOOOOOH")
stall.send("YO2")
stall.close()