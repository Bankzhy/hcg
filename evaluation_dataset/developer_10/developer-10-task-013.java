private Annotation getAnnotation(Binder binder, Method method) {
    if (method.isBridge() || method.isSynthetic()) {
      return null;
    }
    Annotation annotation = null;
    for (Class<? extends Annotation> annotationClass : scanner.annotationClasses()) {
      Annotation foundAnnotation = method.getAnnotation(annotationClass);
      if (foundAnnotation != null) {
        if (annotation != null) {
          binder.addError(
              "More than one annotation claimed by %s on method %s."
                  + " Methods can only have one annotation claimed per scanner.",
              scanner, method);
          return null;
        }
        annotation = foundAnnotation;
      }
    }
    return annotation;
  }