"""
The fundamental difference between a normal function and a generator is how they handle memory and state. 
A normal function calculates all its results and returns them at once in a container (like a list). 
A generator calculates one result at a time, "pauses" its execution, and yields the value to the caller, 
only resuming when the next value is requested.
"""



def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Rooibos Chai"

# stall = serve_chai()

# for cup in stall:
#     print(cup)

def get_chai_gen():
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"

chai = get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))
# print(next(chai)) Give error(StopIteration)