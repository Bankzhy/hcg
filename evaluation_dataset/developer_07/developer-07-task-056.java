@Override
    public JSONObject toJsonObject() throws JSONException {
        JSONObject returnVal = super.toJsonObject();
        if(this.getUser() != null)
        {
            returnVal.put(JSONMapping.USER,
                    this.getUser().toJsonObject());
        }
        if(this.getDateCreated() != null)
        {
            returnVal.put(JSONMapping.DATE_CREATED,
                    this.getDateAsLongFromJson(this.getDateCreated()));
        }
        if(this.getDateRead() != null)
        {
            returnVal.put(JSONMapping.DATE_READ,
                    this.getDateAsLongFromJson(this.getDateRead()));
        }
        if(this.getExpiringLink() != null)
        {
            returnVal.put(JSONMapping.EXPIRING_LINK, this.getExpiringLink());
        }
        if(this.getMessage() != null)
        {
            returnVal.put(JSONMapping.MESSAGE, this.getMessage());
        }
        returnVal.put(JSONMapping.USER_NOTIFICATION_TYPE, this.getUserNotificationType());
        return returnVal;
    }