boolean
    readHeader(InputStream input)
            throws IOException
    {
        byte[] bytehdr = new byte[4];
        int red = input.read(bytehdr);
        if(red == -1) return false;
        if(red < 4)
            throw new IOException("Short binary chunk count");
        this.flags = ((int) bytehdr[0]) & 0xFF;
        bytehdr[0] = 0;
        ByteBuffer buf = ByteBuffer.wrap(bytehdr).order(ByteOrder.BIG_ENDIAN);
        this.chunksize = buf.getInt();
        this.avail = this.chunksize;
        return true;
    }