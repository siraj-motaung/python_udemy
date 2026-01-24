"""
Two threads accessing the same memory
"""


import threading

# shared_array = [0]

# def increment_array():

#     print(f"{threading.current_thread().name} starting operation")
#     for _ in range(100000):
#         import time
#         time.sleep(0)
#         shared_array[0]+=1
#     print(f"{threading.current_thread().name} finishing operation")
    

# t1 = threading.Thread(target=increment_array, name="t1")
# t2 = threading.Thread(target=increment_array, name="t2")

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print(f"Final array value: {shared_array[0]}")

counter = 0
import time

thread_lock = threading.Lock()

def increment_with_lock():
    global counter

    for _ in range(100000):

        #with thread_lock:
        current_val = counter
        time.sleep(0)
        counter = current_val + 1
        print(f"Its not thread {threading.current_thread().name}s turn")



threads = []

for i in range(3):
    t = threading.Thread(target=increment_with_lock, name=f"thread #{i}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(threads)
print(f"Counter - {counter}")





    