import unittest

class Taggerizer:
    #Define an updateable dictionary.  This is according to requirement 1.1
    tagDict = {'NAME': set(['Jack', 'Jill']), 'NUM': set(['one', 'two', 'three', 'nine'])}


    def __init__(self, inputString):
        self.originalStr = inputString
        self.taggedTerms = set()
        self.untaggedTerms = set()
        self.replacedStr = []
        terms = self.originalStr.lower().split(' ')
        for term in terms:
            foundKey = self.getDictKey(term)
            if foundKey:
                self.taggedTerms.append(term)
                self.replacedStr.append(foundKey)
            else:
                self.replacedStr.append(term)
                self.untaggedTerms.append(term)

    #This will be used later to search for and get the key in the tagDict
    def getDictKey(self, term):
        for key, s in tagDict.items():
            if term in s:
                return key

    def getOrinalStr(self):
        return self.originalStr

    def getUntaggedStr(self):
        return ' '.join(self.untaggedTerms)

    def getTagStr(self):
        return ' '.join(self.taggedTerms)

    def getSubStr(self):
        return ' '.join(self.replacedStr)

    # def processStr(self):
    #     terms = self.originalStr.lower().split(' ')
    #     for term in terms:
    #         foundKey = self.getDictKey(term)
    #         if foundKey:
    #             self.taggedTerms.append(term)
    #             self.replacedStr.append(foundKey)
    #         else:
    #             self.replacedStr.append(term)
    #             self.untaggedTerms.append(term)

myStr = Taggerizer("I am Jack and I am three years old")
print myStr.getOrinalStr()
print myStr.getUntaggedStr()
print myStr.getTagStr()
print myStr.getSubStr()
