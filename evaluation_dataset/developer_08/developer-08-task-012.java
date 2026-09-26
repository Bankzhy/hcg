protected Class loadArrayClassByComponentType(final String className, final ClassLoader classLoader) throws ClassNotFoundException {
		int ndx = className.indexOf('[');
		int multi = StringUtil.count(className, '[');
		String componentTypeName = className.substring(0, ndx);
		Class componentType = loadClass(componentTypeName, classLoader);
		if (multi == 1) {
			return Array.newInstance(componentType, 0).getClass();
		}
		int[] multiSizes;
		if (multi == 2) {
			multiSizes = new int[] {0, 0};
		} else if (multi == 3) {
			multiSizes = new int[] {0, 0, 0};
		} else {
			multiSizes = (int[]) Array.newInstance(int.class, multi);
		}
		return Array.newInstance(componentType, multiSizes).getClass();
	}