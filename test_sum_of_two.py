import unittest
from sum_of_two import two_sum


class TestTwoSum(unittest.TestCase):

    def test_example_1(self):
        """[2,7,11,15], target=9 → [0,1]"""
        result = two_sum([2, 7, 11, 15], 9)
        self.assertEqual(result, [0, 1])

    def test_example_2(self):
        """[3,2,4], target=6 → [1,2]"""
        result = two_sum([3, 2, 4], 6)
        self.assertEqual(result, [1, 2])

    def test_example_3(self):
        """[3,3], target=6 → [0,1]"""
        result = two_sum([3, 3], 6)
        self.assertEqual(result, [0, 1])

    def test_no_solution(self):
        """Нет решения → None"""
        result = two_sum([1, 2, 3], 10)
        self.assertIsNone(result)

    def test_empty_array(self):
        """Пустой массив → None"""
        result = two_sum([], 5)
        self.assertIsNone(result)

    def test_one_element(self):
        """Один элемент → None"""
        result = two_sum([5], 5)
        self.assertIsNone(result)

    def test_negative_numbers(self):
        """Отрицательные числа"""
        result = two_sum([-1, -2, -3, -4, -5], -8)
        self.assertEqual(result, [2, 4])  # -3 + (-5) = -8

    def test_with_zero(self):
        """С нулём"""
        result = two_sum([0, 4, 3, 0], 0)
        self.assertEqual(result, [0, 3])  # 0 + 0 = 0


if __name__ == "__main__":
    unittest.main()