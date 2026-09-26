public final void setOptions(Map<String, ?> options) {
		this.verify_yubikey_owner = true;
		if (options.get(OPTION_YUBICO_VERIFY_YK_OWNER) != null) {
			if ("false".equals(options.get(OPTION_YUBICO_VERIFY_YK_OWNER).toString())) {
				this.verify_yubikey_owner = false;
			}
		}
		if (options.get(OPTION_YUBICO_ID2NAME_TEXTFILE) != null) {
			this.id2name_textfile = options.get(OPTION_YUBICO_ID2NAME_TEXTFILE).toString();
		}
		if (options.get(OPTION_YUBICO_AUTO_PROVISION) != null) {
			if ("true".equals(options.get(OPTION_YUBICO_AUTO_PROVISION).toString())) {
				this.auto_provision_owners = true;
			}
		}
	}