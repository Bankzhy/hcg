public void updateShapeForVarName(String varName, long[] shape) {
        if (shape == null) {
            throw new ND4JIllegalStateException("Null shapes not allowed!");
        }
        if (variableNameToArr.containsKey(varName) && !Arrays.equals(variableNameToArr.get(varName).shape(), shape)) {
            throw new ND4JIllegalStateException("Already found an existing array!");
        }
        for (int i = 0; i < shape.length; i++) {
            if (shape[i] < 1) {
                addAsPlaceHolder(varName);
                placeHolderOriginalShapes.put(varName, shape);
                return;
            }
        }
        variableNameToShape.put(varName, shape);
    }