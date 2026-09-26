function consul (options, resilient) {
      defineResilientOptions(params, options)
      return {
        'in': function inHandler (err, res, next) {
          if (err) return next()
          if (Array.isArray(res.data) && Object(res.data[0]) === res.data[0]) {
            res.data = mapServers(res.data)
          }
          next()
        },
        'out': function outHandler (options, next) {
          options.params = options.params || {}
          if (params.datacenter) {
            options.params.dc = params.datacenter
          }
          if (params.onlyHealthy) {
            options.params.passing = true
          }
          if (params.tag) {
            options.params.tag = params.tag
          }
          next()
        }
      }
    }