function typeConvert(obj, onlyDate) {
  var i, res;
  if (typeof obj === "object") {
    for (i in obj) {
      if (obj.hasOwnProperty(i)) {
        obj[i] = typeConvert(obj[i], onlyDate);
      }
    }
  } else if (typeof obj === "string") {
    if (!onlyDate && obj.match(/^([0-9.]+|true|false|undefined|null)$/)) {
      obj = eval(obj);
    } else {
      res = obj.match(/^"?(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z)"?$/);
      if (res) {
        obj = new Date(res[1]);
      }
    }
  }
  return obj;
}