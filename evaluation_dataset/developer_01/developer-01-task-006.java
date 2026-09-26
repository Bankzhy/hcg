private boolean readClassFile(final ClassFileDataInput di) throws IOException {
        if (!readMagicCode(di)) {
            return false;
        }
        if (!readVersion(di)) {
            return false;
        }
        readConstantPoolEntries(di);
        if (!readAccessFlags(di)) {
            return false;
        }
        readThisClass(di);
        readSuperClass(di);
        readInterfaces(di);
        readFields(di);
        readMethods(di);
        return readAttributes(di, ElementType.TYPE);
    }