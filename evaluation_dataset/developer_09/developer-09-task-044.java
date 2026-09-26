public static String getPrincipal(String principalKey) {
        if ( principalKey == null) {
            return principalKey;
        }
        if (principalKey.length() <= GRANTED_MARKER.length()) {
            return null;
        }
        if ( principalKey.endsWith(GRANTED_MARKER) ) {
          return principalKey.substring(0, principalKey.length()-GRANTED_MARKER.length());
        } else if ( principalKey.endsWith(DENIED_MARKER) ) {
          return principalKey.substring(0, principalKey.length()-DENIED_MARKER.length());
        } else {
          return null;
        }
    }