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

        specialChars = ["'", ",", "."]
        processedInStr = inputString
        for ch in specialChars:
            processedInStr = ' '.join(processedInStr.strip().lower().split(ch))
        # Convert everything in the string to lower case and split into list of terms
        terms = processedInStr.strip().split(' ')
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
        return "'".join(' '.join(self.replacedStr).split(" '"))

    # This method will add a tag to a key-value pair and then re-initialize the object
    def addTagToDict(self, key, tag):
        tags.addTag(key, tag)
        self.__init__(self.originalStr)

    # This method will remove a tag from specified key-value pair and then re-initialize the object
    def removeTagFromDict(self, tag):
        tags.removeTag(tag)
        self.__init__(self.originalStr)

    # This method will remove a key value pair from the dictionary and then re-initialize the object
    def removeKeyFromDict(self, key):
        tags.removeKeyValuePair(key)
        self.__init__(self.originalStr)

myStr = Taggerizer("I am Jack and I am three years old")
myStr3 = Taggerizer("  This is Jill's and Jack's sentence with leading and trailing spaces.   ")
print myStr.getOrinalStr()
print myStr.getUntaggedStr()
print myStr.getTagStr()
print myStr.getSubStr()
print myStr3.getOrinalStr()
print myStr3.getUntaggedStr()
print myStr3.getTagStr()
print myStr3.getSubStr()
# myStr2 = Taggerizer("I'm Jack and I'm three years old")
# myStr2.addTagToDict('CONN', 'and')
# print myStr2.getOrinalStr()
# print myStr2.getUntaggedStr()
# print myStr2.getTagStr()
# print myStr2.getSubStr()
# myStr2.removeTagFromDict('jack')
# print myStr2.getOrinalStr()
# print myStr2.getUntaggedStr()
# print myStr2.getTagStr()
# print myStr2.getSubStr()
# myStr2.removeKeyFromDict('CONN')
# print myStr2.getOrinalStr()
# print myStr2.getUntaggedStr()
# print myStr2.getTagStr()
# print myStr2.getSubStr()
