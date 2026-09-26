public static List<PropertyInjector> doGetPropertyInjectors(Ioc ioc, KlassInfo klass, Configuration properties) {
        if (properties == null || properties.size() == 0) {
            return Collections.emptyList();
        }
        List<PropertyInjector> injectors = new ArrayList<PropertyInjector>();
        for (String name : properties.keySet()) {
            PropertyInfo prop = klass.getProperty(name);
            if (prop == null) {
                throw new IllegalStateException("Property not found: " + klass + "#" + name);
            }
            if (!prop.writable()) {
                throw new IllegalStateException("Property not writable: " + prop);
            }
            Object value;
            Class<?> rawType = prop.getRawType(klass.getType());
            if (List.class.isAssignableFrom(rawType)) {
                value = properties.getValueList(prop.getName(), prop.getRawComponentType(klass.getType(), 0));
            } else {
                value = properties.getValue(prop.getName(), rawType, null);
            }
            injectors.add(new PropertyInjector(prop, value));
        }
        return injectors;
    }