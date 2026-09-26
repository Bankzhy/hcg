public INDArray getArr() {
        if(sameDiff.arrayAlreadyExistsForVarName(getVarName()))
            return sameDiff.getArrForVarName(getVarName());
        if(getScalarValue() != null && ArrayUtil.prod(getShape()) == 1) {
            INDArray arr = Nd4j.valueArrayOf(getShape(),
                    getScalarValue().doubleValue());
            sameDiff.associateArrayWithVariable(arr,this);
        }
        else if(sameDiff.getShapeForVarName(getVarName()) == null)
            return null;
        else {
            INDArray newAlloc = getWeightInitScheme().create(sameDiff.getShapeForVarName(getVarName()));
            sameDiff.associateArrayWithVariable(newAlloc,this);
        }
        return sameDiff.getArrForVarName(getVarName());
    }