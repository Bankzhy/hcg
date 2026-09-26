public static String[] getClassSimpleFields(Class<?> clazz) {
        Field[] fields = clazz.getDeclaredFields();
        int length = fields.length;
        Collection<Field> fieldCollection = new ArrayList<Field>();
        for (int i = 0; i < length; i++) {
            Field field = fields[i];
            if (isSimpleType(field)) {
                fieldCollection.add(field);
            }
        }
        String[] fieldNames = new String[fieldCollection.size()];
        int i = 0;
        for (Iterator iterator = fieldCollection.iterator(); iterator.hasNext(); ) {
            Field field = (Field) iterator.next();
            fieldNames[i] = field.getName();
            i++;
        }
        return fieldNames;
    }