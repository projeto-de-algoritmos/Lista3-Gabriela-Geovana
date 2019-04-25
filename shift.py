class Shift(object):
   
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.duration = end - start

    def printShift(self):
        for i in range(self.start):
            print("   ", end='') # this space is equivalent to one hour
        for i in range(self.duration):
            print("---", end='') # this space is equivalent to one hour

        print(" ")