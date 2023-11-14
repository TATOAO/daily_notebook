class Father:
    def __init__(self):
        self.function_list = []

    def register(self, func):
        self.function_list.append(func)
        return func

class Son(Father):
    def __init__(self):
        super().__init__()

    @Father.register
    def functionA(self):
        pass

    @Father.register
    def functionB(self):
        pass

class Son_2(Father):
    def __init__(self):
        super().__init__()

    @Father.register
    def functionC(self):
        pass

# Access the list of registered functions from each Son class
son1 = Son()
son2 = Son_2()

print(son1.function_list)  # Contains functionA and functionB
print(son2.function_list)  # Contains functionC


