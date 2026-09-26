static public long copyB(InputStream in, OutputStream out, int bufferSize) throws IOException {
    long totalBytesRead = 0;
    int done = 0, next = 1;
    byte[] buffer = new byte[bufferSize];
    while (true) {
      int n = in.read(buffer);
      if (n == -1) break;
      out.write(buffer, 0, n);
      totalBytesRead += n;
      if (showCopy) {
        done += n;
        if (done > 1000 * 1000 * next) {
          System.out.println(next + " Mb");
          next++;
        }
      }
    }
    out.flush();
    return totalBytesRead;
  }