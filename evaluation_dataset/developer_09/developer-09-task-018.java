@Override
    public void gemm(char Order, char TransA, char TransB, IComplexNumber alpha, IComplexNDArray A, IComplexNDArray B,
                    IComplexNumber beta, IComplexNDArray C) {
        if (Nd4j.getExecutioner().getProfilingMode() == OpExecutioner.ProfilingMode.ALL)
            OpProfiler.getInstance().processBlasCall(true, A, B, C);
        GemmParams params = new GemmParams(A, B, C);
        if (A.data().dataType() == DataBuffer.Type.DOUBLE) {
            zgemm(Order, TransA, TransB, params.getM(), params.getN(), params.getK(), alpha.asDouble(),
                            A.ordering() == NDArrayFactory.C ? B : A, params.getLda(),
                            B.ordering() == NDArrayFactory.C ? A : B, params.getLdb(), beta.asDouble(), C,
                            params.getLdc());
        } else
            cgemm(Order, TransA, TransB, params.getM(), params.getN(), params.getK(), alpha.asFloat(),
                            A.ordering() == NDArrayFactory.C ? B : A, params.getLda(),
                            B.ordering() == NDArrayFactory.C ? A : B, params.getLdb(), beta.asFloat(), C,
                            params.getLdc());
    }