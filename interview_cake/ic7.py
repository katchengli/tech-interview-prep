class TempTracker(object):
    def __init__(self):
        self.record = [0 for x in range(111)]
        self.nbRecords = 0
        self.total = 0.0
        self.max = None
        self.min = None
        self.mode = None
        self.mean = None
        self.highestFreq = 0

    def insert(self, temp):
        if self.min == None:
            self.min = temp
        elif temp < self.min:
            self.min = temp
        if self.max == None:
            self.max = temp
        elif temp > self.max:
            self.max = temp

        self.nbRecords += 1
        self.total += temp
        self.mean = self.total/self.nbRecords
        self.updateMode(temp)

    def get_max(self):
        return self.max

    def get_min(self):
        return self.min

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode

    def updateMode(self, temp):
        self.record[temp] += 1

        if self.record[temp] > self.highestFreq:
            self.highestFreq = self.record[temp]
            self.mode = temp

t = TempTracker()
t.insert(2)
t.insert(5)
t.insert(100)
t.insert(9)
t.insert(5)
t.insert(2)
t.insert(2)
print('mode: ' + str(t.get_mode()))
print('mean: ' + str(t.get_mean()))
print('min: ' + str(t.get_min()))
print('max: ' + str(t.get_max()))
