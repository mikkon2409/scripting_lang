class Polynomial:
    def __init__(self, coeffs):
        if type(coeffs) != int and type(coeffs) != tuple and type(coeffs) != list:
            raise TypeError
        if type(coeffs) == tuple or type(coeffs) == list:
            if len(coeffs) == 0:
                raise ValueError
        self.coeffs = coeffs
