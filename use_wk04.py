import wk04


def sequential(f, x_start, x_end, delta_x, epsilon=1e-6,):
    xp = x_start

    while True:
        d = wk04.wk04(f, xp, delta_x, epsilon)

        if d['found']:
            break
        elif d['x'] > x_end:
            d['x'] = 'not found'
            break
        else:
            xp = d['x']

    return d['x']


def poly(x):
    return x * x - 20


def main():
    d = sequential(poly, 4, 5, 1e-6)
    print(f"poly({d['x']}) = {poly(d['x'])} is close to zero.")


if "__main__" == __name__:
    main()
