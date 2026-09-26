def _cubic_bernstein_extrema(p0, p1, p2, p3):
        a = 3.*(p3-p0+3.*(p1-p2))
        b = 6.*(p0+p2-2.*p1)
        c = 3.*(p1-p0)
        if a == 0:
            if b == 0:
                return ()
            return (-c / b,)
        d = b*b - 4.*a*c
        if d < 0:
            return ()
        k = -2. * a
        if d == 0:
            return (b / k,)
        r = math.sqrt(d)
        return ((b + r) / k, (b - r) / k)