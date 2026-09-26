function getAdd (opts) {
    opts = opts || {}
    var times = opts.times
    var doesConsume = opts.doesConsume
    return function add () {
      var lastArg = arguments[arguments.length - 1]
      var func = typeof lastArg === 'function' ? lastArg : function () { return lastArg }
      var validators = arguments.length > 1 ? Array.prototype.slice.call(arguments, 0, -1) : []
      var newAdapter = {
        doesConsume: doesConsume,
        times: times,
        func: func,
        validators: ut.combineValidators(validators),
        ns: _ns
      }
      _adapters.push(newAdapter)
      ut.filterArray(_events, function (event) {
        if (newAdapter.times === 0) return true
        var filteredAdapters = ut.filterAndSort(event.args, [newAdapter])
        filteredAdapters.forEach(ut.countdown)
        ut.filterArray(_adapters, ut.notExausted)
        ut.triggerAll(event.context, event.args, filteredAdapters)
        return !(doesConsume && filteredAdapters.length)
      })
      return or
    }
  }