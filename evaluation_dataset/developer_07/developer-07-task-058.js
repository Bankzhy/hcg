function doSet(store, key, value, options) {
  if (!key || typeof key !== 'string') {
    return false;
  }
  const newData = property.set(store._data, key, value, options);
  if (options.immutable) {
    if (newData !== store._data) {
      store._data = newData;
    } else {
      store.debug('WARNING no change after set "%s', key);
      return false;
    }
  }
  return true;
}