from fracs import *
import unittest
class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self): 
        self.assertEqual(sub_frac([1, 5], [2, 3]), [-7, 15])

    def test_mul_frac(self): 
        self.assertEqual(mul_frac([4, 7], [1, 2]), [4, 14])

    def test_div_frac(self):
        self.assertEqual(div_frac([7, 8], [3, 7]), [49, 24])

    def test_is_positive(self):
        self.assertEqual(is_positive([7, 8]),1) 

    def test_is_zero(self): 
        self.assertEqual(is_zero([0, 8]),1) 

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 3],[2,3]),-1)
	self.assertEqual(cmp_frac([5, 6],[1,3]),1)
	self.assertEqual(cmp_frac([2, 4],[1,2]),0)    

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 8]),float(1/8)) 

    def tearDown(self):pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy
