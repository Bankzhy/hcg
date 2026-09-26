public static Pair<INDArray, INDArray> merge2d(INDArray[] arrays, INDArray[] masks) {
        long cols = arrays[0].columns();
        INDArray[] temp = new INDArray[arrays.length];
        boolean hasMasks = false;
        for (int i = 0; i < arrays.length; i++) {
            if (arrays[i].columns() != cols) {
                throw new IllegalStateException("Cannot merge 2d arrays with different numbers of columns (firstNCols="
                                + cols + ", ithNCols=" + arrays[i].columns() + ")");
            }
            temp[i] = arrays[i];
            if (masks != null && masks[i] != null && masks[i] != null) {
                hasMasks = true;
            }
        }
        INDArray out = Nd4j.specialConcat(0, temp);
        INDArray outMask = null;
        if (hasMasks) {
            outMask = DataSetUtil.mergePerOutputMasks2d(out.shape(), arrays, masks);
        }
        return new Pair<>(out, outMask);
    }