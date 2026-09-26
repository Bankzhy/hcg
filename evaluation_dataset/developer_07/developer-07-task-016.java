private void assignLog4JLevel(Level log4jLevel) {
		if (log4jLevel == null) {
			return;
		}
		if (log4jLevel == Level.DEBUG) {
			level = TraceLevel.FINE;
		}
		else if (log4jLevel == Level.INFO) {
			level = TraceLevel.INFO;
		}
		else if (log4jLevel == Level.WARN) {
			level = TraceLevel.WARNING;
		}
		else if (log4jLevel == Level.ERROR) {
			level = TraceLevel.SEVERE;
		}
		else if (log4jLevel == Level.TRACE) {
			level = TraceLevel.FINEST;
		}
		else if (log4jLevel == Level.OFF) {
			level = TraceLevel.OFF;
		}
	}