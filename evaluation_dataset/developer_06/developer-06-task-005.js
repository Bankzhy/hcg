function Template(str, options) {
  if(_.isObject(str) && !options){
    options = str;
    str = null;
  }
  options = options ? _.clone(options) : {};
  if(!_.isBoolean(options.cache)) {
    options.cache = process.env.NODE_ENV === 'production';
  }
  options = _.defaults(options, DEFAULTS);
  options.cacheContext = options.cacheContext || Template;
  this.template = str;
  this.options = options;
  this._compiled = null;
  if(options.cache && !(this._getCache() instanceof options.cacheHandler)) {
    var cacheOptions = [options.cacheHandler].concat(options.cacheOptions);
    options.cacheContext[options._cacheProp] = typeof window !== 'undefined' ?
                                                 new options.cacheHandler() :
                                                 construct.apply(this,
                                                                 cacheOptions);
  }
}