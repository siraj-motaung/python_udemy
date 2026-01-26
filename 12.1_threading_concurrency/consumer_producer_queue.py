"""
When you have two functions where one depends on the output of the other, 
you are dealing with a Producer-Consumer relationship.
"""

import threading
import queue
import time
# The queue.Queue object is specifically designed for multi-threaded communication. 
# It handles the "waiting" for you automatically.

# The queue to hold the output of function_one
data_queue = queue.Queue()

def function_one():
    print("Function 1: Processing data...")
    time.sleep(2) # Simulating heavy work, producing "result"
    result = "Clean data"
    print(f"Function 1: Produced {result}")
    data_queue.put(result)

def function_two():
    print("Function 2: Waiting for data...")
    # .get() will block/pause this thread until data is available
    input_data = data_queue.get()
    print(f"Function 2: Received {input_data}. Starting second phase...")
    time.sleep(1)
    print("Function 2: Task complete.")


# Create threads
t1 = threading.Thread(target=function_one)
t2 = threading.Thread(target=function_two)

t1.start()
t2.start()

t1.join()
t2.join()

