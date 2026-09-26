function() {
    var pending = this._pendingSave.slice();
    this._pendingSave = [];
    forEach(pending, function(tuple) {
      var record = tuple[0], resolver = tuple[1],
          adapter = this.adapterFor(record.constructor),
          operation;
      if (get(record, 'isNew')) {
        operation = 'createRecord';
      } else if (get(record, 'isDeleted')) {
        operation = 'deleteRecord';
      } else {
        operation = 'updateRecord';
      }
      resolver.resolve(_commit(adapter, this, operation, record));
    }, this);
  }