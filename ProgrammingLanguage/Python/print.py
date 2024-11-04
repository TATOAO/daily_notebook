import time

# Using flush=False (default)
for i in range(3):
    print('\r', i, end=" ", flush=False)
    time.sleep(1)

print("\n")

# Using flush=True
for i in range(3):
    print('\r', i, end=" ", flush=True)
    time.sleep(1)

