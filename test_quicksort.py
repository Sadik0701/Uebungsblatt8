import unittest
import quicksort2

class TestQuickSort(unittest.TestCase):
    def test_normal_array(self):
        input_array = [1,3, 2,1]
        quicksort2.quicksort(input_array,0,len(input_array)-1)
        self.assertEqual([1,1,2,3],input_array) # add assertion here

    def test_empty_array(self):
        input_array = []
        quicksort2.quicksort(input_array,0,0)
        self.assertEqual([],input_array)


    def test_negative_array(self):
        input_array = [-1, -5, -2, -3, -5]
        quicksort2.quicksort(input_array,0,len(input_array)-1)
        self.assertEqual([-5, -5, -3, -2, -1], input_array)



if __name__ == '__main__':
    unittest.main()
