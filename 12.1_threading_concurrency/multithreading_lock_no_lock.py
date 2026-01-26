import threading
import time

# A shared global variable
counter = 0

def increment_without_lock():
    global counter
    for _ in range(100000):
        # We manually break the operation into steps 
        # to ensure a thread switch can happen in between
        current_val = counter
        # Adding a sleep(0) tells the OS "you can switch threads now"
        import time
        time.sleep(0)
        counter = current_val + 1

def increment_with_lock(lock):
    global counter
    for _ in range(100000):
        # The 'with lock' statement acts as a Mutex.
        # It ensures the thread completes the increment before being swapped out.
        with lock:
            current_val = counter
            # Adding a sleep(0) tells the OS "you can switch threads now"
            import time
            time.sleep(0)
            counter = current_val + 1


# --- SCENARIO 1: HIGH RISK (No Mutex) ---
counter = 0
threads = []
for i in range(2):
    t = threading.Thread(target=increment_without_lock)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"Final count WITHOUT lock: {counter}")
print("Result is likely NOT 200,000 due to race conditions.")

# --- SCENARIO 2: SAFE (Using Mutex) ---
counter = 0
thread_lock = threading.Lock()
threads = []
for i in range(2):
    t = threading.Thread(target=increment_with_lock, args=(thread_lock,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(f"\nFinal count WITH lock: {counter}")
print("Result is GUARANTEED to be 200,000.")