@Override
	public void onAuthenticationFailure(HttpServletRequest request,
			HttpServletResponse response, AuthenticationException exception)
			throws IOException, ServletException {
		for (Map.Entry<Class<? extends AuthenticationException>, AuthenticationFailureHandler> entry : handlers
				.entrySet()) {
			Class<? extends AuthenticationException> handlerMappedExceptionClass = entry
					.getKey();
			if (handlerMappedExceptionClass.isAssignableFrom(exception.getClass())) {
				AuthenticationFailureHandler handler = entry.getValue();
				handler.onAuthenticationFailure(request, response, exception);
				return;
			}
		}
		defaultHandler.onAuthenticationFailure(request, response, exception);
	}