class Shift(object):
   
    def __init__(self, id, start, end):
        self.id = id
        self.start = start
        self.end = end
        self.duration = end - start
        self.overlaps = []
        self.isSupervised = False

    def printShift(self):
        print(self.id, end='')
        for i in range(self.start):
            print("   ", end='') # this space is equivalent to one hour
        for i in range(self.duration):
            print("---", end='') # this space is equivalent to one hour

        print(" ")