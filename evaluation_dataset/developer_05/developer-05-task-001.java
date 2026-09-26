@Override
    public JSONObject toJsonObject() throws JSONException
    {
        JSONObject returnVal = super.toJsonObject();
        if(this.getSumDecimals() != null)
        {
            returnVal.put(JSONMapping.SUM_DECIMALS, this.getSumDecimals());
        }
        if(this.getTableRecords() != null && !this.getTableRecords().isEmpty())
        {
            JSONArray assoFormsArr = new JSONArray();
            for(Form toAdd :this.getTableRecords())
            {
                assoFormsArr.put(toAdd.toJsonObject());
            }
            returnVal.put(JSONMapping.TABLE_RECORDS, assoFormsArr);
        }
        return returnVal;
    }