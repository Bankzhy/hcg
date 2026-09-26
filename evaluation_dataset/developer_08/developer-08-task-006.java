public void close()
            throws IOException
    {
        if(closed)
            return;
        closed = true;
        if(dmr8 != null) {
            sendDXR(dmr8);
            dmr8 = null;
        }
        if(mode == RequestMode.DMR)
            return;
        if(chunk == null || chunk.position() == 0)
            return;
        verifystate();
        state = State.DATA;
        int flags = DapUtil.CHUNK_END;
        writeChunk(flags);
        state = State.END;
        this.output.flush();
        if(this.saveoutput != null) {
            this.saveoutput.write(((ByteArrayOutputStream) this.output).toByteArray());
        }
    }