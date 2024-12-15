
import time

def a_simple_generator():

    for i in range(1,4):
        time.sleep(1)
        print(f'have wait {i} second')
        yield i


def a_simple_from_generator():

    print('what?')
    yield from a_simple_generator()


def main():
    # aaa = a_simple_from_generator()
    aaa = a_simple_generator()

    print(next(aaa))

    bbb = aaa.send('real_shit')
    print('this is bbb', bbb)


    print(next(aaa))
    print(next(aaa))

if __name__ == "__main__":
    main()

