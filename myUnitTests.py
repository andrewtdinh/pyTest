import unittest
from myTagProcessor import Taggerizer

class TestTagProcessor(unittest.TestCase):
    global testObj, anotherObj, thirdObj, fourthObj
    testObj = Taggerizer("I am Jack and I am three years old")
    anotherObj = Taggerizer("  This is Jill's and Jack's sentence, with leading and trailing spaces.   ")
    thirdObj = Taggerizer("  This is Jill's and Jack's sentence, with leading and trailing spaces.   ")
    fourthObj = Taggerizer("This is Jill's and Jack's sentence, with three trailing spaces.   ")

    def test_getDictKey(self):
        self.assertEqual(testObj.getDictKey('jack'), 'NAME')
        self.assertEqual(testObj.getDictKey('jill'), 'NAME')
        self.assertEqual(testObj.getDictKey('three'), 'NUM')
        self.assertEqual(anotherObj.getDictKey('jill'), 'NAME')
        self.assertEqual(anotherObj.getDictKey('jack'), 'NAME')
        self.assertEqual(anotherObj.getDictKey('four'), 'NUM')


    def test_getOriginalStr(self):
        self.assertEqual(testObj.getOrinalStr(), 'I am Jack and I am three years old')
        self.assertEqual(anotherObj.getOrinalStr(), "  This is Jill's and Jack's sentence, with leading and trailing spaces.   ")

    def test_getUntaggedStr(self):
        self.assertEqual(testObj.getUntaggedStr(), 'i and old am years')
        self.assertEqual(anotherObj.getUntaggedStr(), 'and trailing sentence this leading is s spaces with')

    def test_getTagStr(self):
        self.assertEqual(testObj.getTagStr(), 'jack three')
        self.assertEqual(anotherObj.getTagStr(), 'jill jack')

    def test_getSubStr(self):
        self.assertEqual(testObj.getSubStr(), 'I am NAME and I am NUM years old')
        self.assertEqual(anotherObj.getSubStr(), "This is NAME's and NAME's sentence, with leading and trailing spaces.")

    def test_addTagToDict(self):
        self.assertEqual(thirdObj.getOrinalStr(), "  This is Jill's and Jack's sentence, with leading and trailing spaces.   ")
        self.assertEqual(thirdObj.getUntaggedStr(), 'and trailing sentence this leading is s spaces with')
        self.assertEqual(thirdObj.getTagStr(), 'jill jack')
        self.assertEqual(thirdObj.getSubStr(), "This is NAME's and NAME's sentence, with leading and trailing spaces.")
        thirdObj.addTagToDict('CONN', 'and')
        self.assertEqual(thirdObj.getOrinalStr(), "  This is Jill's and Jack's sentence, with leading and trailing spaces.   ")
        self.assertEqual(thirdObj.getUntaggedStr(), 'trailing sentence this leading is s spaces with')
        self.assertEqual(thirdObj.getTagStr(), 'and jill jack')
        self.assertEqual(thirdObj.getSubStr(), "This is NAME's CONN NAME's sentence, with leading CONN trailing spaces.")

    def test_removeTagFromDict(self):
        self.assertEqual(thirdObj.getOrinalStr(), "  This is Jill's and Jack's sentence, with leading and trailing spaces.   ")
        self.assertEqual(thirdObj.getUntaggedStr(), 'trailing sentence this leading is s spaces with')
        self.assertEqual(thirdObj.getTagStr(), 'and jill jack')
        self.assertEqual(thirdObj.getSubStr(), "This is NAME's CONN NAME's sentence, with leading CONN trailing spaces.")
        thirdObj.removeTagFromDict('jack')
        self.assertEqual(thirdObj.getOrinalStr(), "  This is Jill's and Jack's sentence, with leading and trailing spaces.   ")
        self.assertEqual(thirdObj.getUntaggedStr(), 'trailing sentence this leading is s spaces jack with')
        self.assertEqual(thirdObj.getTagStr(), 'and jill')
        self.assertEqual(thirdObj.getSubStr(), "This is NAME's CONN Jack's sentence, with leading CONN trailing spaces.")

    def test_removeKeyFromDict(self):
        self.assertEqual(fourthObj.getOrinalStr(), "  This is Jill's and Jack's sentence, with leading and trailing spaces.   ")
        self.assertEqual(fourthObj.getUntaggedStr(), 'and trailing sentence this leading is s spaces with')
        self.assertEqual(fourthObj.getTagStr(), 'jill jack')
        self.assertEqual(fourthObj.getSubStr(), "This is NAME's and NAME's sentence, with leading and trailing spaces.")
        # thirdObj.removeTagFromDict('jack')

if __name__ == '__main__':
    unittest.main()
