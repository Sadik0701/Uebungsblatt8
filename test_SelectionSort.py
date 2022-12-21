import unittest
import SelectionSort


class TestSelectionSort(unittest.TestCase):
    def test_a_normal_array(self):
        input_array = [3, 2, 1]
        SelectionSort.selectionsort(input_array)
        self.assertEqual([1, 2, 3], input_array)  # add assertion here

    def test_an_empty_array(self):
        input_array = []
        SelectionSort.selectionsort(input_array)
        self.assertEqual([], input_array)

    def test_array_with_1_element(self):
        input_array = [99]
        SelectionSort.selectionsort(input_array)
        self.assertEqual([99], input_array)


if __name__ == '__main__':
    unittest.main()
