def fab(max = 5):
    n, a, b = 0, 0, 1
    while n <= max:
        yield n, b
        a, b = b, a+b
        n = n + 1


if __name__ == '__main__':
    fab = fab(6)
    print(fab.__next__())
    print(fab.__next__())
    print(fab.__next__())
    print(fab.__next__())
    print(fab.__next__())
    print(fab.__next__())
    print(fab.__next__())
