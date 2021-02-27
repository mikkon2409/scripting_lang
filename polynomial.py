class Polynomial:
    def __init__(self, *args):
        if len(args) != 1:
            raise TypeError
        arg = args[0]
        if type(arg) == type(self):
            self.coeffs = arg.coeffs.copy()
            return
        coeffs = arg
        if type(coeffs) != int and type(coeffs) != tuple and type(coeffs) != list:
            raise TypeError
        if type(coeffs) == tuple or type(coeffs) == list:
            if len(coeffs) == 0:
                raise ValueError
        if type(coeffs) == int:
            self.coeffs = [coeffs]
        else:
            self.coeffs = coeffs.copy()

    def __repr__(self):
        return f'{self.__class__.__name__}({self.coeffs})'

    def __str__(self):
        representation = ''
        for i in range(len(self.coeffs)):
            power = len(self.coeffs) - i - 1
            coeff = self.coeffs[i]
            if coeff == 0:
                continue
            if i != 0 or coeff < 0:
                representation += '+' if coeff > 0 else '-'
            representation += str(abs(coeff)) if power == 0 or abs(coeff) != 1 else ''
            if power > 0:
                representation += 'x'
            if power > 1:
                representation += f'^{power}'
        return representation

    def __add__(self, other):
        coeffs = self.coeffs.copy()
        if type(other) == int:
            coeffs[len(coeffs) - 1] += other
        elif type(other) == type(self):
            other_coeffs = other.coeffs.copy()
            other_coeffs.reverse()
            coeffs.reverse()
            if len(coeffs) < len(other_coeffs):
                for _ in range(len(other_coeffs) - len(coeffs)):
                    coeffs.append(0)
            for i in range(len(other_coeffs)):
                coeffs[i] += other_coeffs[i]
            coeffs.reverse()
        else:
            raise TypeError
        return self.__class__(coeffs)

    def __neg__(self):
        return self.__class__([-x for x in self.coeffs])

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.__add__(-other)

    def __rsub__(self, other):
        return self.__neg__().__add__(other)
