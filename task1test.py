import task1 as t1
import unittest

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        t1.rates = [1,2,3,4]

    def test1(self):
        assert (t1.rates[0] ==1) #test1 fails first rate not 1
        
if __name__ == '__main__':
    unittest.main()
