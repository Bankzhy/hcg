public static BindInfo bindInfoForEnvEntry(String app, String module, String comp, boolean useCompNamespace, final String envEntryName) {
        if (envEntryName.startsWith("java:")) {
            if (useCompNamespace) {
                return bindInfoFor(app, module, comp, envEntryName);
            } else {
                if (envEntryName.startsWith("java:comp")) {
                    return bindInfoFor(app, module, module, "java:module" + envEntryName.substring("java:comp".length()));
                } else {
                    return bindInfoFor(app, module, module, envEntryName);
                }
            }
        } else {
            if (useCompNamespace) {
                return bindInfoFor(app, module, comp, "java:comp/env/" + envEntryName);
            } else {
                return bindInfoFor(app, module, module, "java:module/env/" + envEntryName);
            }
        }
    }