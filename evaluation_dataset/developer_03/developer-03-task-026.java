private Token parseQuotedChars(char quote) {
	StringBuilder buf = new StringBuilder();
	buf.append(quote);
	while (hasNextChar()) {
	    char ch = nextChar();
	    if (ch == '\\') {
		ch = nextChar();
		if (ch == '\\' || ch == quote) {
		    buf.append(ch);
		}
	    } else if (ch == quote) {
		buf.append(ch);
		break;
	    } else {
		buf.append(ch);
	    }
	}
	return new QuotedString(buf.toString());
    }