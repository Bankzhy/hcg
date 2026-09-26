function(path) {
    var split = path.split(':'),
        propertyPath = split[0],
        classNames = "",
        className,
        falsyClassName;
    if (split.length > 1) {
      className = split[1];
      if (split.length === 3) { falsyClassName = split[2]; }
      classNames = ':' + className;
      if (falsyClassName) { classNames += ":" + falsyClassName; }
    }
    return {
      path: propertyPath,
      classNames: classNames,
      className: (className === '') ? undefined : className,
      falsyClassName: falsyClassName
    };
  }