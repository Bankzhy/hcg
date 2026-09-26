public static boolean equal(Iterator<?> i1, Iterator<?> i2)
	{
		if (i1 == i2) {
			return true;
		}
		if (i1 == null || i2 == null) {
			return false;
		}
		while (i1.hasNext() && i2.hasNext()) {
			if (!XObjects.equal(i1.next(), i2.next())) {
				return false;
			}
		}
		return !(i1.hasNext() || i2.hasNext());
	}