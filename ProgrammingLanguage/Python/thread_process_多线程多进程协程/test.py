import multiprocessing
import time
import random
import ctypes

# bar
def bar():
    for _ in range(100):
        print("Tick")
        time.sleep(1)



class Model():
    def __init__(self) -> None:
        self.saved_data = [9, 2]

    def generation(self):

        print('model', ctypes.addressof(self))
        print('list', id(model.saved_data))
        while True:
            # self.saved_data.append(random.randint(0, 10))
            self.saved_data.append(1)
            print(self.saved_data)
            time.sleep(1)

if __name__ == '__main__':
    # Start bar as a process
    model = Model()

    print('model', id(model))
    print('list', id(model.saved_data))
    p = multiprocessing.Process(target=model.generation)
    p.start()

    # Wait for 10 seconds or until process finishes
    p.join(5)

    # If thread is still active
    if p.is_alive():
        print("running... let's kill it...")

        print('model', id(model))
        print('list', id(model.saved_data))
        # Terminate - may not work if process is stuck for good
        p.terminate()
        # OR Kill - will work for sure, no chance for process to finish nicely however
        # p.kill()

        p.join()


        print(model.saved_data)


# 结论 
