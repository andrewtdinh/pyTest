import unittest
from myTagProcessor import Taggerizer

class TestTagProcessor(unittest.TestCase):
    global testObj, anotherObj
    testObj = Taggerizer("I am Jack and I am three years old")
    anotherObj = Taggerizer("  This is Jill's and Jack's sentence with leading and trailing spaces.   ")

    def test_getDictKey(self):
        self.assertEqual(testObj.getDictKey('jack'), 'NAME')
        self.assertEqual(testObj.getDictKey('jill'), 'NAME')
        self.assertEqual(testObj.getDictKey('three'), 'NUM')
        self.assertEqual(anotherObj.getDictKey('jill'), 'NAME')
        self.assertEqual(anotherObj.getDictKey('jack'), 'NAME')
        self.assertEqual(anotherObj.getDictKey('four'), 'NUM')


    def test_getOriginalStr(self):
        self.assertEqual(testObj.getOrinalStr(), 'I am Jack and I am three years old')
        self.assertEqual(anotherObj.getOrinalStr(), "  This is Jill's and Jack's sentence with leading and trailing spaces.   ")

    def test_getUntaggedStr(self):
        self.assertEqual(testObj.getUntaggedStr(), 'i and old am years')

    def test_getTagStr(self):
        self.assertEqual(testObj.getTagStr(), 'jack three')

    def test_getSubStr(self):
        self.assertEqual(testObj.getSubStr(), 'I am NAME and I am NUM years old')


if __name__ == '__main__':
    unittest.main()
