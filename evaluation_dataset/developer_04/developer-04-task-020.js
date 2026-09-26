function(name, _skipAssert) {
    var container = this.container,
        route = container.lookup('route:'+name),
        controller;
    if (route && route.controllerName) {
      name = route.controllerName;
    }
    controller = container.lookup('controller:' + name);
    Ember.assert("The controller named '"+name+"' could not be found. Make sure " +
                 "that this route exists and has already been entered at least " +
                 "once. If you are accessing a controller not associated with a " +
                 "route, make sure the controller class is explicitly defined.",
                 controller || _skipAssert === true);
    return controller;
  }