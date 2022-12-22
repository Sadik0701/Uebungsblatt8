import unittest
import quicksort

class TestQuickSort(unittest.TestCase):
    def test_normal_array(self):
        input_array = [-1,3, 2,1]
        quicksort.quicksort(input_array,0,len(input_array))
        self.assertEqual([-1,1,2,3],input_array) # add assertion here

    def test_empty_array(self):
        input_array = []
        quicksort.quicksort(input_array,0,0)
        self.assertEqual([],input_array)




if __name__ == '__main__':
    unittest.main()
