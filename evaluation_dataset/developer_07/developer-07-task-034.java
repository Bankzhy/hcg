@Override
    public JSONObject toJsonObject() throws JSONException
    {
        JSONObject returnVal = super.toJsonObject();
        if(this.getFormContainer() != null)
        {
            returnVal.put(JSONMapping.FORM_CONTAINER,
                    this.getFormContainer().toJsonObject());
        }
        if(this.getParentFormContainer() != null)
        {
            returnVal.put(JSONMapping.PARENT_FORM_CONTAINER,
                    this.getParentFormContainer().toJsonObject());
        }
        if(this.getParentFormField() != null)
        {
            returnVal.put(JSONMapping.PARENT_FORM_FIELD,
                    this.getParentFormField().toJsonObject());
        }
        return returnVal;
    }