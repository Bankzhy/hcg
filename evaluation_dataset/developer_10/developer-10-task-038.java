public Object decodeFromStream( InputStream in ) throws Exception {
        int read = in.read();
        if ( read < 0 )
            throw new EOFException("stream is closed");
        int ch1 = (read + 256) & 0xff;
        int ch2 = (in.read()+ 256) & 0xff;
        int ch3 = (in.read() + 256) & 0xff;
        int ch4 = (in.read() + 256) & 0xff;
        int len = (ch4 << 24) + (ch3 << 16) + (ch2 << 8) + (ch1 << 0);
        if ( len <= 0 )
            throw new EOFException("stream is corrupted");
        byte buffer[] = new byte[len];
        while (len > 0) {
            len -= in.read(buffer, buffer.length - len, len);
        }
        return getObjectInput(buffer).readObject();
    }