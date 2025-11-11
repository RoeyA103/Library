class a:
    def __init__(self):
        self.__b = True

    def __dict__(self):
        self.d = "assa"

aa = a()
print(a.__dict__)