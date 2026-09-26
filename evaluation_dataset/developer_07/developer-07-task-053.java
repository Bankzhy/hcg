protected Authentication attemptSwitchUser(HttpServletRequest request)
			throws AuthenticationException {
		UsernamePasswordAuthenticationToken targetUserRequest;
		String username = request.getParameter(this.usernameParameter);
		if (username == null) {
			username = "";
		}
		if (this.logger.isDebugEnabled()) {
			this.logger.debug("Attempt to switch to user [" + username + "]");
		}
		UserDetails targetUser = this.userDetailsService.loadUserByUsername(username);
		this.userDetailsChecker.check(targetUser);
		targetUserRequest = createSwitchUserToken(request, targetUser);
		if (this.logger.isDebugEnabled()) {
			this.logger.debug("Switch User Token [" + targetUserRequest + "]");
		}
		if (this.eventPublisher != null) {
			this.eventPublisher.publishEvent(new AuthenticationSwitchUserEvent(
					SecurityContextHolder.getContext().getAuthentication(), targetUser));
		}
		return targetUserRequest;
	}