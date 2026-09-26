@Override
  public final void write(final Map<String, Object> pAddParam,
    final Object pEntity, final Writer pWriter) throws Exception {
    Map<String, Map<String, String>> fieldsSettingsMap =
      getMngSettings().lazFldsSts(pEntity.getClass());
    pWriter.write("<entity class=\"" + pEntity.getClass().getCanonicalName()
      + "\"\n");
    for (Map.Entry<String, Map<String, String>> entry
      : fieldsSettingsMap.entrySet()) {
      if ("true".equals(entry.getValue().get("isEnabled"))) {
        Field field = getUtlReflection()
          .retrieveField(pEntity.getClass(), entry.getKey());
        field.setAccessible(true);
        Object fieldValue = field.get(pEntity);
        ISrvFieldWriter srvFieldWriter = getFieldsWritersMap()
          .get(entry.getValue().get("ISrvFieldWriter"));
        if (srvFieldWriter == null) {
          throw new ExceptionWithCode(ExceptionWithCode
            .CONFIGURATION_MISTAKE, "There is no ISrvFieldWriter " + entry
              .getValue().get("ISrvFieldWriter") + " for "
                + pEntity.getClass() + " / " + field.getName());
        }
        srvFieldWriter.write(pAddParam, fieldValue, field.getName(), pWriter);
      }
    }
    pWriter.write("/>\n");
  }