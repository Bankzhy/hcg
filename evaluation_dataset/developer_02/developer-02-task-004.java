protected void
    writeStructure1(DataCursor instance, SerialWriter dst)
            throws IOException
    {
        assert instance.getScheme() == DataCursor.Scheme.STRUCTURE;
        DapVariable template = (DapVariable) instance.getTemplate();
        assert (this.ce.references(template));
        DapStructure ds = (DapStructure) template.getBaseType();
        List<DapVariable> fields = ds.getFields();
        for(int i = 0; i < fields.size(); i++) {
            DapVariable field = fields.get(i);
            if(!this.ce.references(field)) continue;
            DataCursor df = (DataCursor) instance.readField(i);
            writeVariable(df, dst);
        }
    }