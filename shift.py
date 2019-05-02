class Shift(object):
   
    def __init__(self, id, start, end):
        self.id = id
        self.start = start
        self.end = end
        self.duration = end - start
        self.overlaps = []

    def printShift(self):
        
        for i in range(self.start):
            print("   ", end='') # this space is equivalent to one hour
        for i in range(self.duration):
            print("---", end='') # this space is equivalent to one hour
        
        for i in range(self.end, 24):
            print("   ", end='')
        
        print(self.id)
    
    def __repr__(self):
        return str(self.id) 