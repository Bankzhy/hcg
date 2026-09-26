public static void fromFloat(FloatBuffer floatBuf, AudioFormat format, ByteBuffer buf) {
        if (!format.isSigned())
            throw new NotSupportedException("Unsigned PCM is not supported ( yet? ).");
        if (format.getSampleSizeInBits() != 16 && format.getSampleSizeInBits() != 24)
            throw new NotSupportedException(format.getSampleSizeInBits() + " bit PCM is not supported ( yet? ).");
        if (format.isBigEndian()) {
            if (format.getSampleSizeInBits() == 16) {
                fromFloat16BE(buf, floatBuf);
            } else {
                fromFloat24BE(buf, floatBuf);
            }
        } else {
            if (format.getSampleSizeInBits() == 16) {
                fromFloat16LE(buf, floatBuf);
            } else {
                fromFloat24LE(buf, floatBuf);
            }
        }
    }