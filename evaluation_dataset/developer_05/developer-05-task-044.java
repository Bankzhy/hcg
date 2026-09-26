boolean shutdown() throws IOException {
        if (!shutdown) {
            sslEngine.closeOutbound();
            shutdown = true;
        }
        if (outNetBB.hasRemaining() && tryFlush(outNetBB)) {
            return false;
        }
        outNetBB.clear();
        SSLEngineResult result = sslEngine.wrap(hsBB, outNetBB);
        if (result.getStatus() != Status.CLOSED) {
            throw new SSLException("Improper close state");
        }
        outNetBB.flip();
        if (outNetBB.hasRemaining()) {
            tryFlush(outNetBB);
        }
        return (!outNetBB.hasRemaining() &&
                (result.getHandshakeStatus() != HandshakeStatus.NEED_WRAP));
    }