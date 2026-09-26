private static float getPrimitivePromotionCost(
      final Class<?> srcClass, final Class<?> destClass) {
    float cost = 0.0f;
    Class<?> cls = srcClass;
    if (!cls.isPrimitive()) {
      cost += 0.1f;
      cls = ClassUtils.wrapperToPrimitive(cls);
    }
    for (int i = 0; cls != destClass && i < ORDERED_PRIMITIVE_TYPES.length; i++) {
      if (cls == ORDERED_PRIMITIVE_TYPES[i]) {
        cost += 0.1f;
        if (i < ORDERED_PRIMITIVE_TYPES.length - 1) {
          cls = ORDERED_PRIMITIVE_TYPES[i + 1];
        }
      }
    }
    return cost;
  }