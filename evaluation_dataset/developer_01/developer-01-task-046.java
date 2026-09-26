static StructureMembers
    computemembers(DapVariable var)
    {
        DapStructure ds = (DapStructure)var.getBaseType();
        StructureMembers sm
                = new StructureMembers(ds.getShortName());
        List<DapVariable> fields = ds.getFields();
        for(int i = 0; i < fields.size(); i++) {
            DapVariable field = fields.get(i);
            DapType dt = field.getBaseType();
            DataType cdmtype = CDMTypeFcns.daptype2cdmtype(dt);
            StructureMembers.Member m =
                    sm.addMember(
                            field.getShortName(), "", null,
                            cdmtype,
                            CDMUtil.computeEffectiveShape(field.getDimensions()));
            m.setDataParam(i);
            if(dt.getTypeSort().isStructType()) {
                StructureMembers subsm = computemembers(field);
                m.setStructureMembers(subsm);
            }
        }
        return sm;
    }