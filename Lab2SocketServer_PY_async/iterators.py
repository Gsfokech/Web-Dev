class InfiniteSquaring:
    def __init__(self, init_num):
        self.numToSqr = init_num

    def __next__(self):
        self.numToSqr = self.numToSqr**2
        return self.numToSqr
    
    def __iter__(self):
        return self
    
squares = InfiniteSquaring(6)
aq = next(squares)
print(aq)