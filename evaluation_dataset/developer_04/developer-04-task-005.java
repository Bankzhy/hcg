void
    sendDXR(byte[] dxr8)
            throws IOException
    {
        if(dxr8 == null || dxr8.length == 0)
            return;
        if(mode == RequestMode.DMR || mode == RequestMode.DSR) {
            state = State.END;
        } else {
            int flags = DapUtil.CHUNK_DATA;
            if(this.writeorder == ByteOrder.LITTLE_ENDIAN)
                flags |= DapUtil.CHUNK_LITTLE_ENDIAN;
            chunkheader(dxr8.length, flags, this.header);
            output.write(DapUtil.extract(this.header));
            state = State.DATA;
        }
        output.write(dxr8);
        output.flush();
    }