class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Create serializer with start"""
        self.start = start
        self.current_num = start
        self.firstGeneration = True

    def generate(self):
        """Returns the next sequential number, starting from start"""
        if self.firstGeneration:
            self.firstGeneration = False
            return self.start
        else:
            self.current_num += 1
            return self.current_num


    def reset(self):
        """Reset the number back to the original start"""
        self.current_num = self.start
        self.firstGeneration = True
