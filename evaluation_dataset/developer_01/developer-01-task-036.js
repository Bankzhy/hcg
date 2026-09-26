function formatArray(formatter, value, encode, lengthRequirement) {
  var output = value.slice();
  var formatObject = formatter;
  if (formatter === 'Array|DATA') {
    formatObject = ['D'];
  }
  if (formatter === 'FilterChange' && typeof value[0] === 'string') {
    formatObject = ['D32'];
  }
  if (encode === true
    && typeof lengthRequirement === 'number'
    && value.length < lengthRequirement) {
    throw new Error(`array ${JSON.stringify(value)} must contain at least ${lengthRequirement} params, but only contains ${value.length}.`);
  }
  formatObject = formatObject.slice();
  value.forEach((valueKey, valueIndex) => {
    var formatObjectKey = 0;
    if (formatObject.length > 1) {
      formatObjectKey = valueIndex;
    }
    output[valueIndex] = format(formatObject[formatObjectKey], valueKey, encode);
  });
  return output;
}