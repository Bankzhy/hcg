@Override
    public JSONObject toJsonObject() throws JSONException
    {
        JSONObject returnVal = super.toJsonObject();
        if(this.getAttachmentPath() != null)
        {
            returnVal.put(JSONMapping.ATTACHMENT_PATH,
                    this.getAttachmentPath());
        }
        if(this.getAttachmentDataBase64() != null)
        {
            returnVal.put(JSONMapping.ATTACHMENT_DATA_BASE64,
                    this.getAttachmentDataBase64());
        }
        return returnVal;
    }