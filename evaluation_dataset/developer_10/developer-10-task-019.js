function trustAs(type, trustedValue) {
      var constructor = (byType.hasOwnProperty(type) ? byType[type] : null);
      if (!constructor) {
        throw $sceMinErr('icontext', 'Attempted to trust a value in invalid context. Context: {0}; Value: {1}',
            type, trustedValue);
      }
      if (trustedValue === null || trustedValue === undefined || trustedValue === '') {
        return trustedValue;
      }
      if (typeof trustedValue !== 'string') {
        throw $sceMinErr('itype',
            'Attempted to trust a non-string value in a content requiring a string: Context: {0}',
            type);
      }
      return new constructor(trustedValue);
    }