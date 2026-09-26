function MediaError(value) {
  if (value instanceof MediaError) {
    return value;
  }
  if (typeof value === 'number') {
    this.code = value;
  } else if (typeof value === 'string') {
    this.message = value;
  } else if (isObject(value)) {
    if (typeof value.code === 'number') {
      this.code = value.code;
    }
    assign(this, value);
  }
  if (!this.message) {
    this.message = MediaError.defaultMessages[this.code] || '';
  }
}