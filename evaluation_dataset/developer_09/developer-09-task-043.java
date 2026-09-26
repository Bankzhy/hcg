private List<Resource> findImportedResources(final String resourceUri, final String cssContent)
    throws IOException {
    final List<Resource> imports = new ArrayList<Resource>();
    final String css = cssContent;
    final List<String> foundImports = findImports(css);
    for (final String importUrl : foundImports) {
      final Resource importedResource = createImportedResource(resourceUri, importUrl);
      if (imports.contains(importedResource)) {
        LOG.debug("[WARN] Duplicate imported resource: {}", importedResource);
      } else {
        imports.add(importedResource);
        onImportDetected(importedResource.getUri());
      }
    }
    return imports;
  }