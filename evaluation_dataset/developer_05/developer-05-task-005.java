public void error(
            @Nullable final String event,
            @Nullable final String message,
            @Nullable final Map<String, Object> data,
            @Nullable final Throwable throwable) {
        if (getSlf4jLogger().isErrorEnabled()) {
            LogLevel.ERROR.log(
                    getSlf4jLogger(),
                    event,
                    createKeysFromCollection(
                            data == null ? Collections.emptyList() : data.keySet(),
                            MESSAGE_DATA_KEY),
                    createValuesFromCollection(
                            data == null ? Collections.emptyList() : data.values(),
                            message),
                    throwable);
        }
    }