@Override
    public MessageMetadata readMessageBegin() throws IOException {
        int size = readI32();
        if (size < 0) {
            int version = size & VERSION_MASK;
            if (version != VERSION_1) {
                throw new ProtocolException("Bad version in readMessageBegin");
            }
            return new MessageMetadata(readString(), (byte) (size & 0xff), readI32());
        } else {
            if (strictRead) {
                throw new ProtocolException("Missing version in readMessageBegin");
            }
            return new MessageMetadata(readStringWithSize(size), readByte(), readI32());
        }
    }