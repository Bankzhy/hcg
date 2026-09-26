public void start() {
		if (detectEntriesMode) {
			rulesEntries.detectMode();
		}
		filesToScan.forEach(file -> {
			final String path = file.getAbsolutePath();
			if (StringUtil.endsWithIgnoreCase(path, JAR_FILE_EXT)) {
				if (!acceptJar(file)) {
					return;
				}
				scanJarFile(file);
			} else if (file.isDirectory()) {
				scanClassPath(file);
			}
		});
	}