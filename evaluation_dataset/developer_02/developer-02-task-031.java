private Connection randomGet(List<Connection> conns) {
        if (null == conns || conns.isEmpty()) {
            return null;
        }
        int size = conns.size();
        int tries = 0;
        Connection result = null;
        while ((result == null || !result.isFine()) && tries++ < MAX_TIMES) {
            result = conns.get(this.random.nextInt(size));
        }
        if (result != null && !result.isFine()) {
            result = null;
        }
        return result;
    }