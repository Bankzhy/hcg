private void addPadding()
	{
		int len = BLOCK_LENGTH - bufferLen;
		if (len < 9) {
			len += BLOCK_LENGTH;
		}
		byte[] buf = new byte[len];
		buf[0] = (byte) 0x80;
		for (int i = 1; i < len - 8; i++) {
			buf[i] = (byte) 0x00;
		}
		counter = (counter + (long) bufferLen) * 8L;
		LittleEndian.encode(counter, buf, len - 8);
		update(buf);
	}