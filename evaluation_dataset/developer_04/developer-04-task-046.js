function PromiseResolve () {
    return function F ( resolution ) {
      var promise = F['[[Promise]]'], reactions;
      if ( Type(promise) !== 'object' ) {
        throw TypeError();
      }
      if ( promise['[[PromiseStatus]]'] !== 'unresolved' ) {
        return undefined;
      }
      reactions = promise['[[PromiseResolveReactions]]'];
      defineInternal(promise, '[[PromiseResult]]', resolution);
      defineInternal(promise, '[[PromiseResolveReactions]]', undefined);
      defineInternal(promise, '[[PromiseRejectReactions]]', undefined);
      defineInternal(promise, '[[PromiseStatus]]', 'has-resolution');
      return TriggerPromiseReactions(reactions, resolution);
    };
  }