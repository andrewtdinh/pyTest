import unittest
from myTags import myDict

class Taggerizer:
    global tags
    tags = myDict()

    def __init__(self, inputString):
        self.originalStr = inputString

        # The next two instance variables are sets because we want unique values inside
        self.taggedTerms = set()
        self.untaggedTerms = set()

        # The next variable is a list because we want the terms to be in the order we add them
        self.replacedStr = []

        # Convert everything in the string to lower case and split into list of terms
        terms = self.originalStr.lower().split(' ')
        for term in terms:
            foundKey = self.getDictKey(term)

            # If a tag is found in our tag dictionary:
            if foundKey:
                # We add the search term into the set of tags
                self.taggedTerms.add(term)
                # We add the returned key to the list of replaced string
                self.replacedStr.append(foundKey)
            else:
                # Else we just add the search term to the list of replaced string
                self.replacedStr.append(term)
                # And also add the search term into the set of non-tags
                self.untaggedTerms.add(term)

    # This will be used later to search for and get the key in the tagDict
    def getDictKey(self, term):
        return tags.findKey(term)

    # This method will return the original string
    def getOrinalStr(self):
        return self.originalStr

    # This method will return the non-tag terms
    def getUntaggedStr(self):
        return ' '.join(self.untaggedTerms)

    # This method will return the tag terms
    def getTagStr(self):
        return ' '.join(self.taggedTerms)

    # This method will return key-substituted string
    def getSubStr(self):
        return ' '.join(self.replacedStr)

myStr = Taggerizer("I am Jack and I am three years old")
print myStr.getOrinalStr()
print myStr.getUntaggedStr()
print myStr.getTagStr()
print myStr.getSubStr()
