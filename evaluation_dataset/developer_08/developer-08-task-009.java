@Override
    public File saveObjectToFile(S3URI s3uri, File file) throws IOException {
        Optional<File> cachedFile = objectFileCache.getIfPresent(s3uri);
        if (cachedFile == null) {
            logger.debug("Object cache MISS: '%s'", s3uri);
        } else {
            logger.debug("Object cache hit: '%s'", s3uri);
            if (!cachedFile.isPresent()) {
                return null;
            } else if (!cachedFile.get().exists()) {
                logger.info(String.format("Found cache entry {'%s'-->'%s'}, but local file doesn't exist. " +
                        "Was it deleted? Re-downloading.", s3uri, cachedFile.get()));
                objectFileCache.invalidate(s3uri);
            } else if (!cachedFile.get().equals(file)) {
                Files.copy(cachedFile.get(), file);
                objectFileCache.put(s3uri, Optional.of(file));
                return file;
            } else {
                return file;
            }
        }
        cachedFile = Optional.fromNullable(threddsS3Client.saveObjectToFile(s3uri, file));
        objectFileCache.put(s3uri, cachedFile);
        return cachedFile.orNull();
    }