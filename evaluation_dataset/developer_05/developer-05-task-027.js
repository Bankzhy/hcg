function decodeSnappy (buffer, cb) {
  if (isChunked(buffer)) {
    var pos = 16;
    var max = buffer.length;
    var encoded = [];
    var size;
    while (pos < max) {
      size = buffer.readUInt32BE(pos);
      pos += 4;
      encoded.push(buffer.slice(pos, pos + size));
      pos += size;
    }
    return async.mapSeries(encoded, snappy.uncompress, function (err, decodedChunks) {
      if (err) return cb(err);
      return cb(null, Buffer.concat(decodedChunks));
    });
  }
  return snappy.uncompress(buffer, cb);
}