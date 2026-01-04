"""
When you use yield as an expression (on the right side of an assignment), the generator "pauses" at the yield and waits. 
When the caller calls .send(value), that value becomes the result of the yield expression inside the generator.
"""


def chai_customer():
    print("Welcome! What chai would you like ?")

    order = yield
    while True:
        print(f"Preparing: {order}")
        order = yield

stall = chai_customer()
next(stall) #start the generator

stall.send("Masala Chai")
stall.send("Lemon Chai")