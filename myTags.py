class myDict:
    def __init__(self):
        self.tagDict = {'NAME': set(['jack', 'jill']), 'NUM': set(['one', 'two', 'three', 'four', 'nine'])}

    def findKey(self, term):
        for key, seet in self.tagDict.items():
            if term in seet:
                return key
            else:
                continue
