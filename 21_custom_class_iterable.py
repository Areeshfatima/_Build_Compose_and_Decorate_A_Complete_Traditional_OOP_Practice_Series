# Make a Custom Class Iterable

class Countdown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self      # The object itself is the iterator
    
    def __next__(self):
        if self.current < 0:
            raise StopIteration   # Stop when countdown goes below 0
        value = self.current
        self.current -= 1
        return value
    
for num in Countdown(8):
    print(num)
