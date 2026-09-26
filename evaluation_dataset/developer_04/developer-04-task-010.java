private boolean isValidForOptimizedAssistedInject(
      Set<Dependency<?>> dependencies, Class<?> implementation, TypeLiteral<?> factoryType) {
    Set<Dependency<?>> badDeps = null;
    for (Dependency<?> dep : dependencies) {
      if (isInjectorOrAssistedProvider(dep)) {
        if (badDeps == null) {
          badDeps = Sets.newHashSet();
        }
        badDeps.add(dep);
      }
    }
    if (badDeps != null && !badDeps.isEmpty()) {
      logger.log(
          Level.WARNING,
          "AssistedInject factory {0} will be slow "
              + "because {1} has assisted Provider dependencies or injects the Injector. "
              + "Stop injecting @Assisted Provider<T> (instead use @Assisted T) "
              + "or Injector to speed things up. (It will be a ~6500% speed bump!)  "
              + "The exact offending deps are: {2}",
          new Object[] {factoryType, implementation, badDeps});
      return false;
    }
    return true;
  }