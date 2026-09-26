function get(key, value) {
  var i, parts, name, cookie;
  var result = key ? undefined : {};
  var cookies = (document.cookie || '').split('; ');
  for (i = 0; i < cookies.length; i++) {
    parts = cookies[i].split('=');
    name = this.decode(parts.shift());
    cookie = parts.join('=');
    if (key && key === name) {
      result = this.read(cookie, value);
      break;
    }
    if (!key && (cookie = this.read(cookie)) !== undefined) {
      result[name] = cookie;
    }
  }
  return result;
}