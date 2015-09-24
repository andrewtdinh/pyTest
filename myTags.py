#Define an updateable dictionary.  This is according to requirement 1.1
class myDict:
    def __init__(self):
        self.tagDict = {'NAME': set(['jack', 'jill']), 'NUM': set(['one', 'two', 'three', 'four', 'nine'])}

    # Method to search for a term in the dictionary and return the key if found
    def findKey(self, term):
        for key, seet in self.tagDict.items():
            if term in seet:
                return key
            else:
                continue
