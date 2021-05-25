from typing import Union
import unittest
from polynomial import Polynomial


class TestCreatePolynomial(unittest.TestCase):
    def test_empty(self):
        self.assertRaises(TypeError, Polynomial)

    def test_with_empty_list(self):
        self.assertRaises(ValueError, Polynomial, [])

    def test_constant(self):
        value = 5
        p = Polynomial(value)
        self.assertEqual(p.coeffs, [value])

    def test_list(self):
        value = [5]
        p = Polynomial(value)
        self.assertEqual(p.coeffs, value)

    def test_copy(self):
        value = [5]
        p = Polynomial(value)
        k = Polynomial(p)
        self.assertEqual(p.coeffs, k.coeffs)

    def test_get_set_coeffs(self):
        p = Polynomial(2)
        p.coeffs = [0, 2, 1, 0]
        self.assertEqual(p.coeffs, [2, 1, 0])



class TestAddPolynomial(unittest.TestCase):
    def test_add(self):
        p1 = Polynomial([2, 3, 4])
        p2 = Polynomial([3, 4, 5])
        self.assertEqual(p1+p2, Polynomial([5, 7, 9]))

    def test_add_diff_len(self):
        p1 = Polynomial([2])
        p2 = Polynomial([3, 4, 5])
        self.assertEqual(p1+p2, Polynomial([3, 4, 7]))

    def test_add_with_const(self):
        p1 = Polynomial([3, 4, 5])
        self.assertEqual(p1+2, Polynomial([3, 4, 7]))

    def test_add_with_const_reverse_order(self):
        p1 = Polynomial([3, 4, 5])
        self.assertEqual(2+p1, Polynomial([3, 4, 7]))


class TestSubPolynomial(unittest.TestCase):
    def test_sub(self):
        p1 = Polynomial([2, 3, 4])
        p2 = Polynomial([3, 4, 5])
        self.assertEqual(p1-p2, Polynomial([-1, -1, -1]))

    def test_sub_diff_len(self):
        p1 = Polynomial([2])
        p2 = Polynomial([3, 4, 5])
        self.assertEqual(p1-p2, Polynomial([-3, -4, -3]))

    def test_sub_with_const(self):
        p1 = Polynomial([3, 4, 5])
        self.assertEqual(p1-2, Polynomial([3, 4, 3]))

    def test_sub_with_const_reverse_order(self):
        p1 = Polynomial([3, 4, 5])
        self.assertEqual(2-p1, Polynomial([-3, -4, -3]))


class TestMulPolynomial(unittest.TestCase):
    def test_mul(self):
        p1 = Polynomial([2, 3, 4])
        p2 = Polynomial([3, 4, 5])
        self.assertEqual(p1*p2, Polynomial([6, 17, 34, 31, 20]))

    def test_mul_diff_len(self):
        p1 = Polynomial([2])
        p2 = Polynomial([3, 4, 5])
        self.assertEqual(p1*p2, Polynomial([6, 8, 10]))

    def test_mul_with_const(self):
        p1 = Polynomial([3, 4, 5])
        self.assertEqual(p1*2, Polynomial([6, 8, 10]))

    def test_mul_with_const_reverse_order(self):
        p1 = Polynomial([3, 4, 5])
        self.assertEqual(2*p1, Polynomial([6, 8, 10]))


class TestComparisonPolynomial(unittest.TestCase):
    def test_eq(self):
        p1 = Polynomial([2, 3, 4])
        p2 = Polynomial([2, 3, 4])
        self.assertEqual(p1, p2)

    def test_neq_diff_len(self):
        p1 = Polynomial([2])
        p2 = Polynomial([3, 4, 5])
        self.assertNotEqual(p1, p2)

    def test_eq_with_const(self):
        p1 = Polynomial([2])
        self.assertEqual(p1, 2)

    def test_eq_with_const_reverse_order(self):
        p1 = Polynomial([2])
        self.assertEqual(2, p1)


class TestStrPolynomial(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(Polynomial([2, 1, 0])), "2x^2+x")

    def test_str_with_leading_zeros(self):
        self.assertEqual(str(Polynomial([0, 0, 2, 1, 0])), "2x^2+x")


class TestReprPolynomial(unittest.TestCase):
    def test_repr(self):
        self.assertEqual(repr(Polynomial([2, 1, 0])), "Polynomial([2, 1, 0])")

    def test_str_with_leading_zeros(self):
        self.assertEqual(repr(Polynomial([0, 0, 2, 1, 0])), "Polynomial([2, 1, 0])")


if __name__ == '__main__':
    unittest.main()
