class Polynomial:
    def _del_leading_zeros(self, my_list):
        my_list_res = my_list.copy()
        first_non_zero = 0
        for i in range(len(my_list_res)):
            if my_list_res[i] != 0:
                first_non_zero = i
                break

        del my_list_res[:first_non_zero]
        return my_list_res
        
    def __init__(self, arg):
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
            self.coeffs = list(coeffs).copy()
        self.coeffs = self._del_leading_zeros(self.coeffs)

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

    def __mul__(self, other):
        coeffs = self.coeffs.copy()
        if type(other) == int:
            res_coeffs = [other * x for x in coeffs]
        elif type(other) == type(self):
            other_coeffs = other.coeffs.copy()
            other_coeffs.reverse()
            coeffs.reverse()
            len_diff = abs(len(coeffs) - len(other_coeffs))
            zeros = [0 for _ in range(len_diff)]
            if len(coeffs) < len(other_coeffs):
                coeffs.extend(zeros)
            elif len(coeffs) > len(other_coeffs):
                other_coeffs.extend(zeros)

            res = {}
            for i in range(len(coeffs)):
                for j in range(len(other_coeffs)):
                    power = i + j
                    if power in res:
                        res[power] += coeffs[i] * other_coeffs[j]
                    else:
                        res[power] = coeffs[i] * other_coeffs[j]
            res_coeffs = sorted(res.items(), key=lambda x: x[0], reverse=True)
            res_coeffs = [x[1] for x in res_coeffs]
        else:
            raise TypeError
        return self.__class__(res_coeffs)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other):
        if type(other) == int:
            tmp_coeffs = [other]
        elif type(other) == type(self):
            tmp_coeffs = other.coeffs
        else:
            raise TypeError
        return self.coeffs == tmp_coeffs

    def __getattr__(self, name):
        if name == "coeffs":
            return self.__dict__[name]
        else:
            raise AttributeError

    def __setattr__(self, name, value):
        if name == "coeffs":
            if type(value) != list:
                raise TypeError
            if len(value) == 0:
                raise ValueError
            tmp_value = self._del_leading_zeros(value)
            self.__dict__[name] = tmp_value
        else:
            raise AttributeError
