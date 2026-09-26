function parseDuration(s) {
  s = String(s);
  if (!DURATION_RE.test(s)) {
    return null;
  }
  var parts = s.split(':').map(function (p) {
    return +p;
  });
  if (parts.length === 3) {
    return parts[0] * 3600 + parts[1] * 60 + parts[2];
  } else if (parts.length === 2) {
    return parts[0] * 60 + parts[1];
  } else {
    return parts[0];
  }
}