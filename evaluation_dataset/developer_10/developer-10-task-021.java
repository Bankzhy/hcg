public void remove(String name) {
		Params.notNullOrEmpty(name, "Cookie name");
		if (cookies == null) {
			return;
		}
		for (Cookie cookie : cookies) {
			if (name.equals(cookie.getName())) {
				cookie.setMaxAge(0);
				cookie.setValue("");
				cookie.setPath("/");
				httpResponse.addCookie(cookie);
				break;
			}
		}
	}