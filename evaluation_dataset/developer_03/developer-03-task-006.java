protected boolean
    contractR(DapStructure dstruct, Set<DapStructure> contracted)
    {
        if(contracted.contains(dstruct))
            return true;
        int processed = 0;
        List<DapVariable> fields = dstruct.getFields();
        for(DapVariable field : fields) {
            if(findVariableIndex(field) < 0)
                break;
            DapType base = field.getBaseType();
            if(base.getTypeSort().isCompound()
                    && !contracted.contains((field))) {
                if(!contractR((DapStructure)base, contracted))
                    break;
            }
            processed++;
        }
        if(processed < fields.size())
            return false;
        contracted.add(dstruct);
        return true;
    }