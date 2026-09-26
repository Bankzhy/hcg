private int getQuorum(final String quorumSetting, final String iClusterName, final int totalServers, final Object defaultValue,
      final String server) {
    Object value = getClusterConfiguration(iClusterName).field(quorumSetting);
    if (value == null) {
      value = configuration.field(quorumSetting);
      if (value == null) {
        OLogManager.instance()
            .warn(this, "%s setting not found for cluster=%s in distributed-config.json", quorumSetting, iClusterName);
        value = defaultValue;
      }
    }
    if (value instanceof String) {
      if (value.toString().equalsIgnoreCase(QUORUM_MAJORITY))
        value = totalServers / 2 + 1;
      else if (value.toString().equalsIgnoreCase(QUORUM_ALL))
        value = totalServers;
      else if (value.toString().equalsIgnoreCase(QUORUM_LOCAL_DC)) {
        final String dc = getDataCenterOfServer(server);
        if (dc == null)
          throw new OConfigurationException("Data center not specified for server '" + server + "' in distributed configuration");
        value = getDataCenterWriteQuorum(dc);
      } else
        throw new OConfigurationException(
            "The value '" + value + "' is not supported for " + quorumSetting + " in distributed configuration");
    }
    return (Integer) value;
  }