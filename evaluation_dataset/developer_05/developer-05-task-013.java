public static int countOccurrences(String str, String sub)
	{
		Parameters.checkNotNull(str);
		int n = 0;
		if (!sub.isEmpty()) {
			int start = 0;
			while (true) {
				start = str.indexOf(sub, start);
				if (start == -1) {
					break;
				}
				start += sub.length();
				n++;
			}
		}
		return n;
	}