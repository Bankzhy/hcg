static private boolean isInsideCharClass(String s, int pos) {
        boolean openBracketFound = false;
        boolean closeBracketFound = false;
        String s2 = s.substring(0, pos);
        int posOpen = pos;
        while ((posOpen = s2.lastIndexOf('[', posOpen - 1)) != -1) {
            if (!isEscapedChar(s2, posOpen)) {
                openBracketFound = true;
                break;
            }
        }
        if (openBracketFound) {
            String s3 = s.substring(posOpen, pos);
            int posClose = -1;
            while ((posClose = s3.indexOf(']', posClose + 1)) != -1) {
                if (!isEscapedChar(s3, posClose)) {
                    closeBracketFound = true;
                    break;
                }
            }
        }
        return openBracketFound && !closeBracketFound;
    }