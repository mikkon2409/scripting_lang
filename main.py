from polynomial import Polynomial


def main():
    l = [-5, 0, 0]
    p = Polynomial(l)
    print(p.coeffs)
    print(repr(p))
    print(p)


if __name__ == "__main__":
    main()
