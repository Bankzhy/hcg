@Override
    public Observable<Observable<Row>> findAllDataFromBucket(long timestamp, int pageSize, int maxConcurrency) {
        PreparedStatement ts =
                getTempStatement(MetricType.UNDEFINED, TempStatement.SCAN_WITH_TOKEN_RANGES, timestamp);
        if(ts == null || prepMap.floorKey(timestamp) == 0L) {
            return Observable.empty();
        }
        return Observable.from(getTokenRanges())
                .map(tr -> rxSession.executeAndFetch(
                        ts
                                .bind()
                                .setToken(0, tr.getStart())
                                .setToken(1, tr.getEnd())
                                .setFetchSize(pageSize)));
    }