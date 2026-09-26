protected void onURLConnectionPrepared(final Context context, final URLConnection urlConnection) {
    if (contentType != null) {
      urlConnection.addRequestProperty("Content-Type", contentType);
    }
    if (contentLanguage != null) {
      urlConnection.addRequestProperty("Accept-Language", contentLanguage);
    }
    urlConnection.addRequestProperty("Accept-Encoding", IoUtils.ENCODING_GZIP);
    urlConnection.addRequestProperty("User-Agent", buildUserAgent(context));
    if (headers != null) {
      for (String name : headers.keySet()) {
        urlConnection.addRequestProperty(name, headers.getString(name));
      }
    }
  }