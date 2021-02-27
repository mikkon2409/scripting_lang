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


class TestPrintPolynomial(unittest.TestCase):
    def setUp(self):
        self.p = Polynomial


if __name__ == '__main__':
    unittest.main()
