public static Object getProp( Object object, final String property ) {
        if ( object == null ) {
            return null;
        }
        if ( isDigits( property ) ) {
            object = idx(object, StringScanner.parseInt(property));
        }
        Class<?> cls = object.getClass();
        Map<String, FieldAccess> fields = Reflection.getPropertyFieldAccessors( cls );
        if ( !fields.containsKey( property ) ) {
            fields = Reflection.getAllAccessorFields( cls );
        }
        if ( !fields.containsKey( property ) ) {
            return null;
        } else {
            return fields.get( property ).getValue( object );
        }
    }