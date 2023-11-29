#!/usr/bin/python3
"""Unittests for max_integer. """


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer"""
    def test_no_args(self):
        """Unittest for max_integer no args"""
        self.assertEqual(max_integer(), None)

    def test_empty_ls(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer([]), None)

    def test_one_elem(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer([90]), 90)

   def test_max_start(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer([10, 5, 3, 1]), 10)i

   def test_same_vals(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

   def test_asce(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

   def test_mixed_signs(self):
        """Unittest for max_integer"""
        self.assertEqual(
            max_integer([-25, 68, 51, 64, -124, 89, 88, 120, -26, -416]),
            120)

   def test_large_negatives(self):
        """Unittest for max_integer"""
        self.assertEqual(
            max_integer(
                [-6145619, -854859, -462553, -6088955,
                    -1907189, -8110534, -6601769, -5837524, 
                    -8433749, -7251403, -5117635, -1335257,
                    -6867266, -9073637, -6224732 ,-1080228,
                    -6801278, -8351954, -1736432, -4376995,
                    -967891, -4663691, -71562, -8038202,
                    -7893047, -9350883, -1132134, -8495354,
                    -9158229, -9310087, -6319598, -4906000,
                    -386471, -639929, -2676965,  -6258057,
                    -5490677, -1107298, -4199148,  -9917695,
                    -7759849, -7045734, -4885806,  -5119579,
                    -4147063, -7622811, -4671971,  -840414,
                    -3671742, -4400074, -3549343,  -6071672,
                    -7213213, -1307446, -3936098,  -9162654,
                    -6129976, -5791439, -3481890,  -6954726,
                    -5272933, -4952516, -6115545,  -7271456,
                    -4097027, -4342575, -8400559,  -4373818,
                    -8054214, -8565596, -639225,  -4269529,
                    -7202853, -6891036, -4379807,  -1536591,
                    -2839083, -2586661, -9941097, -3136620]), -71562)

    def test_ints_floats(self):
        """Unittest for max_integer"""
        self.assertEqual(
            max_integer(
                [120, 98.8, -150, 0.1, -1000, 9998, -10000, 9798.9]), 9998)

    def test_nume_string(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer("1924"), "9")

    def test_string(self):
        """Unittest for max_integer"""
        self.assertEqual(max_integer("ALX"), "L")


    def test_mixed_list(self):
        """Unittest for max_integer"""
        with self.assertRaises(TypeError):
            max_integer([[], [2], [3], [5, 8], 99, "hey"])

    def test_None(self):
        """Unittest for max_integer"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_mixed_ls_str_int(self):
        """Unittest for max_integer"""
        with self.assertRaises(TypeError):
            max_integer([75, "hey"])

    def test_dictonry(self):
        """Unittest for max_integer"""
        with self.assertRaises(TypeError):
            max_integer([{51: 53, 15: 48}, {"a": "b"}])

    if __name__ == '__main__':
          unittest.main()
