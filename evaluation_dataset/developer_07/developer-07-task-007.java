public void serialize(String dataset, DataOutputStream sink, CEEvaluator ce, Object specialO)
            throws NoSuchVariableException, DAP2ServerSideException, IOException {
        PrimitiveVector vals = getPrimitiveVector();
        if (!isRead())
            read(dataset, specialO);
        if (vals.getTemplate() instanceof DSequence || ce.evalClauses(specialO)) {
            int length = vals.getLength();
            sink.writeInt(length);
            if (vals instanceof BaseTypePrimitiveVector) {
                for (int i = 0; i < length; i++) {
                    ServerMethods sm = (ServerMethods)
                            ((BaseTypePrimitiveVector) vals).getValue(i);
                    sm.serialize(dataset, sink, ce, specialO);
                }
            } else {
                sink.writeInt(length);
                vals.externalize(sink);
            }
        }
    }