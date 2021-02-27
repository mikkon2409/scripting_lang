from polynomial import Polynomial


def main():
    p1 = Polynomial([-5, 0, 0])
    p2 = Polynomial([6, 7, 5, 1, 1])
    # print(p1 + p2)
    # print(1 + p2)
    # print(p1 + 1)
    # print(1 + p1)
    print(1 - p1)
    print(p1 - 1)
    print(p1 - p2)


if __name__ == "__main__":
    main()
