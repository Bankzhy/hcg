public ResourceBundle mergeWithGlobal(ResourceBundle resourceBundle) {
		if (globalResourceBundle == null) {
			if (resourceBundle == null) {
				return EMPTY_RESOURCE_BUNDLE;
			} else {
				return new ResourceBundleWrapper(resourceBundle);
			}
		} else {
			if (resourceBundle == null) {
				return new ResourceBundleWrapper(globalResourceBundle);
			} else {
				return merge(resourceBundle, globalResourceBundle);
			}
		}
	}