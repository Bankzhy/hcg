private String getServiceUrl(Authentication authentication) {
		String serviceUrl;
		if (authentication.getDetails() instanceof ServiceAuthenticationDetails) {
			serviceUrl = ((ServiceAuthenticationDetails) authentication.getDetails())
					.getServiceUrl();
		}
		else if (serviceProperties == null) {
			throw new IllegalStateException(
					"serviceProperties cannot be null unless Authentication.getDetails() implements ServiceAuthenticationDetails.");
		}
		else if (serviceProperties.getService() == null) {
			throw new IllegalStateException(
					"serviceProperties.getService() cannot be null unless Authentication.getDetails() implements ServiceAuthenticationDetails.");
		}
		else {
			serviceUrl = serviceProperties.getService();
		}
		if (logger.isDebugEnabled()) {
			logger.debug("serviceUrl = " + serviceUrl);
		}
		return serviceUrl;
	}