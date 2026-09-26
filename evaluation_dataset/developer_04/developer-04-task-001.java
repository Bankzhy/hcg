static public BigDecimal pochhammer(final BigDecimal x, final int n) {
        if (n < 0) {
            throw new ProviderException("Unimplemented pochhammer with negative index " + n);
        } else if (n == 0) {
            return BigDecimal.ONE;
        } else {
            BigDecimal xhighpr = scalePrec(x, 2);
            BigDecimal resul = xhighpr;
            double xUlpDbl = x.ulp().doubleValue();
            double xDbl = x.doubleValue();
            double eps = 0.5 * xUlpDbl / Math.abs(xDbl);
            for (int i = 1; i < n; i++) {
                eps += 0.5 * xUlpDbl / Math.abs(xDbl + i);
                resul = resul.multiply(xhighpr.add(new BigDecimal(i)));
                final MathContext mcloc = new MathContext(4 + err2prec(eps));
                resul = resul.round(mcloc);
            }
            return resul.round(new MathContext(err2prec(eps)));
        }
    }