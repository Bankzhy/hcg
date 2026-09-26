function checkSchemaDescriptorTypes(schemaDescriptors) {
  let onlyPlainObjects = schemaDescriptors.every((descriptor) => {
    return descriptor.constructor === Object
  })
  if (onlyPlainObjects) {
    return
  }
  if (!(schemaDescriptors[0] instanceof DatabaseSchema)) {
    throw new TypeError("The schema descriptor of the lowest described " +
        `database version (${schemaDescriptors[0].version}) must be a ` +
        "DatabaseSchema instance, or all schema descriptors must be plain " +
        "objects")
  }
  schemaDescriptors.slice(1).forEach((descriptor) => {
    if (!(descriptor instanceof UpgradedDatabaseSchema)) {
      throw new TypeError("The schema descriptors of the upgraded database " +
          "versions must be UpgradedDatabaseSchema instances, but the " +
          `provided descriptor of version ${descriptor.version} was not an ` +
          "UpgradedDatabaseSchema instance, or all schema descriptors must " +
          "be plain objects")
    }
  })
}