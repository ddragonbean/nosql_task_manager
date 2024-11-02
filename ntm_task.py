class NtmTask:
    def __init__(self):
        pass

    def set(self, **kwargs):
        self.kwargs = kwargs
        for key, value in kwargs.items():
            print(key, ":", value)

    def get(self):
        return self.kwargs

    def get(self, property):
        if self.kwargs == None:
            return ""
        else:
            return self.kwargs.get(property)

if __name__ == '__main__':
    t = NtmTask()
    t.set(a="a", b="b")
    print(t.get("a"))
    print(t.get("c"))