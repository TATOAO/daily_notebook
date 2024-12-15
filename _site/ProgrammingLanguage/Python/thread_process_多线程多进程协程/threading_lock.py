

import threading
import time
import random

counter = {'count': 0}
def increment_counter(counter_dict, seed):
    random.seed(seed)
    for _ in range(1000):
        # current_count = counter_dict['count']
        global counter
        tmp = counter['count']
        # Simulate a delay

        print('before', tmp,  seed)
        time.sleep(random.random() * 0.001)
        print('after', tmp, seed)
        # counter_dict['count'] = current_count + seed
        counter['count'] = tmp + seed
        time.sleep(random.random() * 0.001)
    return 0

# Create threads
thread1 = threading.Thread(target=increment_counter, args=(counter,1.0))
thread2 = threading.Thread(target=increment_counter, args=(counter,2.0))

# Start threads
thread1.start()
thread2.start()

# Wait for threads to finish
thread1.join()
thread2.join()

print(f"Final count: {counter['count']:,.0f}")

