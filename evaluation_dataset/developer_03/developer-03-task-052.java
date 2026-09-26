public static <T> String arrayString(T[] items) {
        StringBuilder sB = new StringBuilder("A[");
        boolean isFirst = true;
        for (T item : items) {
            if (isFirst) {
                isFirst = false;
            } else {
                sB.append(" ");
            }
            if (item instanceof String) {
                sB.append("\"").append(item).append("\"");
            } else {
                sB.append(item);
            }
        }
        return sB.append("]").toString();
    }