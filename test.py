class t:
    def __init__(self):
        self.id=1000
        self.name="tom"
        self.__sal=10000
    def view(self):
            print(self.__sal)
tr=t()
print(tr.__sal  )
