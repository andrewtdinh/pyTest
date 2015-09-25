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

    # Method to update the instance variable tagDict.  The key determines which set to add the term to.
    def addTag(self, key, tag):
        if key in self.tagDict:
            self.tagDict[key].add(tag)
        else:
            self.tagDict[key] = set([tag])

    # Method to remove an existing tag from tag dictionary
    def removeTag(self, term):
        for key, seet in self.tagDict.items():
            if term in seet:
                self.tagDict[key].remove(term)
            else:
                continue

    # Method to remove a key-value pair from the dictionary
    def removeKeyValuePair(self, key):
        self.tagDict.pop(key, None)
