public AnnotationVisitor visitLocalVariableAnnotation(
      final int typeRef,
      final TypePath typePath,
      final Label[] start,
      final Label[] end,
      final int[] index,
      final String descriptor,
      final boolean visible) {
    if (api < Opcodes.ASM5) {
      throw new UnsupportedOperationException(REQUIRES_ASM5);
    }
    if (mv != null) {
      return mv.visitLocalVariableAnnotation(
          typeRef, typePath, start, end, index, descriptor, visible);
    }
    return null;
  }