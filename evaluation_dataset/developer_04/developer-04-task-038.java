@Override
    public int fieldIndex(String name)
            throws DapException
    {
        DapStructure ds;
        if(getTemplate().getSort().isCompound())
            ds = (DapStructure) getTemplate();
        else if(getTemplate().getSort().isVar()
                && (((DapVariable) getTemplate()).getBaseType().getSort().isCompound()))
            ds = (DapStructure) ((DapVariable) getTemplate()).getBaseType();
        else
            throw new DapException("Attempt to get field name on non-compound object");
        int i = ds.indexByName(name);
        if(i < 0)
            throw new DapException("Unknown field name: " + name);
        return i;
    }