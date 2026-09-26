@Override
    public double distance1(INDArray other) {
        float d = 0.0f;
        if (other instanceof IComplexNDArray) {
            IComplexNDArray n2 = (IComplexNDArray) other;
            IComplexNDArray n2Linear = n2.linearView();
            for (int i = 0; i < length(); i++) {
                IComplexNumber n = getComplex(i).sub(n2Linear.getComplex(i));
                d += n.absoluteValue().doubleValue();
            }
            return d;
        }
        INDArray linear = other.linearView();
        for (int i = 0; i < length(); i++) {
            IComplexNumber n = linearView().getComplex(i).sub(linear.getDouble(i));
            d += n.absoluteValue().doubleValue();
        }
        return d;
    }