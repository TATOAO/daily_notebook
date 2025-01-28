
import time
import threading

def background_work():
    for _ in range(10):
        # do something
        time.sleep(0.5)
        print('background_work')


def frontground_work():
    for _ in range(4):
        # do something
        time.sleep(0.4)
        print('front ground_work')

    print('front finished')


def main():
    t = threading.Thread(target=background_work, daemon=True)
    t.start()
    t2 = threading.Thread(target=frontground_work, daemon=True)
    t2.start()
    
if __name__ == "__main__":
    main()

