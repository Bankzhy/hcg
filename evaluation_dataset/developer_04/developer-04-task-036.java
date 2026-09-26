@Override
    protected Unit myMultiplyBy(final Unit that) throws MultiplyException {
        Unit result;
        if (dimension.getRank() == 0) {
            result = that;
        }
        else {
            if (!(that instanceof DerivedUnit)) {
                result = that.multiplyBy(this);
            }
            else {
                final UnitDimension thatDimension = ((DerivedUnit) that)
                        .getDimension();
                result = thatDimension.getRank() == 0
                        ? this
                        : new DerivedUnitImpl(dimension
                                .multiplyBy(thatDimension));
            }
        }
        return result;
    }