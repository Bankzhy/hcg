DictionaryPage readDictionary(ColumnChunkMetaData meta) throws IOException {
    if (!meta.getEncodings().contains(Encoding.PLAIN_DICTIONARY) &&
        !meta.getEncodings().contains(Encoding.RLE_DICTIONARY)) {
      return null;
    }
    if (f.getPos() != meta.getStartingPos()) {
      f.seek(meta.getStartingPos());
    }
    PageHeader pageHeader = Util.readPageHeader(f);
    if (!pageHeader.isSetDictionary_page_header()) {
      return null;
    }
    DictionaryPage compressedPage = readCompressedDictionary(pageHeader, f);
    BytesInputDecompressor decompressor = options.getCodecFactory().getDecompressor(meta.getCodec());
    return new DictionaryPage(
        decompressor.decompress(compressedPage.getBytes(), compressedPage.getUncompressedSize()),
        compressedPage.getDictionarySize(),
        compressedPage.getEncoding());
  }