import unittest
from myTagProcessor import Taggerizer

class TestTagProcessor(unittest.TestCase):
    global testObj, anotherObj
    testObj = Taggerizer("I am Jack and I am three years old")
    anotherObj = Taggerizer("  This is Jill's and Jack's sentence with leading and trailing spaces.   ")

    def test_getOriginalStr(self):
        self.assertEqual(testObj.getOrinalStr(), 'I am Jack and I am three years old')
        self.assertEqual(anotherObj.getOrinalStr(), "  This is Jill's and Jack's sentence with leading and trailing spaces.   ")

    def test_getUntaggedStr(self):
        self.assertEqual(testObj.getUntaggedStr(), 'i and old am years')

    def test_getTagStr(self):
        self.assertEqual(testObj.getTagStr(), 'jack three')

    def test_getSubStr(self):
        self.assertEqual(testObj.getSubStr(), 'i am NAME and i am NUM years old')

if __name__ == '__main__':
    unittest.main()
