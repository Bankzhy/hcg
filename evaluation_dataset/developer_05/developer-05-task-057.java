@Override
    public JSONObject toJsonObject() throws JSONException {
        JSONObject returnVal = super.toJsonObject();
        if(this.getDatasourceName() != null) {
            returnVal.put(JSONMapping.DATASOURCE_NAME,
                    this.getDatasourceName());
        }
        if(this.getQuery() != null) {
            returnVal.put(JSONMapping.QUERY, this.getQuery());
        }
        if(this.getStoredProcedure() != null) {
            returnVal.put(
                    JSONMapping.STORED_PROCEDURE,
                    this.getStoredProcedure());
        }
        if(this.getSqlInputs() != null)
        {
            JSONArray jsonArray = new JSONArray();
            for(SQLColumn toAdd : this.getSqlInputs())
            {
                jsonArray.put(toAdd.toJsonObject());
            }
            returnVal.put(JSONMapping.SQL_INPUTS, jsonArray);
        }
        return returnVal;
    }