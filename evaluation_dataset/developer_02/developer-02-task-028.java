private static boolean isObject(Type[] formalParameters) {
		if (formalParameters.length != 1) {
			return false;
		}
		final Type type = formalParameters[0];
		if (!(type instanceof Class)) {
			return false;
		}
		if (Types.isPrimitive(type)) {
			return false;
		}
		if (Types.isArrayLike(type)) {
			return false;
		}
		if (Types.isMap(type)) {
			return false;
		}
		if (ConverterRegistry.hasType(type)) {
			return false;
		}
		return true;
	}