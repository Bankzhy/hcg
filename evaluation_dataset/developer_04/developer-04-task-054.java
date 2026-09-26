public Process getProcessById(String id) {
		AssertHelper.notEmpty(id);
		Process entity = null;
		String processName;
		Cache<String, String> nameCache = ensureAvailableNameCache();
		Cache<String, Process> entityCache = ensureAvailableEntityCache();
		if(nameCache != null && entityCache != null) {
			processName = nameCache.get(id);
			if(StringHelper.isNotEmpty(processName)) {
				entity = entityCache.get(processName);
			}
		}
		if(entity != null) {
			if(log.isDebugEnabled()) {
				log.debug("obtain process[id={}] from cache.", id);
			}
			return entity;
		}
		entity = access().getProcess(id);
		if(entity != null) {
			if(log.isDebugEnabled()) {
				log.debug("obtain process[id={}] from database.", id);
			}
			cache(entity);
		}
		return entity;
	}