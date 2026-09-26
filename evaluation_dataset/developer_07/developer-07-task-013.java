@Override
    public Object get(Object key) {
        Object value = backingMap.get(key);
        if (type instanceof Class) {
            if (!((Class) type).isInstance(value)) {
                value = convert(type, value);
                backingMap.put(key, value);
            }
        } else {
            if (!(value instanceof ConvertingMap) && !(value instanceof ConvertingList)) {
                value = convert(type, value);
                if (value instanceof ConvertingMap || value instanceof ConvertingList) {
                    backingMap.put(key, value);
                }
            }
        }
        return value;
    }